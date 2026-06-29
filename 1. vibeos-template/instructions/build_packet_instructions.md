# BUILD_PACKET Instructions

## Purpose
Guide the creation or update of a build packet / PRD for a project.

## Use This When
- starting a new tool idea
- shaping a problem into a PRD
- updating scope, risk, or acceptance criteria
- creating a new build packet for a later phase, major feature, or `v2+` slice

## Inputs
- Raw problem notes
- OPS output
- Existing `docs/build_packet.md` if one already exists
- `docs/build_packet_index.md` if multiple build packets exist
- any prior files in `docs/build_packets/` that are relevant to the next slice

## Required Output
Create or update the correct build packet with a concise, high-signal PRD.

## Required Sections
- Title
- Owner
- Risk Level
- Problem Summary
- Users
- Current Workflow
- Desired Workflow
- Success Metrics
- MVP Scope
- Acceptance Criteria
- Inputs
- Outputs
- UI / UX Notes
- Architecture Decision
- Data Sources
- Data Classification
- External AI Use
- Security Constraints
- Edge Cases
- Test Plan
- Deployment
- Links
- Next Step

## Rules
- Keep the doc under 100 lines
- Prefer clear, testable behavior
- Keep MVP small and safe
- Prefer read-only first slices
- State assumptions explicitly
- Do not invent infra or permissions
- Flag missing info instead of guessing
- Use Given / When / Then for acceptance criteria where possible
- Keep links to `project_context`, `STANCE`, `SIGNALS`, and `MINDSET` accurate
  so personas can use the build packet as part of onboarding
- Do not overwrite an older build packet when the work has become a new major slice
- If the next slice deserves its own PRD, create a new file under `docs/build_packets/`
- Keep `docs/build_packet.md` as the root/original project build packet unless there is a strong reason not to
- If multiple build packets exist, update `docs/build_packet_index.md` to mark which one is current

## Multi-Build-Packet SOP

When the project is still one coherent slice:
- update `docs/build_packet.md`

When the project has evolved into a new major phase, feature, subsystem, or version:
- preserve `docs/build_packet.md`
- create a new named file in `docs/build_packets/`
- update `docs/build_packet_index.md`

Examples:
- `docs/build_packets/v2_search_product.md`
- `docs/build_packets/feature_calendar_writeback.md`
- `docs/build_packets/phase_public_preview.md`

## Safety Checks
- No PII/HR/finance/customer data unless explicitly required
- No broad write/admin scopes by default
- No secrets in the document
- No external AI use unless justified and approved
- If risk is unclear, default conservative
