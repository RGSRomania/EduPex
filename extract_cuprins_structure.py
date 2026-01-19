#!/usr/bin/env python3
"""
Extract actual curriculum structure from Manual.pdf files
Reading Cuprins (Table of Contents) to get:
- Chapter names (Unitatea 1, 2, 3...)
- Lesson names (L1, L2, L3...)
- Exact page numbers
"""

import pdfplumber
import json
import re
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "-q"])
    import pdfplumber

BASE_PATH = "/Users/mdica/PycharmProjects/EduPex/Planificari + Manual + Culegeri"

# Define all subjects and their paths
SUBJECTS = {
    "Clasa a V a": {
        "Matematica": "Matematica/Manual.pdf",
        "Limba și literatura română": "Limba și literatura română/Manual.pdf"
    },
    "Clasa a VI a": {
        "Matematica": "Matematica/Manual.pdf",
        "Limba si literatura romana": "Limba si literatura romana/Manual.pdf"
    },
    "Clasa a VII a": {
        "Matematica": "Matematica/Manual.pdf",
        "Limba si literatura romana": "Limba si literatura romana/Manual.pdf"
    },
    "Clasa a VIII a": {
        "Matematica": "Matematica/Manual.pdf",
        "Limba si literatura Romana": "Limba si literatura Romana/Manual.pdf"
    }
}

def extract_cuprins_from_pdf(pdf_path):
    """Extract table of contents from PDF"""
    try:
        if not Path(pdf_path).exists():
            print(f"❌ File not found: {pdf_path}")
            return None

        with pdfplumber.open(pdf_path) as pdf:
            all_text = ""
            # Look through first 20 pages for Cuprins
            for i, page in enumerate(pdf.pages[:20]):
                text = page.extract_text()
                if text:
                    all_text += text + "\n"
                # Stop if we find a lot of content (passed Cuprins)
                if i > 10 and len(all_text) > 5000:
                    break

            return all_text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def parse_structure(text):
    """Parse the extracted text to find Unitatea and Lectia entries"""
    lines = text.split('\n')

    chapters = []
    current_chapter = None

    for line in lines:
        line = line.strip()

        # Look for Unitatea (chapter)
        if line.startswith('U') and ('nitatea' in line or 'nitate' in line):
            if current_chapter:
                chapters.append(current_chapter)
            current_chapter = {
                'name': line,
                'lessons': []
            }

        # Look for L (lesson)
        elif current_chapter and line and line[0] == 'L' and ':' in line:
            # Extract lesson
            lesson_name = line
            if lesson_name not in current_chapter['lessons']:
                current_chapter['lessons'].append(lesson_name)

    if current_chapter:
        chapters.append(current_chapter)

    return chapters

def main():
    print("=" * 80)
    print("🔍 EXTRACTING ACTUAL CURRICULUM STRUCTURE FROM PDFs")
    print("=" * 80)
    print()

    all_structures = {}

    for clasa, subjects in SUBJECTS.items():
        print(f"\n{'='*80}")
        print(f"📚 {clasa}")
        print(f"{'='*80}")

        all_structures[clasa] = {}

        for subject, relative_path in subjects.items():
            pdf_path = Path(BASE_PATH) / clasa / relative_path

            print(f"\n📖 {subject}")
            print(f"   Path: {pdf_path}")

            # Extract text from PDF
            text = extract_cuprins_from_pdf(str(pdf_path))

            if text:
                print(f"   ✅ Extracted {len(text)} characters")

                # Save extracted text for manual inspection
                output_file = f"CUPRINS_{clasa}_{subject.replace(' ', '_')}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(text)
                print(f"   ✅ Saved to: {output_file}")

                # Show first 1000 chars (Cuprins section)
                print(f"\n   --- PREVIEW (first 1000 chars) ---")
                print(text[:1000])
                print("   --- END PREVIEW ---\n")

                all_structures[clasa][subject] = text
            else:
                print(f"   ❌ Failed to extract")

    print("\n" + "=" * 80)
    print("✅ EXTRACTION COMPLETE")
    print("=" * 80)
    print(f"\nExtracted text from all PDFs saved as CUPRINS_*.txt files")
    print("Please review these files to understand the exact structure")
    print("Then we can rebuild the JSON files with correct chapter organization")

if __name__ == "__main__":
    main()

