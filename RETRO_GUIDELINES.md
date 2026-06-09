# Retrospective Guidelines

## Process

- **Review the 10.9 Dashboard**: Open the release statistics dashboard and review key metrics → [Release retrospective - 10.9](https://zerto.atlassian.net/jira/dashboards/15285)
- **Analyze Your Domain**: Each feature lead or GM reviews data from their area.
- **Suggest Improvement**: For every missed KPI, suggest 1–2 **practical actions** that can improve the next release.
- **Track and Follow Up**: Add all actions to a shared tracker (JIRA / Excel)
  - Review progress during the next release planning
  - Validate if KPIs improved in the following release
- **Directors must review and approve the retrospective.**
- **Directors must update the PMO on all approvals; otherwise, we will cancel the meeting.**

---

## Standards for Evidence and Analysis

- **Metric-driven**: KPI trend, not just the point-in-time value. Compare vs. last release.
- **Root cause clarity**: Identify process, capacity, dependency, or quality-system drivers behind the metric.
- **Action quality**: Actions must be specific, testable, time-bound, and assigned to a single accountable owner.

Use: **"If we do X, then we expect KPI Y to move from A to B by next release"** to ensure actions are hypothesis-driven.

---

## Template: Action Item Format

| Field | Description |
|-------|-------------|
| **Focus Area** | Which KPI / metric area |
| **Owner** | Single accountable GM |
| **Issue** | Link to Jira data showing the problem |
| **KPI(s)** | Target value |
| **Analysis Insights** | Root cause bullets |
| **Proposed Actions (1–2)** | Specific, testable actions with Owner, ETA, Expected Impact |

---

## Examples

### Example 1: Breached Feature Freeze

| Field | Value |
|-------|-------|
| **Focus Area** | Breached Feature Freeze (FF) items |
| **Owner** | Dana |
| **Issue** | [22 stories](https://zerto.atlassian.net/jira/dashboards/15285?maximized=31217) breached FF |
| **KPI** | 0 |
| **Analysis** | Most FE US (6/26) are related to enabling tweaks for features that were already developed, but tweaks were activated only at the end of the development phase. |
| **Actions** | 1. Activate tweaks at least 2 sprints before FF<br>2. Increase unit testing from 50% to 70% |
| **ETA** | Sprint 8 |
| **Expected Impact** | Zero issues for FF |

### Example 2: Regression Bugs

| Field | Value |
|-------|-------|
| **Focus Area** | Regression bugs |
| **Owner** | Rajeev |
| **Issue** | [13 regression bugs](https://zerto.atlassian.net/jira/dashboards/15285?maximized=31213) |
| **KPI** | Less than 8 |
| **Analysis** | [9 bugs](https://zerto.atlassian.net/issues?jql=(filter%20%3D%2012120%20AND%20fixVersion%20%3D%2010.8%20AND%20created%20%3E%3D%202025-03-18%20AND%20created%20%3C%202025-10-28%20AND%20(affectedVersion%20%3D%2010.8%20or%20fixVersion%20%3D%2010.8))%20AND%20(key%20in%20(ZER-163418%2CZER-163951%2CZER-163954%2CZER-164582%2CZER-165881%2CZER-166703%2CZER-167691%2CZER-168243%2CZER-168265%2CZER-171175%2CZER-171820%2CZER-180564%2CZER-183681))%20and%20component%20%3D%20%22SETTINGS%20service%22) found in the **settings service** — lack of unit tests & automation |
| **Actions** | Add 6 automated tests to cover the bugs |
| **ETA** | Sprint 6 |
| **Expected Impact** | Less than 8 regression issues total, max 2 in "settings service" |

### Example 3: Release Status Meeting

| Field | Value |
|-------|-------|
| **Focus Area** | Release status meeting |
| **Owner** | Asaf |
| **Issue** | Meeting consumes excessive time, some GMs arrive unprepared |
| **KPI** | Less than 1.5 hour meeting |
| **Analysis** | 1. Structured fields not updated<br>2. GMs unprepared<br>3. Reviewing all epics (160–250) instead of yellow/red<br>4. Many epics "planned maybe" |
| **Actions** | Split into: Meeting #1 (Director Scrum of Scrums) + Meeting #2 (Portfolio release status). [Decision doc](https://zerto.atlassian.net/wiki/spaces/PM/pages/2418573339/Release+Status+Meeting+Format+Decision+Single+Meeting+vs.+Split+by+Release#Option-C) |
| **ETA** | Sprint 5 |
| **Expected Impact** | Meeting under 1.5 hours, GMs prepared, less than 2 "planned maybe" per GM |

---

## 10.9 KPI Dashboard

[https://zerto.atlassian.net/jira/dashboards/15285](https://zerto.atlassian.net/jira/dashboards/15285)

## Timeline

| Milestone | Date |
|-----------|------|
| Sprint 0 | Sep 29, 2025 |
| Feature Freeze | Jan 26, 2026 |
| Code Freeze | Feb 17, 2026 |
| GA | May 13, 2026 |

Sprints are prefixed `10.9` (e.g., "10.9 Sprint 1", "10.9 Sprint 2", etc.)
