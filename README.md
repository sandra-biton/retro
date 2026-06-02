# Release 10.9 Retrospective — Collaborative Project

## Purpose
This repo contains the **Release 10.9 Retrospective RCA & Action Items** report and presentation for Dana, Shlomi, and Rajeev squads. It's designed for collaborative editing — tune the data, fix inaccuracies, and regenerate the slides.

## Files

| File | Description |
|------|-------------|
| `retro_109_rca_action_items.md` | The full retro report (editable markdown) |
| `generate_presentation.py` | Python script to regenerate the PPTX from scratch |
| `retro_109_presentation.pptx` | Generated presentation (26 slides, dark theme) |
| `CONTEXT.md` | Full background context for continuing this work |

## Quick Start

```bash
# Install dependencies
pip install python-pptx requests

# Regenerate slides after editing the report
python generate_presentation.py
```

## How to Collaborate

1. **Edit the markdown report** (`retro_109_rca_action_items.md`) — fix numbers, add context, tune action items
2. **Regenerate slides** by running `python generate_presentation.py`
3. **Push changes** — Sandra will review and align

## Key Decisions Still Pending

- [ ] Squad-to-GM mapping needs final validation (see CONTEXT.md for details)
- [ ] Some squads with 10.9 content may be missing from the report
- [ ] PPTX may need manual polish after generation (fonts, alignment)

## Jira Access

To query live data, you need Jira Cloud access:
- Instance: `https://zerto.atlassian.net`
- API: REST v3 (`POST /rest/api/3/search/jql`)
- Auth: HTTP Basic (email + API token)
- Key fields: `customfield_10101` (Owning Squad), `customfield_10325` (Owning GM)

## Squad Ownership (Validated from Jira)

### In Scope
| GM | Squads |
|----|--------|
| **Dana Mittelman** | Squad Cloud Azure, Squad Cloud Opus, Squad - Eng - Hyper-V, Squad - Eng - Nils, Squad AI Agents |
| **Shlomi Apel** | Squad VRA, Squad Cyber Resilience, Squad Driver, Squad Mavka |
| **Rajeev Srivastav** | Squad Apex Legends, Squad GreenBoat, Squad Core Services |

### NOT in Scope (other GMs)
| GM | Squads |
|----|--------|
| Idan Shama | Boom, DR Cloud Enablement, DR New Platforms |
| Bat-Ami Hain | DevOps Doom, Appliance, Griffin, SaaS |
| Ilan Cohen | DR Recovery, KVM Platform, KVM ZVM Core, Vpg Management |
| Miron Aloni | Scale |
| Sandra Biton | Cloud AWS, Cloud ZIC |

## Timeline
- Sprint 0: Sep 30, 2025
- Feature Freeze: Jan 26, 2026
- Code Freeze: Feb 17, 2026
- GA: May 13, 2026
