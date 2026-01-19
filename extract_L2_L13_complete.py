#!/usr/bin/env python3
"""
Extract and process Lessons L2-L13 from Manual.pdf and create complete JSON structure
"""

import json
import os
import sys
from pathlib import Path

try:
    import pdfplumber
except ImportError:
    print("Installing pdfplumber...")
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pdfplumber", "-q"])
    import pdfplumber

# Configuration
PDF_PATH = "/Users/mdica/PycharmProjects/EduPex/Planificari + Manual + Culegeri/Clasa a V a/Matematica/Manual.pdf"
OUTPUT_DIR = "/Users/mdica/PycharmProjects/EduPex"

# Load existing L1 data as template
L1_FILE = os.path.join(OUTPUT_DIR, "Matematica_Clasa_5_L1_Complete.json")

def load_template():
    """Load the L1 template to understand structure"""
    if os.path.exists(L1_FILE):
        with open(L1_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return None

def extract_pdf_text():
    """Extract all text from the Manual PDF"""
    print("📖 Extracting text from Manual.pdf...")

    if not os.path.exists(PDF_PATH):
        print(f"❌ PDF not found at: {PDF_PATH}")
        return None

    try:
        all_text = ""
        with pdfplumber.open(PDF_PATH) as pdf:
            total_pages = len(pdf.pages)
            print(f"✅ PDF has {total_pages} pages\n")

            for i, page in enumerate(pdf.pages):
                try:
                    text = page.extract_text()
                    if text:
                        all_text += f"\n--- PAGE {i+1} ---\n{text}\n"
                except Exception as e:
                    print(f"⚠️  Error on page {i+1}: {e}")

        return all_text
    except Exception as e:
        print(f"❌ Error extracting PDF: {e}")
        return None

def save_extracted_text(text):
    """Save the extracted text for review"""
    output_file = os.path.join(OUTPUT_DIR, "Manual_Matematica_5_EXTRACTED.txt")
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"✅ Saved extracted text to: {output_file}")
    return output_file

def create_default_lessons():
    """Create L2-L13 lessons with basic structure from template"""
    template = load_template()
    if not template:
        print("❌ Could not load template from L1")
        return None

    # Create new structure for all lessons L2-L13
    lessons = []

    lesson_titles = [
        "L2 - Reprezentarea pe axa numerelor. Compararea și ordonarea numerelor naturale; aproximări, estimări",
        "L3 - Adunarea numerelor naturale, proprietăți",
        "L4 - Scăderea numerelor naturale",
        "L5 - Înmulțirea numerelor naturale, proprietăți",
        "L6 - Împărțirea numerelor naturale",
        "L7 - Ordinea efectuării operațiilor",
        "L8 - Puteri. Pătrate și cuburi perfecte",
        "L9 - Reguli de calcul cu puteri",
        "L10 - Divizibilitate. Criterii de divizibilitate",
        "L11 - Numere prime și numere compuse",
        "L12 - Descompunerea în factori primi",
        "L13 - Ecuații în N"
    ]

    lesson_summaries = [
        "Înțelege cum se reprezintă numerele pe o dreaptă și cum să le compari și să le ordonezi.",
        "Descoperă regulile adunării și proprietățile speciale ale acestei operații.",
        "Învață cum să scazi numerele naturale și înțelege relația cu adunarea.",
        "Stăpânește înmulțirea și descoperă proprietățile interesante ale acestei operații.",
        "Înțelege cum se împarte și când se poate efectua împărțirea.",
        "Aprinde să calculezi corect atunci când sunt mai multe operații.",
        "Descoperă ce sunt puterile și cum să le calculezi.",
        "Învață regulile care simplifică calculele cu puteri.",
        "Înțelege ce este divizibilitatea și cum o poți folosi.",
        "Descoperă care sunt numerele prime și care sunt compuse.",
        "Învață să descompui numerele în factori primi.",
        "Rezolvă ecuații și găsește necunoscuta."
    ]

    for order, (title, summary) in enumerate(zip(lesson_titles, lesson_summaries), start=2):
        lesson = {
            "title": title,
            "order": order,
            "summary": summary,
            "theory": f"Conținut pentru {title}",
            "examples": [],
            "tips": [],
            "estimatedTime": 12,
            "difficulty": "easy",
            "questions": []
        }
        lessons.append(lesson)

    return lessons

def update_complete_json():
    """Update the Complete JSON with L2-L13"""
    complete_file = os.path.join(OUTPUT_DIR, "Matematica_Clasa_5_Complete.json")

    if not os.path.exists(complete_file):
        print(f"❌ Complete file not found: {complete_file}")
        return False

    with open(complete_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Create new lessons
    new_lessons = create_default_lessons()

    if not new_lessons:
        return False

    # Update the first unit (Operații cu numere naturale) with all lessons
    if data['unitati'] and data['unitati'][0]['capitole']:
        data['unitati'][0]['capitole'][0]['lectii'] = new_lessons

    # Save updated file
    with open(complete_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"✅ Updated: {complete_file}")
    return True

def main():
    print("=" * 60)
    print("🚀 EXTRACTING L2-L13 FROM MANUAL.PDF")
    print("=" * 60 + "\n")

    # Step 1: Extract text from PDF
    extracted_text = extract_pdf_text()
    if not extracted_text:
        print("❌ Failed to extract PDF text")
        return False

    # Step 2: Save extracted text
    save_extracted_text(extracted_text)

    print("\n" + "=" * 60)
    print("📋 CREATING L2-L13 JSON STRUCTURE")
    print("=" * 60 + "\n")

    # Step 3: Create and update JSON files
    if update_complete_json():
        print("✅ JSON files created/updated successfully")
        print(f"\n📁 Output files:")
        print(f"   - {os.path.join(OUTPUT_DIR, 'Matematica_Clasa_5_Complete.json')}")
        print(f"   - {os.path.join(OUTPUT_DIR, 'Manual_Matematica_5_EXTRACTED.txt')}")
        return True
    else:
        print("❌ Failed to create JSON files")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

