
# TC-004 Edge Cases
**Data:** extremely long titles, emoji/unicode, duplicate adds.

**Steps:**
1) Attempt to add a duplicate track twice.
2) Add a track with very long title.
3) Add a track with emoji/unicode characters.

**Expected:** 
- Duplicate add is blocked or de-duplicated.
- Long/emoji titles render without layout break.

**Result:** (PASS/FAIL)  
**Notes:**
