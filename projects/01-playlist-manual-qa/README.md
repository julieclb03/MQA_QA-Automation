
# 🎧 Playlist Manual QA System

**Goal:** validate a playlist manager (create, add/remove tracks, shuffle/repeat, edge cases).  
**Focus:** test design quality, coverage, and defect hygiene.

## Structure
- `test-cases/` – atomic test cases with steps, data, expected results
- `checklists/` – smoke/regression checklist
- `bug-reports/bugs.md` – Jira-style markdown bugs (title, repro steps, AR/ER, env, severity)
- `evidence/` – screenshots + session notes

## How to run manual tests & show results
1. Open each file in `test-cases/` and execute steps manually.
2. Update the **Result** block at the bottom to `PASS` or `FAIL` and add short notes.
3. Mark `checklists/regression-checklist.md` ✅/❌.
4. Save failure screenshots in `evidence/screenshots/` and reference them in the test case / bug.

