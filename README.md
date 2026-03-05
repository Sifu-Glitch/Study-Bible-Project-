# Obsidian Bible Study Notes

This project is developed using an isolated Docker sandbox environment utilizing Opencode.ai

Every thing you see here is a test created by Ai models.

NKJV Bible notes in Obsidian-compatible markdown format with Strong's concordances.

## Structure

```
Bible/NKJV/
├── 1-Peter/
│   ├── 1-Peter-Index.md          # Book index with overview
│   ├── 1-Peter-1-Chapter.md     # Chapter overview
│   └── 1-Peter-1-1.md           # Individual verse files
└── Jude/
    ├── Jude-Index.md
    ├── Jude-1-Chapter.md
    └── Jude-1-1.md through Jude-1-25.md
```

## File Formats

### Book Index (`*-Index.md`)
- Frontmatter with book metadata
- Author, date, theme, key verse
- Chapter summary table
- Verse index with links

### Chapter Overview (`*-Chapter.md`)
- Verse navigation links
- Full chapter text with verse numbers
- Section headings
- Navigation links

### Verse File (`*-Chapter-Verse.md`)
```markdown
---
book: Jude
chapter: 1
verse: 1
translation: NKJV
category: Bible/NKJV/Jude
tags: [jude, apostle, called, sanctified]
---

# Jude 1:1

Verse text here.

## Cross References

[[Romans 8:28]], [[1 Peter 1:2]]

## Strong's Numbers

[[G2455]] - Ἰούδας (Ioudas) - Judah, Jude
[[G1401]] - δοῦλος (doulos) - Bondservant
```

## Tools

### Flashcard Generator (`bible_flashcards.py`)

Generates flashcards from Bible notes for Anki or other flashcard apps.

**Usage:**
```bash
python3 bible_flashcards.py <path> [--anki] [--csv] [--json] [-o output]
```

**Arguments:**
- `path` - Path to Bible folder (default: `Bible/NKJV`)
- `--anki` - Export to Anki CSV format
- `--csv` - Export to readable CSV
- `--json` - Export to JSON
- `-o, --output` - Output filename (without extension)

**Output:** Creates flashcard files with:
- Verse recall cards
- Cross reference cards
- Strong's definition cards

**Example:**
```bash
python3 bible_flashcards.py Bible/NKJV --csv -o bible_cards
python3 bible_flashcards.py Bible/NKJV --anki -o anki_import
```

## Adding New Books

1. Create folder: `Bible/NKJV/<Book-Name>/`
2. Create `*-Index.md` - Book overview
3. Create `*-Chapter.md` - Chapter text
4. Create `*-Chapter-Verse.md` - Individual verses

See 1-Peter or Jude for example format.


