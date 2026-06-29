#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Iterable


WORKSPACE_EXCLUDE = {
    ".agents",
    "0. vibeos-global",
    "1. vibeos-template",
    "2. vibeos-skills",
    "projects",
    "output",
    "plugins",
    "tmp",
}

BASE_REQUIRED_DOCS = [
    "docs/project_context.md",
]

BASE_REQUIRED_INSTRUCTIONS = [
    "instructions/stance_instructions.md",
    "instructions/signals_instructions.md",
    "instructions/mindset_instructions.md",
]

BUILD_REQUIRED_DOCS = [
    "docs/build_packet.md",
]

BUILD_REQUIRED_INSTRUCTIONS = [
    "instructions/build_packet_instructions.md",
]

ENGOPS_CANONICAL_DOC = "docs/operating_brief.md"
ENGOPS_CANONICAL_INSTRUCTION = "instructions/operating_brief_instructions.md"

REQUIRED_COGNITIVE = [
    "project cognitive layer/STANCE.md",
    "project cognitive layer/SIGNALS.md",
    "project cognitive layer/MINDSET.md",
    "project cognitive layer/0. stance_instructions.md",
    "project cognitive layer/0. signals_instructions.md",
    "project cognitive layer/0. mindset_instructions.md",
]

ALLOWED_TOP_LEVEL_DIRS = {
    "ai_inventory",
    "apps_script_mvp",
    "apps_script_v1",
    "config",
    "docs",
    "instructions",
    "out",
    "pjdh",
    "project cognitive layer",
    "prompts",
    "reporting",
    "scripts",
    "skills",
    "src",
    "tests",
    "time_windows",
    "ui",
}

PROMPT_EXPECTATIONS = {
    "BUILD_PACKET": "../instructions/build_packet_instructions.md",
    "STANCE Update": "../project cognitive layer/0. stance_instructions.md",
    "SIGNALS Extraction": "../project cognitive layer/0. signals_instructions.md",
    "MINDSET Proposal": "../project cognitive layer/0. mindset_instructions.md",
}

ENGOPS_PROMPT_EXPECTATIONS = {
    "OPERATING BRIEF": "../instructions/operating_brief_instructions.md",
    "STANCE Update": "../project cognitive layer/0. stance_instructions.md",
    "SIGNALS Extraction": "../project cognitive layer/0. signals_instructions.md",
    "MINDSET Proposal": "../project cognitive layer/0. mindset_instructions.md",
}

FRAMEWORK_SKILL_DOCS = [
    "OS_INDEX.md",
    "CLAUDE.md",
    "0. vibeos-global/SKILLS_CHEATSHEET.md",
    "0. vibeos-global/standards/SKILL_STANDARD.md",
]


@dataclass
class Finding:
    severity: str
    check: str
    message: str
    critical: bool = False


@dataclass
class ProjectReport:
    project: str
    level: str
    findings: list[Finding] = field(default_factory=list)


def parse_projects_index(workspace: Path) -> dict[str, dict[str, str]]:
    index = workspace / "projects" / "INDEX.md"
    if not index.exists():
        return {}

    registry: dict[str, dict[str, str]] = {}
    for line in index.read_text(encoding="utf-8", errors="replace").splitlines():
        if not line.startswith("|"):
            continue
        cols = [col.strip().strip("*") for col in line.strip().strip("|").split("|")]
        if not cols or cols[0] in {"Folder", ""} or set(cols[0]) <= {"-"}:
            continue
        if len(cols) < 6:
            continue
        registry[cols[0]] = {
            "name": cols[1],
            "confidentiality": cols[2],
            "description": cols[3],
            "domain": cols[4],
            "type": cols[5],
        }
    return registry


def project_kind(workspace: Path, project_dir: Path) -> str:
    registry = parse_projects_index(workspace)
    meta = registry.get(project_dir.name, {})
    domain = meta.get("domain", "").strip().lower()
    if domain == "eng ops":
        return "engops"
    if domain in {"build", "personal"}:
        return "build"
    if (project_dir / ENGOPS_CANONICAL_DOC).exists():
        return "engops"
    return "build"


def discover_projects(workspace: Path) -> list[Path]:
    projects: list[Path] = []
    projects_root = workspace / "projects"
    if not projects_root.is_dir():
        return projects
    for child in sorted(projects_root.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir() or child.name.startswith("."):
            continue
        if (child / "docs").is_dir() or (child / "project cognitive layer").is_dir() or (child / "instructions").is_dir():
            projects.append(child)
    return projects


def discover_legacy_root_projects(workspace: Path) -> list[Path]:
    legacy: list[Path] = []
    for child in sorted(workspace.iterdir(), key=lambda p: p.name.lower()):
        if not child.is_dir() or child.name in WORKSPACE_EXCLUDE or child.name.startswith("."):
            continue
        if (child / "START_HERE.md").exists() and (
            (child / "docs").is_dir() or (child / "project cognitive layer").is_dir() or (child / "instructions").is_dir()
        ):
            legacy.append(child)
    return legacy


def discover_skill_dirs(workspace: Path) -> list[Path]:
    skills_root = workspace / "2. vibeos-skills" / "skills"
    if not skills_root.is_dir():
        return []
    return [
        child
        for child in sorted(skills_root.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir() and not child.name.startswith(".")
    ]


def discover_persona_dirs(workspace: Path) -> list[Path]:
    personas_root = workspace / "0. vibeos-global" / "personas"
    if not personas_root.is_dir():
        return []
    return [
        child
        for child in sorted(personas_root.iterdir(), key=lambda p: p.name.lower())
        if child.is_dir() and not child.name.startswith(".")
    ]


def persona_agent_name(persona_dir: Path) -> str:
    without_index = re.sub(r"^\d+\.\s*", "", persona_dir.name)
    return without_index.split(" ", 1)[0].strip().lower()


def generated_route_text(workspace: Path, source: Path) -> str:
    return source.read_text(encoding="utf-8", errors="replace").replace("{{VIBEOS_ROOT}}", str(workspace))


def doc_mentions_skill(text: str, skill_name: str) -> bool:
    return f"/{skill_name}" in text or f"`{skill_name}`" in text or f"`/{skill_name}`" in text


def add_finding(findings: list[Finding], severity: str, check: str, message: str, critical: bool = False) -> None:
    findings.append(Finding(severity=severity, check=check, message=message, critical=critical))


def parse_prompt_follow_paths(prompts_md: Path) -> dict[str, str]:
    text = prompts_md.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    mapping: dict[str, str] = {}
    current_heading = ""
    for idx, line in enumerate(lines):
        if line.startswith("## "):
            current_heading = line[3:].strip()
        if line.strip() == "Follow:" and current_heading:
            if idx + 1 < len(lines):
                mapping[current_heading] = lines[idx + 1].strip()
    return mapping


def resolve_prompt_path(prompt_mapping: dict[str, str], prefix: str) -> str | None:
    for heading, path in prompt_mapping.items():
        if heading == prefix or heading.startswith(prefix + " "):
            return path
    return None


def has_malformed_residue(project_dir: Path) -> list[str]:
    hits: list[str] = []
    for child in project_dir.iterdir():
        if not child.is_dir():
            continue
        if child.name in ALLOWED_TOP_LEVEL_DIRS or child.name.startswith("."):
            continue
        # Strong residue heuristic: odd top-level dir with its own venv structure.
        if (child / "pyvenv.cfg").exists() or ((child / "bin").is_dir() and (child / "lib").is_dir()):
            hits.append(child.name)
        elif re.fullmatch(r"[#%&]+", child.name):
            hits.append(child.name)
    return sorted(set(hits))


def evaluate_project(workspace: Path, project_dir: Path) -> ProjectReport:
    findings: list[Finding] = []
    projects_root = workspace / "projects"
    in_projects_root = project_dir.parent == projects_root
    kind = project_kind(workspace, project_dir)

    if not in_projects_root:
        add_finding(
            findings,
            "FAIL",
            "legacy_root_project",
            f"Project must live under projects/: {project_dir.name}",
            critical=True,
        )

    if not (project_dir / "START_HERE.md").exists():
        add_finding(findings, "FAIL", "start_here", "Missing START_HERE.md", critical=True)

    for rel_path in BASE_REQUIRED_DOCS:
        if not (project_dir / rel_path).exists():
            add_finding(findings, "FAIL", "required_docs", f"Missing {rel_path}", critical=True)

    if kind == "engops":
        has_operating_brief = (project_dir / ENGOPS_CANONICAL_DOC).exists()
        has_legacy_build_packet = (project_dir / "docs/build_packet.md").exists()
        if not has_operating_brief and not has_legacy_build_packet:
            add_finding(
                findings,
                "FAIL",
                "required_docs",
                f"Missing {ENGOPS_CANONICAL_DOC} or transitional docs/build_packet.md",
                critical=True,
            )
        elif not has_operating_brief:
            add_finding(
                findings,
                "WARN",
                "engops_operating_brief_missing",
                f"Eng Ops project still uses transitional docs/build_packet.md; add {ENGOPS_CANONICAL_DOC} on next substantive touch",
            )
    else:
        for rel_path in BUILD_REQUIRED_DOCS:
            if not (project_dir / rel_path).exists():
                add_finding(findings, "FAIL", "required_docs", f"Missing {rel_path}", critical=True)

    if not (project_dir / "instructions").is_dir():
        add_finding(findings, "FAIL", "instructions_dir", "Missing instructions/ directory", critical=True)

    if (project_dir / "project instructions").exists():
        add_finding(
            findings,
            "FAIL",
            "deprecated_instructions_dir",
            "Deprecated project instructions/ directory present",
            critical=True,
        )

    for rel_path in BASE_REQUIRED_INSTRUCTIONS:
        if not (project_dir / rel_path).exists():
            add_finding(findings, "FAIL", "required_instructions", f"Missing {rel_path}", critical=True)

    if kind == "engops":
        if (project_dir / ENGOPS_CANONICAL_DOC).exists() and not (project_dir / ENGOPS_CANONICAL_INSTRUCTION).exists():
            add_finding(
                findings,
                "FAIL",
                "required_instructions",
                f"Missing {ENGOPS_CANONICAL_INSTRUCTION}",
                critical=True,
            )
    else:
        for rel_path in BUILD_REQUIRED_INSTRUCTIONS:
            if not (project_dir / rel_path).exists():
                add_finding(findings, "FAIL", "required_instructions", f"Missing {rel_path}", critical=True)

    if not (project_dir / "project cognitive layer").is_dir():
        add_finding(findings, "FAIL", "cognitive_dir", "Missing project cognitive layer/ directory", critical=True)

    for rel_path in REQUIRED_COGNITIVE:
        if not (project_dir / rel_path).exists():
            add_finding(findings, "FAIL", "required_cognitive", f"Missing {rel_path}", critical=True)

    encoded_alias = project_dir.name.replace(" ", "%20")
    if encoded_alias != project_dir.name and (workspace / encoded_alias).exists():
        add_finding(
            findings,
            "FAIL",
            "encoded_duplicate_root",
            f"Encoded duplicate root exists: {encoded_alias}",
            critical=True,
        )

    if in_projects_root and (workspace / project_dir.name).exists():
        add_finding(
            findings,
            "FAIL",
            "duplicate_root_project",
            f"Legacy root-level project duplicate exists: {project_dir.name}",
            critical=True,
        )

    malformed = has_malformed_residue(project_dir)
    if malformed:
        add_finding(
            findings,
            "FAIL",
            "malformed_residue",
            f"Malformed residue directories present: {', '.join(malformed)}",
            critical=True,
        )

    prompts_md = project_dir / "prompts" / "prompts.md"
    if prompts_md.exists():
        prompt_mapping = parse_prompt_follow_paths(prompts_md)
        expectations = ENGOPS_PROMPT_EXPECTATIONS if kind == "engops" and (project_dir / ENGOPS_CANONICAL_DOC).exists() else PROMPT_EXPECTATIONS
        for heading_prefix, expected_path in expectations.items():
            actual = resolve_prompt_path(prompt_mapping, heading_prefix)
            if actual is None:
                add_finding(
                    findings,
                    "WARN",
                    "prompt_mapping",
                    f"Prompt section missing Follow path: {heading_prefix}",
                )
            elif actual != expected_path:
                add_finding(
                    findings,
                    "WARN",
                    "prompt_mapping",
                    f"{heading_prefix} points to {actual}, expected {expected_path}",
                )
            elif not (prompts_md.parent / actual).exists():
                add_finding(
                    findings,
                    "FAIL",
                    "prompt_target_missing",
                    f"{heading_prefix} target does not exist: {actual}",
                    critical=True,
                )
    else:
        add_finding(findings, "WARN", "prompts_missing", "prompts/prompts.md not present")

    project_context = project_dir / "docs" / "project_context.md"
    if project_context.exists():
        text = project_context.read_text(encoding="utf-8", errors="replace")
        if "project cognitive layer/STANCE.md" not in text:
            add_finding(
                findings,
                "WARN",
                "project_context_links",
                "project_context.md does not clearly reference project cognitive layer/STANCE.md as source of truth",
            )
    if (project_dir / "src").exists() and not (project_dir / "tests").exists():
        add_finding(findings, "WARN", "tests_missing", "src/ exists without tests/")

    if not (project_dir / "README.md").exists():
        add_finding(findings, "WARN", "readme_missing", "README.md not present")

    if list(project_dir.rglob(".DS_Store")):
        add_finding(findings, "WARN", "ds_store", ".DS_Store files present")

    critical_fail = any(f.severity == "FAIL" and f.critical for f in findings)
    warn_count = sum(1 for f in findings if f.severity == "WARN")

    if critical_fail:
        level = "Level 3"
    elif warn_count > 2:
        level = "Level 2"
    else:
        level = "Level 1"

    return ProjectReport(project=project_dir.name, level=level, findings=findings)


def evaluate_framework(workspace: Path) -> ProjectReport:
    findings: list[Finding] = []
    skill_dirs = discover_skill_dirs(workspace)
    skill_names = {skill_dir.name for skill_dir in skill_dirs}
    routing_commands_dir = workspace / "routing" / "commands"
    generated_commands_dir = workspace / ".claude" / "commands"
    routing_agents_dir = workspace / "routing" / "agents"
    generated_agents_dir = workspace / ".claude" / "agents"

    for skill_dir in skill_dirs:
        skill_name = skill_dir.name
        if not (skill_dir / "SKILL.md").exists():
            add_finding(findings, "FAIL", "skill_contract", f"Missing SKILL.md for skill: {skill_name}", critical=True)
        if not (skill_dir / "agents" / "openai.yaml").exists():
            add_finding(
                findings,
                "FAIL",
                "skill_contract",
                f"Missing agents/openai.yaml for skill: {skill_name}",
                critical=True,
            )

        skill_md = skill_dir / "SKILL.md"
        if skill_md.exists():
            stext = skill_md.read_text(encoding="utf-8", errors="replace")
            name_match = re.search(r"^name:\s*(.+)$", stext, re.MULTILINE)
            if name_match and name_match.group(1).strip() != skill_name:
                add_finding(
                    findings,
                    "FAIL",
                    "skill_frontmatter",
                    f"{skill_name}/SKILL.md frontmatter name '{name_match.group(1).strip()}' != folder '{skill_name}'",
                    critical=True,
                )
            low = stext.lower()
            if "## context requirement" not in low:
                add_finding(findings, "WARN", "skill_sections", f"{skill_name}/SKILL.md missing a Context Requirement section")
            if not ("## process" in low or "## workflow" in low):
                add_finding(findings, "WARN", "skill_sections", f"{skill_name}/SKILL.md missing a Process/Workflow section")
            if not ("## required output" in low or "## required outputs" in low or "## output" in low):
                add_finding(findings, "WARN", "skill_sections", f"{skill_name}/SKILL.md missing a Required output section")
            if not ("## checks before finalizing" in low or "## guardrails" in low):
                add_finding(findings, "WARN", "skill_sections", f"{skill_name}/SKILL.md missing a Checks before finalizing section")
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if openai_yaml.exists():
            ytext = openai_yaml.read_text(encoding="utf-8", errors="replace")
            for key in ("display_name", "short_description", "default_prompt"):
                if key not in ytext:
                    add_finding(findings, "WARN", "skill_openai_keys", f"{skill_name}/agents/openai.yaml missing key: {key}")

        routing_command = routing_commands_dir / f"{skill_name}.md"
        generated_command = generated_commands_dir / f"{skill_name}.md"
        if not routing_command.exists():
            add_finding(
                findings,
                "FAIL",
                "command_route_missing",
                f"Missing routing/commands/{skill_name}.md",
                critical=True,
            )
        if not generated_command.exists():
            add_finding(
                findings,
                "FAIL",
                "generated_command_missing",
                f"Missing .claude/commands/{skill_name}.md; run scripts/setup_machine.sh",
                critical=True,
            )
        if routing_command.exists() and generated_command.exists():
            expected = generated_route_text(workspace, routing_command)
            actual = generated_command.read_text(encoding="utf-8", errors="replace")
            if actual != expected:
                add_finding(
                    findings,
                    "FAIL",
                    "generated_command_drift",
                    f".claude/commands/{skill_name}.md differs from routing/commands/{skill_name}.md; run scripts/setup_machine.sh",
                    critical=True,
                )

        # Dispatcher target must actually exist and match the command name.
        if routing_command.exists():
            route_text = routing_command.read_text(encoding="utf-8", errors="replace")
            target_match = re.search(r"skills/([^/\n]+)/SKILL\.md", route_text)
            if not target_match:
                add_finding(
                    findings,
                    "FAIL",
                    "route_target_unparsable",
                    f"routing/commands/{skill_name}.md does not reference a skills/<name>/SKILL.md target",
                    critical=True,
                )
            else:
                target_folder = target_match.group(1)
                if not (workspace / "2. vibeos-skills" / "skills" / target_folder / "SKILL.md").exists():
                    add_finding(
                        findings,
                        "FAIL",
                        "route_target_missing",
                        f"routing/commands/{skill_name}.md points to a non-existent skill target: skills/{target_folder}/SKILL.md",
                        critical=True,
                    )
                elif target_folder != skill_name:
                    add_finding(
                        findings,
                        "FAIL",
                        "route_target_mismatch",
                        f"routing/commands/{skill_name}.md targets skills/{target_folder}/ but the command is {skill_name}",
                        critical=True,
                    )

        for rel_doc in FRAMEWORK_SKILL_DOCS:
            doc = workspace / rel_doc
            if not doc.exists():
                add_finding(findings, "FAIL", "framework_doc_missing", f"Missing {rel_doc}", critical=True)
                continue
            text = doc.read_text(encoding="utf-8", errors="replace")
            if not doc_mentions_skill(text, skill_name):
                add_finding(
                    findings,
                    "WARN",
                    "skill_index_missing",
                    f"{rel_doc} does not mention skill: {skill_name}",
                )

    route_names = {path.stem for path in routing_commands_dir.glob("*.md")} if routing_commands_dir.is_dir() else set()
    generated_names = {path.stem for path in generated_commands_dir.glob("*.md")} if generated_commands_dir.is_dir() else set()
    for stale in sorted(route_names - skill_names):
        add_finding(findings, "WARN", "stale_command_route", f"routing/commands/{stale}.md has no matching skill folder")
    for stale in sorted(generated_names - skill_names):
        add_finding(findings, "WARN", "stale_generated_command", f".claude/commands/{stale}.md has no matching skill folder")

    persona_dirs = discover_persona_dirs(workspace)
    persona_names = {persona_agent_name(persona_dir) for persona_dir in persona_dirs}
    for persona_dir in persona_dirs:
        agent_name = persona_agent_name(persona_dir)
        if not (persona_dir / "PERSONA.md").exists():
            add_finding(
                findings,
                "FAIL",
                "persona_contract",
                f"Missing PERSONA.md for persona folder: {persona_dir.name}",
                critical=True,
            )
        for req_file in ("MINDSET.md", "SIGNALS.md", "STARTER_PROMPT.md"):
            if not (persona_dir / req_file).exists():
                add_finding(
                    findings,
                    "FAIL",
                    "persona_contract",
                    f"Missing {req_file} for persona folder: {persona_dir.name}",
                    critical=True,
                )
        persona_md = persona_dir / "PERSONA.md"
        if persona_md.exists():
            ptext = persona_md.read_text(encoding="utf-8", errors="replace")
            for header in ("## Role", "## Lens", "## When to invoke", "## Handoffs"):
                if header not in ptext:
                    add_finding(
                        findings,
                        "WARN",
                        "persona_sections",
                        f"{persona_dir.name}/PERSONA.md missing section: {header}",
                    )
        mindset_md = persona_dir / "MINDSET.md"
        if mindset_md.exists() and "## Calibration" not in mindset_md.read_text(encoding="utf-8", errors="replace"):
            add_finding(
                findings,
                "WARN",
                "persona_calibration",
                f"{persona_dir.name}/MINDSET.md has no ## Calibration section",
            )
        routing_agent = routing_agents_dir / f"{agent_name}.md"
        generated_agent = generated_agents_dir / f"{agent_name}.md"
        if not routing_agent.exists():
            add_finding(
                findings,
                "FAIL",
                "agent_route_missing",
                f"Missing routing/agents/{agent_name}.md",
                critical=True,
            )
        if not generated_agent.exists():
            add_finding(
                findings,
                "FAIL",
                "generated_agent_missing",
                f"Missing .claude/agents/{agent_name}.md; run scripts/setup_machine.sh",
                critical=True,
            )
        if routing_agent.exists() and generated_agent.exists():
            expected = generated_route_text(workspace, routing_agent)
            actual = generated_agent.read_text(encoding="utf-8", errors="replace")
            if actual != expected:
                add_finding(
                    findings,
                    "FAIL",
                    "generated_agent_drift",
                    f".claude/agents/{agent_name}.md differs from routing/agents/{agent_name}.md; run scripts/setup_machine.sh",
                    critical=True,
                )

    route_agent_names = {path.stem for path in routing_agents_dir.glob("*.md")} if routing_agents_dir.is_dir() else set()
    generated_agent_names = {path.stem for path in generated_agents_dir.glob("*.md")} if generated_agents_dir.is_dir() else set()
    for stale in sorted(route_agent_names - persona_names):
        add_finding(findings, "WARN", "stale_agent_route", f"routing/agents/{stale}.md has no matching persona folder")
    for stale in sorted(generated_agent_names - persona_names):
        add_finding(findings, "WARN", "stale_generated_agent", f".claude/agents/{stale}.md has no matching persona folder")

    critical_fail = any(f.severity == "FAIL" and f.critical for f in findings)
    warn_count = sum(1 for f in findings if f.severity == "WARN")
    if critical_fail:
        level = "Level 3"
    elif warn_count > 2:
        level = "Level 2"
    else:
        level = "Level 1"

    return ProjectReport(project="VibeOS Framework", level=level, findings=findings)


def render_text(reports: Iterable[ProjectReport]) -> str:
    lines: list[str] = []
    for report in reports:
        lines.append(f"Project: {report.project}")
        lines.append(f"Conformance Level: {report.level}")
        critical_fails = [f for f in report.findings if f.severity == "FAIL" and f.critical]
        warns = [f for f in report.findings if f.severity == "WARN"]
        other_fails = [f for f in report.findings if f.severity == "FAIL" and not f.critical]
        if critical_fails:
            lines.append("Critical FAIL:")
            for finding in critical_fails:
                lines.append(f"- [{finding.check}] {finding.message}")
        if other_fails:
            lines.append("FAIL:")
            for finding in other_fails:
                lines.append(f"- [{finding.check}] {finding.message}")
        if warns:
            lines.append("WARN:")
            for finding in warns:
                lines.append(f"- [{finding.check}] {finding.message}")
        if not report.findings:
            lines.append("PASS:")
            lines.append("- No findings")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate VibeOS workspace project conformance.")
    parser.add_argument(
        "projects",
        nargs="*",
        help="Optional project folder names to validate. Defaults to all detected VibeOS projects.",
    )
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of text.")
    parser.add_argument(
        "--workspace",
        default=None,
        help="Override workspace root. Defaults to the parent of 0. vibeos-global.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent.parent

    all_projects = discover_projects(workspace)
    legacy_projects = discover_legacy_root_projects(workspace)
    if args.projects:
        wanted = set(args.projects)
        projects = [p for p in all_projects + legacy_projects if p.name in wanted]
        missing = wanted - {p.name for p in projects}
        if missing:
            parser.error(f"Unknown project(s): {', '.join(sorted(missing))}")
    else:
        projects = all_projects + legacy_projects

    reports = []
    if not args.projects:
        reports.append(evaluate_framework(workspace))
    reports.extend(evaluate_project(workspace, project_dir) for project_dir in projects)

    if args.json:
        payload = [asdict(report) for report in reports]
        print(json.dumps(payload, indent=2))
    else:
        print(render_text(reports), end="")

    return 1 if any(report.level == "Level 3" for report in reports) else 0


if __name__ == "__main__":
    raise SystemExit(main())
