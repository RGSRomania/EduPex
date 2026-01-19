#!/usr/bin/env python3
"""
Extract exact table of contents (Cuprins) from all Manual.pdf files
For all grades and subjects
"""

import pdfplumber
import re
from pathlib import Path

BASE_PATH = "/Users/mdica/PycharmProjects/EduPex/Planificari + Manual + Culegeri"

SUBJECTS = {
    "Clasa a V a": {
        "Matematica": ("Matematica", "Manual.pdf"),
        "Limba și literatura română": ("Limba și literatura română", "Manual.pdf")
    },
    "Clasa a VI a": {
        "Matematica": ("Matematica", "Manual.pdf"),
        "Limba si literatura romana": ("Limba si literatura romana", "Manual.pdf")
    },
    "Clasa a VII a": {
        "Matematica": ("Matematica", "Manual.pdf"),
        "Limba si literatura romana": ("Limba si literatura romana", "Manual.pdf")
    },
    "Clasa a VIII a": {
        "Matematica": ("Matematica", "Manual.pdf"),
        "Limba si literatura Romana": ("Limba si literatura Romana", "Manual.pdf")
    }
}

def extract_cuprins(pdf_path):
    """Extract Cuprins (table of contents) from PDF"""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            cuprins_text = ""
            # Usually Cuprins is in first 10 pages
            for i, page in enumerate(pdf.pages[:15]):
                text = page.extract_text()
                if text:
                    cuprins_text += text + "\n"
            return cuprins_text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return None

def parse_units_and_lessons(text):
    """Parse the Cuprins to extract UNITĂȚI and LECȚII"""
    lines = text.split('\n')

    units = []
    current_unit = None

    for line in lines:
        line = line.strip()

        # Look for UNITATEA pattern
        if 'UNITATEA' in line.upper() or 'UNITATE' in line.upper():
            if current_unit:
                units.append(current_unit)
            current_unit = {
                'name': line,
                'lessons': []
            }

        # Look for Lecția/Lectie pattern
        elif current_unit and ('Lecț' in line or 'Lecti' in line or line.startswith('L')):
            if 'L' in line and ':' in line:
                current_unit['lessons'].append(line)

    if current_unit:
        units.append(current_unit)

    return units

def main():
    print("="*80)
    print("🔍 EXTRACTING TABLE OF CONTENTS FROM ALL PDFS")
    print("="*80 + "\n")

    all_structures = {}

    for clasa, subjects in SUBJECTS.items():
        print(f"\n📚 {clasa}")
        print("-" * 80)

        all_structures[clasa] = {}

        for subject_name, (dir_name, pdf_file) in subjects.items():
            pdf_path = Path(BASE_PATH) / clasa / dir_name / pdf_file

            print(f"\n  📖 {subject_name}")
            print(f"     Path: {pdf_path}")

            if not pdf_path.exists():
                print(f"     ❌ FILE NOT FOUND")
                continue

            # Extract Cuprins
            cuprins_text = extract_cuprins(str(pdf_path))

            if cuprins_text:
                print(f"     ✅ Extracted {len(cuprins_text)} characters")

                # Save full Cuprins for reference
                safe_subject = subject_name.replace(' ', '_').replace('ă', 'a').replace('ș', 's').replace('ț', 't').replace('î', 'i')
                safe_clasa = clasa.replace(' ', '_')
                cuprins_file = f"CUPRINS_{safe_clasa}_{safe_subject}.txt"
                with open(cuprins_file, 'w', encoding='utf-8') as f:
                    f.write(cuprins_text)

                # Parse structure
                units = parse_units_and_lessons(cuprins_text)
                all_structures[clasa][subject_name] = {
                    'units': units,
                    'total_units': len(units),
                    'total_lessons': sum(len(u['lessons']) for u in units)
                }

                print(f"     ✅ Found {len(units)} units")
                for unit in units[:3]:  # Show first 3
                    lesson_count = len(unit['lessons'])
                    print(f"        • {unit['name'][:60]} → {lesson_count} lessons")
                if len(units) > 3:
                    print(f"        ... and {len(units) - 3} more units")
            else:
                print(f"     ❌ Failed to extract")

    # Summary
    print("\n" + "="*80)
    print("📊 SUMMARY")
    print("="*80)

    for clasa, subjects in all_structures.items():
        print(f"\n{clasa}:")
        for subject, data in subjects.items():
            if data and 'total_units' in data:
                print(f"  {subject}: {data['total_units']} units, {data['total_lessons']} total lessons")

if __name__ == "__main__":
    main()

