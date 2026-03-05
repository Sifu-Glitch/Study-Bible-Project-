#!/usr/bin/env python3
"""
Obsidian Bible Flashcard Generator
Generates Anki-compatible flashcards from Obsidian Bible notes
"""

import os
import re
import csv
from pathlib import Path
from dataclasses import dataclass
from typing import Optional
import argparse


@dataclass
class VerseData:
    book: str
    chapter: int
    verse: int
    text: str
    cross_references: list[str]
    strongs: list[tuple[str, str, str]]
    tags: list[str]


def parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter"""
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return {}
    
    fm = {}
    for line in match.group(1).split('\n'):
        if ':' in line:
            key, value = line.split(':', 1)
            fm[key.strip()] = value.strip()
    return fm


def parse_strongs(content: str) -> list[tuple[str, str, str]]:
    """Extract Strong's numbers from verse file"""
    strongs = []
    pattern = r'\[\[([GH]\d+)\]\]\s*-\s*([^\(]+)\s*\(([^)]+)\)\s*-\s*(.+)'
    
    for match in re.finditer(pattern, content):
        strongs.append((match.group(1), match.group(2).strip(), match.group(4)))
    
    return strongs


def parse_cross_references(content: str) -> list[str]:
    """Extract cross references"""
    pattern = r'\[\[([^\]]+)\]\]'
    matches = re.findall(pattern, content)
    return [m for m in matches if not m.startswith('G') and not m.startswith('H')]


def parse_verse_file(filepath: Path) -> Optional[VerseData]:
    """Parse a single verse file"""
    content = filepath.read_text()
    
    fm = parse_frontmatter(content)
    if not fm:
        return None
    
    try:
        chapter = int(fm.get('chapter', 0))
        verse = int(fm.get('verse', 0))
    except ValueError:
        return None
    
    text_match = re.search(r'^#\s+\w+\s+\d+:\d+\n\n(.+?)(?=##|\Z)', content, re.DOTALL)
    text = text_match.group(1).strip() if text_match else ""
    
    tags_str = fm.get('tags', '')
    tags = [t.strip() for t in tags_str.strip('[]').split(',')] if tags_str else []
    
    return VerseData(
        book=fm.get('book', ''),
        chapter=chapter,
        verse=verse,
        text=text,
        cross_references=parse_cross_references(content),
        strongs=parse_strongs(content),
        tags=tags
    )


def generate_cards(verse: VerseData) -> list[dict]:
    """Generate flashcards from verse data"""
    cards = []
    
    reference = f"{verse.book} {verse.chapter}:{verse.verse}"
    
    card = {
        'front': f"{reference}",
        'back': verse.text,
        'tags': f"bible nkjv {verse.book.lower().replace(' ', '-')}"
    }
    cards.append(card)
    
    if verse.cross_references:
        card_ref = {
            'front': f"What are the cross references for {reference}?",
            'back': '<br>'.join(verse.cross_references),
            'tags': f"bible crossref {verse.book.lower().replace(' ', '-')}"
        }
        cards.append(card_ref)
    
    for strong_num, greek, definition in verse.strongs:
        card_strong = {
            'front': f"What does {strong_num} ({greek}) mean in {reference}?",
            'back': definition,
            'tags': f"bible strongs {verse.book.lower().replace(' ', '-')}"
        }
        cards.append(card_strong)
    
    return cards


def process_bible_folder(bible_path: Path) -> list[dict]:
    """Process all verse files in Bible folder"""
    all_cards = []
    
    for book_folder in bible_path.iterdir():
        if not book_folder.is_dir():
            continue
        
        print(f"Processing {book_folder.name}...")
        
        for verse_file in book_folder.glob("*.md"):
            if 'Chapter' in verse_file.name or 'Index' in verse_file.name:
                continue
            
            verse = parse_verse_file(verse_file)
            if verse:
                cards = generate_cards(verse)
                all_cards.extend(cards)
    
    return all_cards


def export_to_anki(cards: list[dict], output_file: Path):
    """Export cards to Anki CSV format"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['front', 'back', 'tags'])
        writer.writeheader()
        writer.writerows(cards)
    
    print(f"\nExported {len(cards)} cards to {output_file}")
    print("To import into Anki: File -> Import -> Select the CSV file")


def export_to_csv(cards: list[dict], output_file: Path):
    """Export cards to readable CSV"""
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Question', 'Answer', 'Tags'])
        for card in cards:
            writer.writerow([card['front'], card['back'], card['tags']])
    
    print(f"Exported {len(cards)} cards to {output_file}")


def export_to_json(cards: list[dict], output_file: Path):
    """Export cards to JSON for programmatic use"""
    import json
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(cards, f, indent=2, ensure_ascii=False)
    
    print(f"Exported {len(cards)} cards to {output_file}")


def main():
    parser = argparse.ArgumentParser(description='Generate flashcards from Obsidian Bible notes')
    parser.add_argument('path', nargs='?', default='Bible/NKJV', help='Path to Bible folder')
    parser.add_argument('--anki', action='store_true', help='Export to Anki CSV format')
    parser.add_argument('--csv', action='store_true', help='Export to readable CSV')
    parser.add_argument('--json', action='store_true', help='Export to JSON')
    parser.add_argument('-o', '--output', default='flashcards', help='Output filename (without extension)')
    
    args = parser.parse_args()
    
    bible_path = Path(args.path)
    if not bible_path.exists():
        print(f"Error: {args.path} does not exist")
        return
    
    print(f"Processing Bible notes from {bible_path}...")
    cards = process_bible_folder(bible_path)
    
    if not cards:
        print("No cards generated. Check the path and file format.")
        return
    
    output_path = Path(args.output)
    
    if args.anki:
        export_to_anki(cards, output_path.with_suffix('.anki.csv'))
    elif args.json:
        export_to_json(cards, output_path.with_suffix('.json'))
    else:
        export_to_csv(cards, output_path.with_suffix('.csv'))


if __name__ == '__main__':
    main()
