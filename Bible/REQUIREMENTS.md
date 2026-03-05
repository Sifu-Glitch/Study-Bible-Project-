# NKJV Study Bible for Obsidian - Requirements & Status

## Project Overview

**Goal:** Create a comprehensive verse-by-verse Study Bible in Obsidian using the NKJV translation with:
- Verse-level markdown notes
- Cross-references between verses
- Strong's Hebrew/Greek numbers with definitions
- Sidecar viewing capability

---

## Current Status

### Completed ✅

1. **Folder Structure Created:**
   ```
   /Bible/NKJV/1-Peter/           - Verse-level notes
   /Strongs/Hebrew/               - Placeholder for Hebrew Strong's
   /Strongs/Greek/                - Placeholder for Greek Strong's
   /scripts/                      - Generator scripts
   ```

2. **1 Peter Verse Notes Created:** 60+ verses across all 5 chapters
   - Each verse has frontmatter (book, chapter, verse, translation, category, tags)
   - Verse text from NKJV
   - Cross-references section (wikilinks format)
   - Strong's numbers section

3. **1 Peter Chapter Notes Created (for sidebar viewing):**
   - [[1-Peter-1-Chapter|1-Peter-1-Chapter.md]]
   - [[1-Peter-2-Chapter|1-Peter-2-Chapter.md]]
   - [[1-Peter-3-Chapter|1-Peter-3-Chapter.md]]
   - [[1-Peter-4-Chapter|1-Peter-4-Chapter.md]]
   - [[1-Peter-5-Chapter|1-Peter-5-Chapter.md]]

4. **1 Peter Index Note Created:**
   - Overview of the book
   - Chapter summaries
   - Links to all verses

5. **Documentation:**
   - `/Bible/README.md` - Project documentation
   - `/Bible/REQUIREMENTS.md` - Requirements and status

### In Progress 🔄

- 1 Peter Strong's numbers need verification (using Blue Letter Bible as source)
- Chapter notes now created - ready for sidebar viewing!

---

## Requirements

### Phase 1: Complete 1 Peter (Priority: High)

- [ ] Fix any remaining verse note errors
- [ ] Add accurate Strong's numbers for all verses (source: Blue Letter Bible interlinear)
- [ ] Add cross-references for all verses
- [ ] Create chapter-level notes for 1 Peter (full chapter text for sidebar viewing)

### Phase 2: Expand to Full Bible (Priority: Medium)

- [ ] Create verse notes for all 66 books (31,102 verses total)
- **Estimated time:** Several hours to weeks depending on automation

### Phase 3: Strong's Numbers (Priority: Medium)

- [ ] Create individual Strong's number notes (H0001-H8674, G0001-G5624)
- [ ] Link verse notes to Strong's notes
- **Resource:** https://github.com/gapmiss/kingdom-study-tools-for-obsidian

### Phase 4: Cross-References (Priority: Medium)

- [ ] Add comprehensive cross-references to all verses
- **Resource:** https://github.com/cevr/bible-cross-reference-wikilinks

### Phase 5: Obsidian Setup (Priority: High)

- [ ] Install recommended plugins:
  - Bible Reference - Quick verse lookup
  - Bible Sidecar - View translations in sidebar
  - Dataview - Query verses by tags
- [ ] Create chapter-level notes for sidebar viewing

---

## Options to Continue

### Option A: Continue Manually
Continue creating verse notes one by one using Blue Letter Bible as source.

**Pros:** Accurate Strong's, full control
**Cons:** Slow (31,102 verses = very time consuming)

### Option B: Use Existing Resources (Recommended)
Download and adapt pre-built datasets:
1. Get complete NKJV markdown from: https://github.com/gapmiss/kingdom-study-tools-for-obsidian
2. Get cross-references from: https://github.com/cevr/bible-cross-reference-wikilinks
3. Import and adapt to our verse-level format

**Pros:** Fast, complete data
**Cons:** May need format conversion

### Option C: Hybrid Approach
1. Download pre-built Bible text
2. Run our existing script to generate verse files with cross-references
3. Manually add Strong's numbers over time

**Pros:** Balanced speed and accuracy
**Cons:** Requires some technical setup

---

## Data Sources

| Resource | URL | Purpose |
|----------|-----|---------|
| Blue Letter Bible | blueletterbible.org | Strong's numbers, interlinear |
| Bible Cross-References | github.com/cevr/bible-cross-reference-wikilinks | 31,000+ verse connections |
| Kingdom Study Tools | github.com/gapmiss/kingdom-study-tools-for-obsidian | Complete Bible + Strong's |
| Obsidian Bible Reference | obsidian.md/plugins | Plugin for verse lookup |

---

## Technical Notes

### Verse File Format (Current)
```markdown
---
book: 1 Peter
chapter: 1
verse: 1
translation: NKJV
category: Bible/NKJV/1-Peter
tags: [peter, apostle, elect]
---

# 1 Peter 1:1

[Verse text here]

## Cross References

[[Romans 8:29]], [[Ephesians 1:4]]

## Strong's Numbers

- **G3972** - Πέτρος (Petros) - Peter, rock
- **G652** - ἀπόστολος (apostolos) - Apostle, messenger
```

### Naming Convention
- Folder: `1-Peter/` (Book name with hyphen)
- File: `1-Peter-1-1.md` (Book-Chapter-Verse.md)

### Strong's Number Format
- Hebrew: `H0001` - `H8674`
- Greek: `G0001` - `G5624`

---

## Next Steps (Priority Order)

1. ~~**HIGH:** Create chapter-level notes for 1 Peter (for sidebar viewing)~~ ✅ DONE
2. **HIGH:** Choose Option A, B, or C for continuing (see above)
3. **MEDIUM:** If using Option B/C, download and process existing datasets
4. **MEDIUM:** Add Strong's numbers to verse notes
5. **MEDIUM:** Add cross-references

---

## Contact / Continuation

To continue this project:
1. Read this requirements document
2. Choose continuation option (A, B, or C)
3. Install Obsidian and recommended plugins
4. Continue from where left off

---

*Last Updated: 2026-03-03*
*Current Progress: 105 verse notes + 5 chapter notes + 1 index note for 1 Peter*
*Total Bible: 31,102 verses - Current: 105 (~0.3%)*
