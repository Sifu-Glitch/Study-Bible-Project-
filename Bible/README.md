# NKJV Study Bible for Obsidian

This is a comprehensive Bible study system for Obsidian with verse-level notes, cross-references, and Strong's numbers.

## Current Structure

```
/
├── Bible/
│   └── NKJV/
│       └── 1-Peter/
│           ├── 1-Peter-1-1.md
│           ├── 1-Peter-1-2.md
│           └── ... (32 verse files created so far)
├── Strongs/
│   ├── Hebrew/
│   │   └── (H0001-H8674)
│   └── Greek/
│       └── (G0001-G5624)
├── CrossRefs/
│   └── (cross-reference data)
└── scripts/
    ├── generate_bible.py
    └── setup_bible_study.py
```

## What's Been Created

### 1. Verse-Level Notes (32 created for 1 Peter)
- Each verse is its own markdown file
- Format: `Book-Chapter-Verse.md` (e.g., `1-Peter-1-1.md`)
- Includes:
  - Frontmatter with book, chapter, verse, translation, category, tags
  - Verse text
  - Cross-references section
  - Strong's numbers section

### 2. Folder Structure
- `/Bible/NKJV/` - Main Bible text location
- `/Strongs/Hebrew/` - Hebrew Strong's numbers (H0001-H8674)
- `/Strongs/Greek/` - Greek Strong's numbers (G0001-G5624)
- `/CrossRefs/` - Cross-reference data

### 3. Scripts
- `setup_bible_study.py` - Creates folder structure
- `generate_bible.py` - Generates verse files

## How to Continue

### Option 1: Complete 1 Peter Manually
Continue creating the remaining 73 verses for 1 Peter (chapters 2-5).

### Option 2: Use Existing Resources
- Download pre-built Bible markdown files from GitHub
- Adapt existing cross-reference datasets
- Import Strong's numbers from existing datasets

### Recommended Resources
1. **Bible Text**: 
   - https://github.com/gapmiss/kingdom-study-tools-for-obsidian
   - https://github.com/JackNathan05/Obsidian-Bible-KJV

2. **Cross-References**:
   - https://github.com/cevr/bible-cross-reference-wikilinks
   - https://github.com/josephilipraja/bible-cross-reference-json

3. **Strong's Numbers**:
   - https://github.com/openscriptures/strongs
   - https://github.com/gapmiss/kingdom-study-tools-for-obsidian

## Plugins to Install in Obsidian

1. **Bible Reference** - Quick verse lookup
2. **Bible Sidecar** - View translations in sidebar
3. **Dataview** - Query verses by tags
4. **Scripture Indexer** - Auto-detect references

## Example Verse File

```markdown
---
book: 1 Peter
chapter: 1
verse: 1
translation: NKJV
category: Bible/NKJV/1-Peter
tags: [peter, apostle, elect, dispersion]
---

# 1 Peter 1:1

Peter, an apostle of Jesus Christ, To the pilgrims of the Dispersion in Pontus, Galatia, Cappadocia, Asia, and Bithynia,

## Cross References

[[Romans 8:29]], [[Ephesians 1:4]], [[James 1:1]]

## Strong's Numbers

[[G3972]] - Πέτρος (Petros) - Peter, rock
[[G652]] - ἀπόστολος (apostolos) - Apostle, messenger
```

## Next Steps

1. Continue adding more books (Gospels: Matthew, Mark, Luke, John)
2. Add cross-references to each verse
3. Create Strong's number files
4. Import into Obsidian vault
