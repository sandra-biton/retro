# Full Context for Continuing This Work

## What Was Done

This retrospective was built from **live Jira data** (REST API v3) and the 10.8 retro findings. The full pipeline:

1. Queried Jira for all 10.9 items by squad (regressions, FF breaches, CF breaches)
2. Cross-referenced with 10.8 retro data to track what was/wasn't addressed
3. Analyzed RFT (Ready For Testing) backlog growth trend
4. Measured story and epic lifecycle timing (In Progress → Completed)
5. Wrote RCA per metric with action items per GM
6. Generated PPTX presentation

## Known Issues / Corrections Needed

### 1. Squad Mapping Was Wrong Initially
Originally, Boom, DR Cloud Enablement, and DevOps Doom were counted under Rajeev. This is WRONG:
- **Boom** → Idan Shama (NOT Rajeev)
- **DR Cloud Enablement** → Idan Shama (NOT Rajeev)
- **DevOps Doom** → Bat-Ami Hain (NOT Rajeev)
- **Scale** → Miron Aloni (NOT Dana)

The report has been partially corrected but **numbers may still include wrong squads in totals**.

### 2. Missing Squads With 10.9 Content
These squads had items in 10.9 sprints but are NOT in the report:
| Squad | Items | Regressions | GM |
|-------|-------|-------------|-----|
| GLDR Astra | 187 | 35 | Shlomi |
| Cloud Compliance | 148 | 19 | Dana |
| AI Agents | 120 | 4 | Dana |
| Mavka | 31 | 5 | Shlomi |
| Core Services | ? | ? | Rajeev |

**Decision needed:** Should these be added? If yes, all KPI totals change.

### 3. Cycle Time Methodology
The correct story workflow (confirmed by Sandra):
```
New → In Progress → Ready For Testing → Testing → Completed → Accepted
```
- **Dev Time** = In Progress → Ready For Testing
- **QA Queue** = Ready For Testing → Testing
- **QA Execution** = Testing → Completed
- **Total Active** = In Progress → Completed

"In Review" is NOT a QA status for stories (it's for epics only).

## Jira API Details

### Authentication
```
Email: sandra.biton@hpe.com
Token: <ASK SANDRA FOR THE API TOKEN - do not commit tokens to git>
Base URL: https://zerto.atlassian.net
```

### Key Fields
| Field | ID | Usage |
|-------|-----|-------|
| Owning Squad | `customfield_10101` | Squad assignment |
| Owning GM | `customfield_10325` | GM assignment |
| Sprint | `customfield_10020` | Sprint mapping |
| Regression? | `"Regression?[Dropdown]"` | Yes/No |
| Found in Automation? | `"Found in Automation?[Dropdown]"` | Yes/No |
| Affected Version | `affectedVersion` | Release (10.9) |

### Key Filters (saved in Jira)
| Filter | ID | Description |
|--------|-----|-------------|
| 10.9 FF stories | 21636 | Stories breaching Feature Freeze |
| 10.9 CF stories | 21637 | Stories breaching Code Freeze |
| 10.9 CF bugs | 21638 | Bugs breaching Code Freeze |
| 10.8 Regression Total | 21034 | All 10.8 regressions |

### Example JQL Queries
```jql
-- All 10.9 regressions for a squad
"Owning Team/Squad[Group Picker (single group)]" = "Squad GreenBoat" 
  AND affectedVersion = 10.9 
  AND "Regression?[Dropdown]" = Yes 
  AND status not in (Obsolete)

-- All regressions by GM
"Owning GM[User Picker (single user)]" = "dana.mittelman" 
  AND affectedVersion = 10.9 
  AND "Regression?[Dropdown]" = Yes

-- RFT backlog current
status = "Ready For Testing" 
  AND "Owning Team/Squad[Group Picker (single group)]" in (
    "Squad - Eng - Nils", "Squad Cloud Azure", "Squad Cloud Opus",
    "Squad GreenBoat", "Squad Apex Legends", "Squad Core Services",
    "Squad VRA", "Squad Cyber Resilience", "Squad Driver"
  )
```

### API Pagination (v3)
```python
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("sandra.biton@hpe.com", "<token>")
url = "https://zerto.atlassian.net/rest/api/3/search/jql"

# v3 uses POST with nextPageToken (NOT startAt)
# v3 does NOT return 'total' field
# maxResults must be >= 1

payload = {"jql": "...", "maxResults": 100, "fields": ["summary", "status"]}
resp = requests.post(url, json=payload, auth=auth)
data = resp.json()
issues = data["issues"]
next_token = data.get("nextPageToken")
# Continue with: payload["nextPageToken"] = next_token
```

## Dashboard
- [Release Retrospective Dashboard](https://zerto.atlassian.net/jira/dashboards/10405)

## 10.8 Retro Findings (for cross-reference)
1. Don't enable FE tweaks at end of release → NOT addressed in 10.9
2. React side-by-side comparison with AngularJS → NOT done
3. Increase Cypress coverage → Rate DROPPED
4. Clarify cross-team ownership (GB/Linux) → Same issue
5. Test upgrade scenarios during dev → ADDRESSED (Rajeev stable)
6. Scale/perf setups lacking → Still not ready
7. ZIC timeline different from ZVM → Under discussion
8. Enhance ZIC quality (design, requirements) → NOT addressed

## What To Do Next

1. **Validate all numbers** — re-query Jira to confirm per-squad regression counts
2. **Decide on missing squads** — should GLDR Astra (35 reg, Shlomi), Cloud Compliance (19 reg, Dana), AI Agents (4 reg, Dana) be added?
3. **Recalculate KPI totals** if squads are added/removed
4. **Polish action items** — make them realistic and assign proper owners
5. **Regenerate PPTX** after all corrections
