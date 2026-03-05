# Bible Study Notes - Project Context

## Current State

- Bible notes in markdown format at `Bible/NKJV/`
- Currently includes: 1-Peter (5 chapters), Jude (1 chapter, 25 verses)
- All verse files include cross references and Strong's concordances

## Completed Work

### Bible Notes Created
- **1-Peter**: 5 chapters, 105 verses with cross references and Strong's
- **Jude**: 1 chapter, 25 verses with cross references and Strong's

### Tools Created
- `bible_flashcards.py` - Flashcard generator for Bible notes
  - Generates verse recall cards
  - Generates cross reference cards  
  - Generates Strong's definition cards
  - Supports CSV, Anki CSV, and JSON export formats

### Generated Outputs
- `bible_cards.csv` - 756 flashcards generated from all Bible notes

## Available Tools

- `bible_flashcards.py` - Generate flashcards from Bible notes

## Commands to Run

### Flashcard Generation
```bash
python3 /home/opencodeuser/project/bible_flashcards.py /home/opencodeuser/project/Bible/NKJV --csv -o /home/opencodeuser/project/bible_cards
```

## Next Steps Suggestions

1. Add more Bible books following the existing format
2. Run lint/typecheck if available
3. Expand flashcard generator features (word frequency, theme analysis)

## Files Created

- `/home/opencodeuser/project/bible_flashcards.py` - Flashcard generator
- `/home/opencodeuser/project/bible_cards.csv` - Generated flashcards (756 cards)
- `/home/opencodeuser/project/README.md` - Project documentation
