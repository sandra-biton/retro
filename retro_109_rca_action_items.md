# Release 10.9 Retrospective — RCA & Action Items
## Scope: Dana, Shlomi, Rajeev squads only
### Timeline: Sprint 0 (Sep 30) → FF (Jan 26) → CF (Feb 17) → GA (May 13)

---

## 📊 KPI Comparison: 10.8 → 10.9 (Our Squads Only)

| Metric | KPI | 10.8 | 10.9 | Δ | Trend | Jira |
|--------|-----|------|------|---|-------|------|
| **Breached FF** (open stories) | 0 | 37 | [25](https://zerto.atlassian.net/issues/?filter=21636) | -12 | ✅ Improved (-32%) | [Filter 21636](https://zerto.atlassian.net/issues/?filter=21636) |
| **Breached CF** (open stories) | 0 | 23 | [36](https://zerto.atlassian.net/issues/?filter=21637) | +13 | ❌ Worse (+57%) | [Filter 21637](https://zerto.atlassian.net/issues/?filter=21637) |
| **Breached CF** (open bugs) | 0 | 4 | [6](https://zerto.atlassian.net/issues/?filter=21638) | +2 | ❌ Worse | [Filter 21638](https://zerto.atlassian.net/issues/?filter=21638) |
| **Regression total** | <10 | 50 | [152](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%2C%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%2C%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | +102 | ❌ Worse (+204%) | [JQL](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%2C%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%2C%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Regression in hardening** | <4 | 17 | 60 | +43 | ❌ Worse (+253%) | (created >= 2026-02-17) |
| **Regression by automation** | +20% rate | 32% | TBD | — | ❌ Dropped | — |

---

## Per-GM Breakdown

### Dana Mittelman

Squads: Nils, Azure, Opus, Hyper-V, AI Agents, Cloud Compliance

| Metric | 10.8 | 10.9 | Δ | Jira |
|--------|------|------|---|------|
| Breached FF | 7 | [6](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021636) | ✅ -1 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021636) |
| Breached CF Stories | 6 | [2](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021637) | ✅ -4 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021637) |
| Breached CF Bugs | 2 | [2](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021638) | ➡️ Same | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20filter%20%3D%2021638) |
| Regression total | 19 | [95](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | ❌ +76 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20-%20Eng%20-%20Nils%22%2C%22Squad%20Cloud%20Azure%22%2C%22Squad%20Cloud%20Opus%22%2C%22Squad%20-%20Eng%20-%20Hyper-V%22%2C%22Squad%20AI%20Agents%22%2C%22Squad%20Cloud%20Compliance%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| Regression hardening | 11 | 37 | ❌ +26 | (created >= 2026-02-17) |

**Per-squad regression breakdown:**
| Squad | Regressions | Hardening | FF | CF |
|-------|:-----------:|:---------:|:--:|:--:|
| [Nils](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20-%20Eng%20-%20Nils%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 60 | 27 | 2 | 0 |
| [Cloud Compliance](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Compliance%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 19 | 2 | 0 | 0 |
| [Azure](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Azure%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 8 | 4 | 2 | 0 |
| [Opus](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Opus%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 4 | 4 | 0 | 0 |
| [AI Agents](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20AI%20Agents%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 4 | 0 | 2 | 2 |
| Hyper-V | 0 | 0 | 0 | 0 |

**FF/CF: Improved.** CF stories down 6→2.
**Regressions: Massively worse.** 19 → 95 (+400%), driven by Nils (60) and Cloud Compliance (19).

### Shlomi Apel

Squads: VRA, Cyber Resilience, Driver, Mavka

| Metric | 10.8 | 10.9 | Δ | Jira |
|--------|------|------|---|------|
| Breached FF | 0 | [8](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021636) | ❌ +8 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021636) |
| Breached CF Stories | 3 | [9](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021637) | ❌ +6 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021637) |
| Breached CF Bugs | 2 | [2](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021638) | ➡️ Same | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20filter%20%3D%2021638) |
| Regression total | 4 | [27](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | ❌ +23 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20VRA%22%2C%22Squad%20Cyber%20Resilience%22%2C%22Squad%20Driver%22%2C%22Squad%20Mavka%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| Regression hardening | 1 | 17 | ❌ +16 | (created >= 2026-02-17) |

**Per-squad regression breakdown:**
| Squad | Regressions | Hardening | FF | CF |
|-------|:-----------:|:---------:|:--:|:--:|
| [Driver](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 11 | 10 | 1 | 1 |
| [VRA](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20VRA%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 10 | 6 | 0 | 0 |
| [Mavka](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Mavka%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 5 | 0 | 0 | 4 |
| [Cyber Resilience](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 1 | 1 | 7 | 4 |

**All metrics worse.** Driver (11 reg, 10 in hardening), VRA (10 reg), Mavka (5 reg + 4 CF). Cyber Resilience: 7 FF breaches from late requirements.

### Rajeev Srivastav

Squads: Apex Legends, GreenBoat, Core Services

| Metric | 10.8 | 10.9 | Δ | Jira |
|--------|------|------|---|------|
| Breached FF | 30 | [11](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021636) | ✅ -19 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021636) |
| Breached CF Stories | 14 | [25](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021637) | ❌ +11 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021637) |
| Breached CF Bugs | 0 | [2](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021638) | ❌ +2 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20filter%20%3D%2021638) |
| Regression total | 27 | [30](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | ❌ +3 | [link](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20in%20%28%22Squad%20Apex%20Legends%22%2C%22Squad%20GreenBoat%22%2C%22Squad%20Core%20Services%22%29%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| Regression hardening | 5 | 6 | ➡️ +1 | (created >= 2026-02-17) |

**Per-squad regression breakdown:**
| Squad | Regressions | Hardening | FF | CF |
|-------|:-----------:|:---------:|:--:|:--:|
| [GreenBoat](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 22 | 4 | 4 | 13 |
| [Apex Legends](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) | 8 | 2 | 7 | 12 |
| Core Services | 0 | 0 | 0 | 0 |

**FF improved significantly** (30→11). **Regressions slightly up** 27→30. **CF breach nearly doubled** — GreenBoat (13) + Apex Legends (12).

---

## 🔍 RCA per Metric (with 10.8 Retro Cross-Reference)

### 1. Breached FF — Stories open after Feature Freeze (Total: [25](https://zerto.atlassian.net/issues/?filter=21636))

| Squad | Count | Root Cause | Jira |
|-------|-------|-----------|------|
| Cyber Resilience (Shlomi) | 7 | Late requirements (LTS Support, Integration Hub received end of Sprint 3). Design approved end Sprint 4 — known FF miss, RIH filed | [7 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20filter%20%3D%2021636) |
| Apex Legends (Rajeev) | 7 | Secret Centralization stories moved to "Ready for Testing" before FF, but QA bandwidth limited → acceptance after FF | [7 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20filter%20%3D%2021636) |
| GreenBoat (Rajeev) | 4 | Dependencies on GB dev completion (Linux migration) + waiver to work during FF | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20filter%20%3D%2021636) |
| Nils (Dana) | 2 | FE tweaks enabled late (same issue as 10.8) | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20-%20Eng%20-%20Nils%22%20AND%20filter%20%3D%2021636) |
| Cloud Azure (Dana) | 2 | AWS stories "ready for testing prior FF" but not accepted | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Azure%22%20AND%20filter%20%3D%2021636) |
| AI Agents (Dana) | 2 | New squad in 10.9 — stories not completed by FF | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20AI%20Agents%22%20AND%20filter%20%3D%2021636) |
| Driver (Shlomi) | 1 | FF-breaching story also breached CF | [1 issue](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20filter%20%3D%2021636) |

**Was this addressed from 10.8?**
- 10.8 retro said: "Avoid enabling tweaks after FF" → ❌ Repeated (Dana/Nils)
- 10.8 retro said: "ZIC timeline different from ZVM" → ⏳ Under discussion (Shlomi)
- **New in 10.9:** Late requirement injection (Shlomi) — not a recurring issue

---

### 2. Breached CF — Stories still open at Code Freeze (Total: [36](https://zerto.atlassian.net/issues/?filter=21637))

| Squad | Count | Root Cause | Jira |
|-------|-------|-----------|------|
| GreenBoat (Rajeev) | 13 | Public Cloud testing setup not ready for FF and still being stabilized. GB had waiver for FF work, pushed CF | [13 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20filter%20%3D%2021637) |
| Apex Legends (Rajeev) | 12 | Testing started late so stories remained in testing phase past CF | [12 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20filter%20%3D%2021637) |
| Mavka (Shlomi) | 4 | Stories carried into hardening | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Mavka%22%20AND%20filter%20%3D%2021637) |
| Cyber Resilience (Shlomi) | 4 | LTS stories (3/6 of CF breach) — known late start. Also: "Do we need to treat Testplan creation in this metric?" | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20filter%20%3D%2021637) |
| AI Agents (Dana) | 2 | New squad, stories not completed by CF | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20AI%20Agents%22%20AND%20filter%20%3D%2021637) |
| Driver (Shlomi) | 1 | Urgent HF pushed due to customer case (LTR). HV stabilization prolonged | [1 issue](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20filter%20%3D%2021637) |

**Was this addressed from 10.8?**
- 10.8 retro said: "Enhance ZIC quality by improving design, requirements, test planning" → ❌ CF breach worse
- 10.8 retro said: "Scale and performance setups lacking" → ❌ Not fixed. Same finding by Shlomi in 10.9
- **New in 10.9:** HV testing setup + signing server availability (Shlomi's finding)

---

### 3. Regression Total — 50 → 152 (+204%)

| Squad | 10.8 | 10.9 | Δ | RCA | Jira |
|-------|------|------|---|-----|------|
| **Nils** (Dana) | 16 | 60 | +44 | React Migration — all bugs in new implementation are classified as regressions. Missing PO requirements. Tweaks activated at end of release | [60 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20-%20Eng%20-%20Nils%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **GreenBoat** (Rajeev) | 15 | 22 | +7 | Upgrade scenarios (10.8→10.9 migration), External Vault Secrets, EF Cache. GB/Linux migration code conflict with AWS | [22 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Cloud Compliance** (Dana) | — | 19 | — | Security/compliance bugs. 0/19 found by automation | [19 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Compliance%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Driver** (Shlomi) | 1 | 11 | +10 | VME/VAIO bugs — driver loading failures, FOT IO errors, VRA sync issues. "Bugs caused by low quality dev testing" (Shlomi's finding) | [11 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **VRA** (Shlomi) | 3 | 10 | +7 | Scale issues — VRA sync slow at scale, public cloud VRA version mismatch | [10 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20VRA%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Azure** (Dana) | 3 | 8 | +5 | GPv2 performance issues, recovery operations stuck — related to new GPv2 feature | [8 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Azure%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Apex Legends** (Rajeev) | 6 | 8 | +2 | Secret Centralization + testing started late | [8 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Mavka** (Shlomi) | — | 5 | — | CF breach stories | [5 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Mavka%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **AI Agents** (Dana) | — | 4 | — | 2 FF + 2 CF breaches. New squad in 10.9 | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20AI%20Agents%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Opus** (Dana) | — | 4 | — | Cloud platform regressions | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Opus%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Cyber Resilience** (Shlomi) | — | 1 | — | Single regression | [1 issue](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29) |
| **Core Services** (Rajeev) | — | 0 | — | No regressions | — |
| **Hyper-V** (Dana) | — | 0 | — | No regressions | — |

**Was this addressed from 10.8?**
- 10.8 said: "React — perform more side-by-side comparisons with AngularJS" → ❌ NOT DONE. Nils went 16→60
- 10.8 said: "Increase Cypress coverage" → ❌ Automation rate dropped
- 10.8 said: "Clarify ownership for cross-team changes (GB/Linux migration)" → ❌ Same conflict repeated
- 10.8 said: "Testing started late so regression came late" (Rajeev) → Apex went 6→8, Driver 1→11

---

### 4. Regression During Hardening — 17 → 60 (+253%)

| Squad | Count | RCA | Jira |
|-------|-------|-----|------|
| **Nils** (Dana) | 27 | React tweaks turned ON during hardening → instant regressions in production code | [27 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20-%20Eng%20-%20Nils%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Driver** (Shlomi) | 10 | VME/VAIO - bugs found late because testing started late | [10 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **VRA** (Shlomi) | 6 | Scale bugs only visible on large setups | [6 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20VRA%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Azure** (Dana) | 4 | GPv2 + Linux migration tool must be developed after ZVM RC → inherently late | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Azure%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Opus** (Dana) | 4 | Cloud platform regressions found in hardening | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Opus%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **GreenBoat** (Rajeev) | 4 | Upgrade path bugs | [4 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Cloud Compliance** (Dana) | 2 | Security bugs found in hardening | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Cloud%20Compliance%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Apex Legends** (Rajeev) | 2 | Late testing | [2 issues](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20%28single%20group%29%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20%28Obsolete%29%20AND%20created%20%3E%3D%20%222026-02-17%22) |
| **Cyber Resilience** (Shlomi) | 1 | Single regression in hardening | — |

**Was this addressed from 10.8?**
- 10.8 said: "Avoid enabling FE tweaks at end of release" → ❌ NOT DONE. 27/37 Dana hardening regressions are Nils/React
- **New root cause:** Linux migration tool has structural dependency on RC → will always create late regressions unless decoupled

---

### 5. Regression Detected by Automation — 32% → 12.6%

**This is the most concerning metric.** The KPI target is +20% improvement, we went BACKWARDS.

| Factor | Analysis |
|--------|----------|
| Automation found 16/50 bugs in 10.8 | Good detection |
| Automation found only 12/95 bugs in 10.9 | Poor detection |
| New bugs concentrated in React (Nils) and VME (Driver) | These areas have LOW automation coverage |
| React has Cypress coverage but it's insufficient for complex scenarios | Per Dana: "Increase Cypress coverage in high-risk and complex areas" |
| VME/Driver has minimal automation | Per Shlomi: "N/A" — no automation improvement proposed |

---

## 📋 Improvements That DID Happen (10.8 → 10.9)

| What | Evidence | GM |
|------|----------|-----|
| ✅ FF discipline improved | 37→27 breaches (-27%) | All GMs |
| ✅ Dana's CF breach → zero | 6→0 stories at CF | Dana |
| ✅ Rajeev FF halved | 30→13 | Rajeev |
| ✅ Apex: regressions halved | 6→3 | Rajeev |
| ✅ Rajeev regression stable | 27→27 despite more scope | Rajeev |
| ✅ 10.9 upgrade testing focus | "In 10.9 we are focusing on upgrade test scenarios during development" | Rajeev |

---

## 🎯 ACTION ITEMS

### Dana Mittelman — Priority: REGRESSION (54 bugs, +35 from 10.8)

| # | Action Item | Owner | Deadline | Success Metric |
|---|-------------|-------|----------|----------------|
| D1 | **Enforce tweak activation policy**: No FE tweak may be activated after Sprint 5 (one sprint before FF). Requires dev+QA sign-off before activation. | Dana + Nils TL | 10.10 Sprint 1 | Zero regressions from late-activated tweaks |
| D2 | **React Migration quality gate**: Require side-by-side visual comparison with AngularJS for every React page before merge. Add to Definition of Done. | Nils TL | 10.10 Sprint 2 | Nils regressions < 20 (down from 47) |
| D3 | **Cypress coverage plan for React**: Define Cypress test matrix for all React-migrated pages. Use Copilot to accelerate. Target: top 5 high-traffic pages covered by Sprint 3 | Nils QA Lead | 10.10 Sprint 3 | Automation detection rate > 25% for Nils bugs |
| D4 | **Decouple Linux Migration tool from RC**: Investigate if stub/mock RC can be used for development, so tool doesn't create forced-late regressions | Azure TL | 10.10 Sprint 2 (design) | Linux migration regressions moved to pre-CF |

---

### Shlomi Apel — Priority: ALL METRICS REGRESSED

| # | Action Item | Owner | Deadline | Success Metric |
|---|-------------|-------|----------|----------------|
| S1 | **Driver squad: mandatory dev self-testing checklist** before marking "Ready for Testing". Define 5 basic scenarios per feature that dev must execute. | Driver TL | 10.10 Sprint 1 | Driver regressions < 4 (down from 8) |
| S2 | **HV testing setup always-available policy**: Ensure HV signing server and testing setup are persistent (not provisioned on-demand). Raise to infra team if needed. | Shlomi + DevOps | 10.10 Sprint 1 | Zero CF breaches from setup unavailability |
| S3 | **Scale testing capacity**: Escalate to VP/Infra for dedicated Public Cloud scale test environment. Current gap causes late CF breaches and late regression discovery. | Shlomi → VP | 10.10 planning | Scale tests can run parallel to dev (not sequential) |
| S4 | **Cyber Resilience: earlier requirement intake**. Requirements must be locked by Sprint 2. Any requirement after Sprint 2 → automatic RIH + FF waiver pre-approval. | Shlomi + PO | 10.10 Sprint 0 | Zero FF breaches from late requirements |
| S5 | **VRA scale regression prevention**: Add scale checkpoint at Sprint 4 (mid-release) where VRA sync time is measured. Don't wait for hardening to discover scale issues. | VRA TL | 10.10 Sprint 4 | VRA P1 scale regressions = 0 |

---

### Rajeev Srivastav — Priority: CF BREACH (26 stories)

| # | Action Item | Owner | Deadline | Success Metric |
|---|-------------|-------|----------|----------------|
| R1 | **GreenBoat: stabilize Public Cloud test environment BEFORE Sprint 5**. Define environment readiness criteria. If not met by Sprint 5, descope features dependent on it. | GB TL + QA | 10.10 Sprint 5 checkpoint | GB CF breach < 5 (down from 13) |
| R2 | **Cross-team impact ownership contract**: For features that touch other teams' code (e.g., GB → AWS/Linux migration), define a signed ownership doc at design phase specifying who fixes bugs in each module. | Rajeev + Dana | 10.10 Sprint 1 | Zero cross-team blame escalations |
| R3 | **Apex Legends: QA bandwidth reservation**. If stories are "Ready for Testing" before FF but QA can't test them → pre-allocate QA capacity in Sprint 5-6 for acceptance. | Apex TL + QA Lead | Sprint 5 planning | Zero FF breaches from "ready but not tested" |
| R4 | **Upgrade regression gate**: Continue 10.9 practice of testing upgrade scenarios during development. Add upgrade test to CI pipeline for GreenBoat. | GB TL | 10.10 Sprint 2 | Upgrade regressions < 3 (down from ~5) |

---

### Org-Level (Sandra)

| # | Action Item | Owner | Deadline | Success Metric |
|---|-------------|-------|----------|----------------|
| O1 | **Automation investment plan**: Current rate (12.6%) is far below KPI (+20%). Request dedicated automation sprint per GM to cover gaps in React, VME/Driver, and Public Cloud. | Sandra + QA Dir | 10.10 Sprint 0 | Automation rate > 25% next release |
| O2 | **Tweak policy enforcement**: Make tweak activation a formal release milestone (not a dev decision). Create Jira workflow step: "Tweak Activation" must happen by Sprint 5. | Sandra | 10.10 Sprint 0 | Measurable in Jira |
| O3 | **ZIC/different-timeline decision**: Formally decide whether ZIC squads (Cyber Resilience) are measured on same FF/CF dates or get different milestones. Current ambiguity causes confusion in metrics. | Sandra + Shlomi | 10.10 Sprint 0 | Clear KPI definition |
| O4 | **Mid-release regression checkpoint (Sprint 4)**: Review regression count at mid-release. If any squad > 5 regressions by Sprint 4, trigger remediation plan immediately. | Sandra | Every Sprint 4 | Early intervention, not post-mortem |

---

## 📈 QA-Dev Interface: Ready For Testing (RFT) Backlog

### RFT Backlog Growth Trend (10.9 → Today)

| Milestone | Items in RFT | Notes |
|-----------|:------------:|-------|
| 10.9 Sprint 1 | 75 | Baseline |
| 10.9 Sprint 4 | 84 | +12% |
| 10.9 Feature Freeze | 87 | Stable |
| 10.9 Code Freeze | 45 | Consumed during hardening |
| 10.10 Sprint 1 | 94 | Immediately refilled |
| 10.10 Sprint 2 | 169 | ⚠️ Spike |
| **Today** | **196** | **❌ +161% from 10.9 baseline** |

### RFT at Feature Freeze: 10.8 vs 10.9

| | 10.8 FF | 10.9 FF | Δ |
|-|:-------:|:-------:|:-:|
| Items in RFT | 39 | 64 | ❌ +64% |
| Stuck > 3 weeks | 3 | 7 | ❌ Doubled |

### Per-Squad RFT Breakdown (Current: 196 items)

| Squad (GM) | Items | Avg Age | Max Age | Concern |
|------------|:-----:|:-------:|:-------:|---------|
| Nils (Dana) | 50 | 71d | >180d | ⚠️ Largest backlog |
| Boom (Idan Shama) | 34 | 57d | >120d | Not in scope |
| Opus (Dana) | 31 | 57d | >120d | |
| Azure (Dana) | 25 | 97d | >180d | ⚠️ Highest avg age |
| Apex Legends (Rajeev) | 16 | 90d | >180d | |

**Key Stats:** 148/196 items (75%) have been in RFT > 30 days. 55 items > 3 months.

### RFT Transit Time (sample of resolved 10.9 items)

| GM | n | Avg Days in RFT | Median | Max |
|----|:-:|:---------------:|:------:|:---:|
| Rajeev Srivastav | 7 | 37d | 7d | 84d |
| Dana Mittelman | 1 | 0d | — | — |

**Example:** ZER-167251 — entered RFT Oct 19, completed Feb 23 (**127 days in RFT**).

### RCA: Why is RFT growing?
- **QA bandwidth is fixed** while dev output increases — items accumulate faster than QA can consume
- **No RFT WIP limit** — there is no policy triggering action when RFT exceeds a threshold
- **No aging alerts** — items sit unnoticed for months without escalation
- **Hardening drains RFT temporarily** (87→45 at CF) but dev refills it immediately after (→196 today)

---

## ⏱️ Epic & Story Lifecycle SLA Analysis

### Epic Workflow
```
New → Ready For Development → In Development → In Review → Ready To Ship
       (FR done)               (dev starts)                  (shipped)
```

### Story Workflow
```
New → In Progress → Ready For Testing → Testing → Completed → Accepted
      (dev starts)  (dev done, QA queue) (QA active) (QA done)  (approved)
```

### Epic Phase Duration (10.9 epics, n=50 sampled)

| Phase | Meaning | n | Avg | Median | P90 | Max |
|-------|---------|:-:|:---:|:------:|:---:|:---:|
| **FR (New → Ready For Dev)** | Feature Requirements & Design | 11 | 71d | 21d | 212d | 331d |
| **Planning (Ready For Dev → In Dev)** | Wait time before dev starts | 10 | 43d | 30d | 140d | 140d |

### Epic Phase Duration — Per GM

| GM | Phase | n | Avg | Median | Max |
|----|-------|:-:|:---:|:------:|:---:|
| **Shlomi** | FR (New → Ready For Dev) | 4 | 94d | 21d | 331d |
| **Shlomi** | Planning (Ready For Dev → In Dev) | 3 | 26d | 25d | 29d |
| **Rajeev** | FR (New → Ready For Dev) | 7 | 57d | 35d | 212d |
| **Rajeev** | Planning (Ready For Dev → In Dev) | 7 | 50d | 47d | 140d |

⚠️ Dana's epics have insufficient lifecycle data — most were created in earlier releases and transitions not tracked cleanly.

---

### Story Lifecycle Timing (measured from In Progress, n=80 sampled)

| Phase | Meaning | n | Avg | Median | P90 | Max |
|-------|---------|:-:|:---:|:------:|:---:|:---:|
| **Dev Time** (In Progress → Ready For Testing) | Development | 44 | 27d | 12d | 34d | 393d |
| **QA Queue** (Ready For Testing → Testing) | Waiting for QA | 45 | 25d | 14d | 70d | 143d |
| **QA Execution** (Testing → Completed) | Active testing | 43 | 15d | 3d | 42d | 125d |
| **Total Active** (In Progress → Completed) | End-to-end | 61 | 56d | 27d | 146d | 470d |

### Story Lifecycle — Per GM

| GM | Dev Time (avg/med) | QA Queue (avg/med) | QA Execution (avg/med) | Total Active (avg/med) |
|----|:------------------:|:------------------:|:---------------------:|:---------------------:|
| **Dana** | 7d / 5d | 15d / 19d | 2d / 0d | **18d / 11d** |
| **Shlomi** | 11d / 7d | 10d / 6d | 6d / 2d | **24d / 21d** |
| **Rajeev** | 42d / 15d | 44d / 29d | 33d / 28d | **90d / 74d** ⚠️ |

### Story Lifecycle — Per Squad

| Squad (GM) | Total Active (avg/med) | QA Queue (avg/med) | Concern |
|------------|:---------------------:|:------------------:|---------|
| GreenBoat (Rajeev) | 95d / 80d | 45d / 29d | ⚠️ Longest cycle + longest QA queue |
| Apex Legends (Rajeev) | 83d / 27d | 41d / 26d | ⚠️ High variability |
| Cyber Resilience (Shlomi) | 24d / 24d | 11d / 6d | ✅ Healthy |
| Cloud Azure (Dana) | 19d / 19d | 16d / 19d | ✅ Healthy |

### Design Story Active Cycle (In Progress → Completed/Accepted)

| GM | n | Avg | Median | Max |
|----|:-:|:---:|:------:|:---:|
| **All** | 16 | 31d | 27d | 78d |
| Dana Mittelman | 10 | 30d | 27d | 76d |
| Shlomi Apel | 4 | 42d | 50d | 78d |
| Rajeev Srivastav | 2 | 17d | 23d | 23d |

### Test Plan (TP) Story Active Cycle (In Progress → Completed/Accepted)

| GM | n | Avg | Median | Max |
|----|:-:|:---:|:------:|:---:|
| **All** | 3 | 56d | 43d | 102d |
| Rajeev Srivastav | 3 | 56d | 43d | 102d |

(Dana/Shlomi TP stories did not pass through standard In Progress → Completed flow)

### Key Findings: Where Does Time Go?

1. **QA queue is the #1 time sink for Rajeev** — 44 days avg waiting in "Ready For Testing" before QA picks it up. GreenBoat=45d, Apex=41d.
2. **Rajeev's total active cycle is 4-5x longer than Dana/Shlomi** — 90d vs 18-24d. Driven by long dev time (42d) AND long QA queue (44d) AND long QA execution (33d).
3. **Dana and Shlomi have healthy cycles** — 18d and 24d respectively. QA queue is reasonable (10-15d).
4. **FR Phase (epic level) is 71 days avg** — Shlomi's epics avg 94d, Rajeev's 57d. Both exceed a reasonable 30d target.
5. **Planning idle (epic level) is 43 days** — after FR is complete, epics sit ~6 weeks before dev starts. Rajeev's avg 50d.
6. **Design stories are efficient once started** — 31d avg active cycle. Not a bottleneck.

---

### 🎯 ADDITIONAL ACTION ITEMS (RFT & Lifecycle)

| # | Action Item | Owner | Deadline | Success Metric |
|---|-------------|-------|----------|----------------|
| L1 | **RFT WIP limit policy**: Set maximum RFT threshold per squad (e.g., 15 items). When breached, dev must stop new feature work and assist QA with test execution. | Sandra + QA Dir | 10.10 Sprint 1 | RFT backlog < 100 at FF (down from 196) |
| L2 | **RFT aging alert**: Weekly automated report of items in RFT > 30 days, sent to GM + TL. Items > 60 days require written justification. | Sandra (dashboard) | 10.10 Sprint 1 | Zero items > 90d in RFT |
| L3 | **Reduce FR phase duration**: Require epic FR completion within 30 days of creation. If requirements aren't ready, epic stays in backlog — don't create epic prematurely. | PO + GM | 10.10 Sprint 0 | FR phase < 30d avg (down from 71d) |
| L4 | **Eliminate planning idle time**: Once epic is "Ready for Development", squad must pick it up within 2 sprints (4 weeks). If not, descope or reassign. | GMs | Ongoing | Planning wait < 21d avg (down from 43d) |
| L5 | **Rajeev: QA queue SLA**: Stories must not sit in "Ready For Testing" longer than 14 days. Current avg is 44d. Investigate QA capacity gap in GreenBoat/Apex. | Rajeev + QA Leads | 10.10 Sprint 2 | QA queue < 14d avg (down from 44d) |

---

## Summary: What Was Raised in 10.8 and What Actually Happened

| 10.8 Retro Finding | Suggested Improvement | 10.9 Result | Verdict |
|--------------------|----------------------|-------------|---------|
| FE tweaks enabled late → regressions | Don't turn on tweaks at end of release | Same issue, Nils regressions 16→47 | ❌ NOT ADDRESSED |
| React needs side-by-side comparison | Perform comparisons with AngularJS earlier | Not done. React classified as regressions "by definition" | ❌ NOT ADDRESSED |
| Increase Cypress coverage | Leverage Copilot for test creation | Automation rate dropped 32%→12.6% | ❌ NOT ADDRESSED |
| Clarify cross-team ownership (GB) | Define ownership for impacting changes | Same GB/Linux migration/AWS blame issue | ❌ NOT ADDRESSED |
| Testing started late (Rajeev) | Upgrade test during development | Rajeev regressions FLAT (27→27) | ✅ ADDRESSED (stable) |
| Scale setups lacking (Shlomi) | Increase investment in scale/perf setups | HV/Public Cloud setup still not ready | ❌ NOT ADDRESSED |
| ZIC timeline is different | Separate ZIC metrics | Under discussion, not decided | ⏳ IN PROGRESS |
| Enhance ZIC quality (design, requirements) | Improve design/test planning | Cyber Resilience FF breach +7 | ❌ NOT ADDRESSED |

**Score: 1/8 improvements implemented. 1/8 in progress. 6/8 not addressed.**

---

## Jira Links

- [Dashboard: Release Retrospective](https://zerto.atlassian.net/jira/dashboards/10405)
- [10.9 FF Breach Filter](https://zerto.atlassian.net/issues/?filter=21636)
- [10.9 CF Stories Filter](https://zerto.atlassian.net/issues/?filter=21637)
- [10.9 CF Bugs Filter](https://zerto.atlassian.net/issues/?filter=21638)
- [10.8 Regression Total](https://zerto.atlassian.net/issues/?filter=21034)
### Per-Squad Regressions (10.9)
- [Nils Regressions (47)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20-%20Eng%20-%20Nils%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [GreenBoat Regressions (17)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [Driver Regressions (8)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Driver%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [Azure Regressions (6)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Cloud%20Azure%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [VRA Regressions (5)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20VRA%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [Cyber Resilience Regressions](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [Apex Legends Regressions (3)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
- [Core Services Regressions](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Core%20Services%22%20AND%20affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))

### Per-Squad CF Breaches
- [GreenBoat CF Breach (13)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20filter%20%3D%2021637)
- [Apex Legends CF Breach (12)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20filter%20%3D%2021637)
- [Cyber Resilience CF Breach (4)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20filter%20%3D%2021637)

### Per-Squad FF Breaches
- [Cyber Resilience FF Breach (7)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Cyber%20Resilience%22%20AND%20filter%20%3D%2021636)
- [Apex Legends FF Breach (7)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20Apex%20Legends%22%20AND%20filter%20%3D%2021636)
- [GreenBoat FF Breach (4)](https://zerto.atlassian.net/issues/?jql=%22Owning%20Team%2FSquad%5BGroup%20Picker%20(single%20group)%5D%22%20%3D%20%22Squad%20GreenBoat%22%20AND%20filter%20%3D%2021636)

### All Regressions (all squads)
- [All 10.9 Regressions](https://zerto.atlassian.net/issues/?jql=affectedVersion%20%3D%2010.9%20AND%20%22Regression%3F%5BDropdown%5D%22%20%3D%20Yes%20AND%20status%20not%20in%20(Obsolete))
