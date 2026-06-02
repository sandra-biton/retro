# Release 10.9 Retrospective — RCA & Action Items
## Scope: Dana, Shlomi, Rajeev squads only
### Timeline: Sprint 0 (Sep 30) → FF (Jan 26) → CF (Feb 17) → GA (May 13)

---

## 📊 KPI Comparison: 10.8 → 10.9 (Our Squads Only)

| Metric | KPI | 10.8 | 10.9 | Δ | Trend |
|--------|-----|------|------|---|-------|
| **Breached FF** (open stories) | 0 | 37 | 27 | -10 | ✅ Improved (-27%) |
| **Breached CF** (open stories) | 0 | 23 | 32 | +9 | ❌ Worse (+39%) |
| **Breached CF** (open bugs) | 0 | 4 | 5 | +1 | ➡️ Flat |
| **Regression total** | <10 | 50 | 95 | +45 | ❌ Worse (+90%) |
| **Regression in hardening** | <4 | 17 | 40 | +23 | ❌ Worse (+135%) |
| **Regression by automation** | +20% rate | 32% | 12.6% | -19.4pp | ❌ Dropped significantly |

---

## Per-GM Breakdown

### Dana Mittelman

| Metric | 10.8 | 10.9 | Δ |
|--------|------|------|---|
| Breached FF | 7 | 4 | ✅ -3 |
| Breached CF Stories | 6 | 0 | ✅ -6 |
| Breached CF Bugs | 2 | 1 | ✅ -1 |
| Regression total | 19 | 54 | ❌ +35 |
| Regression hardening | 11 | 24 | ❌ +13 |

**FF/CF: Significantly improved.** CF breaches went to zero stories.
**Regressions: Massively worse.** 19 → 54 (+184%), driven entirely by Squad Nils (React Migration).

### Shlomi Apel

| Metric | 10.8 | 10.9 | Δ |
|--------|------|------|---|
| Breached FF | 0 | 10 | ❌ +10 |
| Breached CF Stories | 3 | 6 | ❌ +3 |
| Breached CF Bugs | 2 | 2 | ➡️ Same |
| Regression total | 4 | 14 | ❌ +10 |
| Regression hardening | 1 | 10 | ❌ +9 |

**All metrics worse.** New issues: Driver squad (8 regressions from 1), Cyber Resilience FF breaches (7), and VRA scale regressions.

### Rajeev Srivastav

| Metric | 10.8 | 10.9 | Δ |
|--------|------|------|---|
| Breached FF | 30 | 13 | ✅ -17 |
| Breached CF Stories | 14 | 26 | ❌ +12 |
| Breached CF Bugs | 0 | 2 | ❌ +2 |
| Regression total | 27 | 27 | ➡️ Same |
| Regression hardening | 5 | 6 | ➡️ Same |

**FF improved significantly** (30→13). Regressions stable. **CF breach doubled** — driven by GreenBoat (13) and Apex Legends (12) carrying stories into hardening.

---

## 🔍 RCA per Metric (with 10.8 Retro Cross-Reference)

### 1. Breached FF — Stories open after Feature Freeze

| Squad | Count | Root Cause |
|-------|-------|-----------|
| Cyber Resilience (Shlomi) | 7 | Late requirements (LTS Support, Integration Hub received end of Sprint 3). Design approved end Sprint 4 — known FF miss, RIH filed |
| Apex Legends (Rajeev) | 7 | Secret Centralization stories moved to "Ready for Testing" before FF, but QA bandwidth limited → acceptance after FF |
| GreenBoat (Rajeev) | 4 | Dependencies on GB dev completion (Linux migration) + waiver to work during FF |
| Driver (Shlomi) | 2 | All FF-breaching stories also breached CF (duplicated) |
| Nils (Dana) | 2 | FE tweaks enabled late (same issue as 10.8) |
| Cloud Azure (Dana) | 2 | AWS stories "ready for testing prior FF" but not accepted |

**Was this addressed from 10.8?**
- 10.8 retro said: "Avoid enabling tweaks after FF" → ❌ Repeated (Dana/Nils)
- 10.8 retro said: "ZIC timeline different from ZVM" → ⏳ Under discussion (Shlomi)
- **New in 10.9:** Late requirement injection (Shlomi) — not a recurring issue

---

### 2. Breached CF — Stories still open at Code Freeze

| Squad | Count | Root Cause |
|-------|-------|-----------|
| GreenBoat (Rajeev) | 13 | Public Cloud testing setup not ready for FF and still being stabilized. GB had waiver for FF work, pushed CF |
| Apex Legends (Rajeev) | 12 | Testing started late so stories remained in testing phase past CF |
| Cyber Resilience (Shlomi) | 4 | LTS stories (3/6 of CF breach) — known late start. Also: "Do we need to treat Testplan creation in this metric?" |
| Driver (Shlomi) | 2 | Urgent HF pushed due to customer case (LTR). HV stabilization prolonged |

**Was this addressed from 10.8?**
- 10.8 retro said: "Enhance ZIC quality by improving design, requirements, test planning" → ❌ CF breach worse
- 10.8 retro said: "Scale and performance setups lacking" → ❌ Not fixed. Same finding by Shlomi in 10.9
- **New in 10.9:** HV testing setup + signing server availability (Shlomi's finding)

---

### 3. Regression Total — 50 → 95 (+90%)

| Squad | 10.8 | 10.9 | Δ | RCA |
|-------|------|------|---|-----|
| **Nils** (Dana) | 16 | 47 | +31 | React Migration — all bugs in new implementation are classified as regressions. Missing PO requirements. Tweaks activated at end of release |
| **GreenBoat** (Rajeev) | 15 | 17 | +2 | Upgrade scenarios (10.8→10.9 migration), External Vault Secrets, EF Cache. GB/Linux migration code conflict with AWS |
| **Driver** (Shlomi) | 1 | 8 | +7 | VME/VAIO bugs — driver loading failures, FOT IO errors, VRA sync issues. "Bugs caused by low quality dev testing" (Shlomi's finding) |
| **Azure** (Dana) | 3 | 6 | +3 | GPv2 performance issues, recovery operations stuck — related to new GPv2 feature |
| **VRA** (Shlomi) | 3 | 5 | +2 | Scale issues — VRA sync slow at scale, public cloud VRA version mismatch |
| **Apex Legends** (Rajeev) | 6 | 3 | -3 | ✅ Improved — fewer regressions |
| **DR Cloud Enablement** (Idan Shama) | 3 | 3 | 0 | Stable (not in scope) |

**Was this addressed from 10.8?**
- 10.8 said: "React — perform more side-by-side comparisons with AngularJS" → ❌ NOT DONE. Nils went 16→47
- 10.8 said: "Increase Cypress coverage" → ❌ Automation rate dropped 32%→12.6%
- 10.8 said: "Clarify ownership for cross-team changes (GB/Linux migration)" → ❌ Same conflict repeated
- 10.8 said: "Testing started late so regression came late" (Rajeev) → Rajeev's regressions stayed FLAT (good), but Shlomi's Driver increased due to same cause

---

### 4. Regression During Hardening — 17 → 40 (+135%)

| Squad | Count | RCA |
|-------|-------|-----|
| **Nils** (Dana) | 20 | React tweaks turned ON during hardening → instant regressions in production code. 9/15 are React |
| **Driver** (Shlomi) | 6 | VME/VAIO - bugs found late because testing started late |
| **VRA** (Shlomi) | 3 | Scale bugs only visible on large setups |
| **Azure** (Dana) | 3 | Linux migration tool must be developed after ZVM RC exists → inherently late |
| **GreenBoat** (Rajeev) | 2 | Upgrade path bugs |

**Was this addressed from 10.8?**
- 10.8 said: "Avoid enabling FE tweaks at end of release" → ❌ NOT DONE. 20/24 Dana hardening regressions are Nils/React + tweaks
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
