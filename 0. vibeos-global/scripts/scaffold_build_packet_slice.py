#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from pathlib import Path


BUILD_PACKET_INDEX_TEMPLATE = """# BUILD_PACKET_INDEX

## Current Active Build Packet
- `docs/build_packet.md` — status: current — root project build packet

## Root / Original Build Packet
- `docs/build_packet.md` — status: root — original project PRD

## Additional Build Packets
- None yet

## Planned Future Build Packets
- None yet

## Rules
- Always mark exactly one build packet as the current active planning source
- Do not overwrite old major-slice PRDs
- Add new phase / feature / version build packets under `docs/build_packets/`
- Keep old build packets listed here after they stop being current
"""


CURRENT_STATUS_TEMPLATE = """# Current Status Overview

## Project Identity
- Project: {project_name}
- What it is: <1-2 line summary>
- Who it serves: <primary users / stakeholders>

## Current Active Slice
- Current active build packet: `docs/build_packet.md`
- Current phase / version / major surface: <current active slice>
- What is actively in scope right now: <active scope>

## What Already Exists
- <major capability or decision>
- <major capability or decision>
- <stable context to preserve>

## What Has Changed Since The Original PRD
- <new constraint>
- <new opportunity>
- <changed scope boundary>

## Open Tensions
- <what is unclear or overloaded>
- <why a fresh PRD may be justified>

## Recommended Next PRD Slice
- Proposed build packet name: `docs/build_packets/{slice_filename}`
- What it should cover: <next slice scope>
- What it should not cover: <explicit exclusions>

## Inputs The PRD GPT Should Treat As Source Of Truth
- `docs/build_packet.md`
- `docs/project_context.md`
- `docs/build_packet_index.md`
- `project cognitive layer/STANCE.md`
- `project cognitive layer/SIGNALS.md`
- `project cognitive layer/MINDSET.md`
- <other relevant files>

## Preservation Rules
- Preserve `docs/build_packet.md` as the root/original project build packet
- Do not overwrite older build packets
- Preserve historical context that should remain true
"""


BUILD_PACKET_TEMPLATE = """# BUILD_PACKET

## Title
{title}

## Owner
<owner>

## Risk Level
Level 1 / Level 2 / Level 3

---

## Problem Summary
Who is affected:
<who this slice is for>

What is happening:
<what new phase / feature / subsystem needs planning>

Why it matters:
<why this deserves its own build packet>

---

## Users
Primary:
- <primary user>

Secondary:
- <secondary user>

---

## Current Workflow
1. <current step>
2. <current step>
3. <current step>

---

## Desired Workflow
1. <desired step>
2. <desired step>
3. <desired step>

---

## Success Metrics
- <metric>
- <metric>

---

## MVP Scope
In scope:
- <in-scope item>

Out of scope:
- <out-of-scope item>

---

## Acceptance Criteria (Given / When / Then)
- Given <context>, when <action>, then <expected result>.

---

## Inputs
- Systems:
  - <system>
- Data:
  - <data>

---

## Outputs
- <output>

---

## UI / UX Notes
- <ux note>

---

## Architecture Decision (High Level)
Surface:
<surface>

Runtime:
<runtime>

Key components:
- <component>

---

## Data Sources
- <source>

---

## Data Classification
- <classification>

---

## External AI Use
- <none or scoped usage>

---

## Security Constraints
- <constraint>

---

## Edge Cases
- <edge case>

---

## Test Plan (Stub)
- Happy path: <happy path>
- Failure case: <failure case>

---

## Deployment (Stub)
Where:
<where it runs>

Trigger:
<trigger>

Kill switch:
<kill switch>

---

## Links
Root Build Packet:
`docs/build_packet.md`

Build Packet Index:
`docs/build_packet_index.md`

Current Status Overview:
`docs/{current_status_filename}`

---

## Next Step
-> Refine this slice and decide whether it becomes the current active build packet
"""


def slugify(value: str) -> str:
    slug = value.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    slug = re.sub(r"_+", "_", slug)
    return slug.strip("_")


def ensure_file(path: Path, content: str) -> bool:
    if path.exists():
        return False
    path.write_text(content, encoding="utf-8")
    return True


def replace_none_yet_block(text: str, heading: str, new_line: str) -> str:
    marker = f"## {heading}\n"
    if marker not in text:
        return text
    before, after = text.split(marker, 1)
    lines = after.splitlines()
    updated: list[str] = []
    inserted = False
    i = 0
    while i < len(lines):
        line = lines[i]
        if not inserted and line.strip() == "- None yet":
            updated.append(new_line)
            inserted = True
            i += 1
            continue
        updated.append(line)
        i += 1
    if not inserted:
        updated.insert(0, new_line)
    return before + marker + "\n".join(updated)


def append_index_entry(index_path: Path, rel_build_packet: str, title: str, status: str) -> None:
    text = index_path.read_text(encoding="utf-8")
    entry = f"- `{rel_build_packet}` — status: {status} — {title}"
    if entry in text or rel_build_packet in text:
        return

    heading = "Planned Future Build Packets" if status == "planned" else "Additional Build Packets"
    updated = replace_none_yet_block(text, heading, entry)
    if updated == text:
        # Fallback append under the chosen heading if the structure drifts.
        marker = f"## {heading}\n"
        if marker in text:
            updated = text.replace(marker, marker + entry + "\n", 1)
        else:
            updated = text.rstrip() + f"\n\n## {heading}\n{entry}\n"
    index_path.write_text(updated, encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a new build-packet slice for an existing VibeOS project."
    )
    parser.add_argument("project", help="Project folder name or path")
    parser.add_argument("slice_name", help="Human-readable slice name, e.g. 'Google Sites V1 Catalog'")
    parser.add_argument(
        "--status",
        choices=["planned", "parallel"],
        default="planned",
        help="How to register the new slice in docs/build_packet_index.md",
    )
    parser.add_argument(
        "--workspace",
        default=None,
        help="Workspace root override. Defaults to the parent of 0. vibeos-global.",
    )
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    workspace = Path(args.workspace).resolve() if args.workspace else script_dir.parent.parent
    projects_root = workspace / "projects"

    project_input = Path(args.project)
    if project_input.is_absolute():
        project_dir = project_input
    else:
        canonical_project_dir = projects_root / project_input
        legacy_project_dir = workspace / project_input
        if canonical_project_dir.is_dir():
            project_dir = canonical_project_dir
        elif legacy_project_dir.is_dir():
            project_dir = legacy_project_dir
        else:
            project_dir = canonical_project_dir
    project_dir = project_dir.resolve()

    if not project_dir.is_dir():
        parser.error(f"Project directory not found: {project_dir}")

    docs_dir = project_dir / "docs"
    if not docs_dir.is_dir():
        parser.error(f"Project does not have docs/: {project_dir}")

    build_packet_path = docs_dir / "build_packet.md"
    if not build_packet_path.exists():
        parser.error(f"Project is missing docs/build_packet.md: {project_dir}")

    build_packets_dir = docs_dir / "build_packets"
    build_packets_dir.mkdir(exist_ok=True)

    index_path = docs_dir / "build_packet_index.md"
    ensure_file(index_path, BUILD_PACKET_INDEX_TEMPLATE)

    project_name = project_dir.name
    slice_slug = slugify(args.slice_name)
    build_packet_filename = f"{slice_slug}.md"
    current_status_filename = f"current_status_overview_{slice_slug}.md"

    build_packet_rel = f"docs/build_packets/{build_packet_filename}"
    current_status_rel = f"docs/{current_status_filename}"

    current_status_path = docs_dir / current_status_filename
    build_packet_slice_path = build_packets_dir / build_packet_filename

    status_created = ensure_file(
        current_status_path,
        CURRENT_STATUS_TEMPLATE.format(
            project_name=project_name,
            slice_filename=build_packet_filename,
        ),
    )
    build_packet_created = ensure_file(
        build_packet_slice_path,
        BUILD_PACKET_TEMPLATE.format(
            title=args.slice_name,
            current_status_filename=current_status_filename,
        ),
    )

    append_index_entry(index_path, build_packet_rel, args.slice_name, args.status)

    print(f"Project: {project_dir}")
    print(f"Build packet index: {index_path}")
    print(f"Current status overview: {current_status_path} ({'created' if status_created else 'already existed'})")
    print(
        f"Build packet slice: {build_packet_slice_path} ({'created' if build_packet_created else 'already existed'})"
    )
    print(f"Registered in index as: {args.status}")
    print("Next step: fill the current status overview, then refine the new build packet slice.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
