#!/usr/bin/env python3
"""
BUILD ALL 8 CORRECT JSON STRUCTURES
Creates skeleton with correct unit structure for all grades and subjects
Ready to be populated with actual content from PDFs
"""

import json
from pathlib import Path

OUTPUT_PATH = "/Users/mdica/PycharmProjects/EduPex"

# Define all curriculum structures based on actual Cuprins data
CURRICULUM_STRUCTURES = {
    "Matematica_Clasa_V": {
        "materie": "Matematica",
        "clasa": "V",
        "unitati": [
            ("UNITATEA 1 - Operații cu numere naturale", 13),
            ("UNITATEA 2 - Metode aritmetice de rezolvare a problemelor", 5),
            ("UNITATEA 3 - Divizibilitatea numerelor naturale", 3),
            ("UNITATEA 4 - Fracții ordinare", 10),
            ("UNITATEA 5 - Fracții zecimale", 9),
            ("UNITATEA 6 - Elemente de geometrie și unități de măsură", 11),
        ]
    },
    "Matematica_Clasa_VI": {
        "materie": "Matematica",
        "clasa": "VI",
        "unitati": [
            ("UNITATEA 1 - Mulțimi. Numere naturale", 10),
            ("UNITATEA 2 - Fracții ordinare", 11),
            ("UNITATEA 3 - Fracții zecimale", 8),
            ("UNITATEA 4 - Rapoarte și proporții", 6),
            ("UNITATEA 5 - Numere întregi", 8),
            ("UNITATEA 6 - Elemente de geometrie. Figuri geometrice", 12),
        ]
    },
    "Matematica_Clasa_VII": {
        "materie": "Matematica",
        "clasa": "VII",
        "unitati": [
            ("UNITATEA 1 - Numere raționale", 12),
            ("UNITATEA 2 - Calcul algebric", 10),
            ("UNITATEA 3 - Ecuații și inecuații", 8),
            ("UNITATEA 4 - Sisteme de ecuații", 6),
            ("UNITATEA 5 - Elemente de geometrie", 11),
            ("UNITATEA 6 - Figuri geometrice", 10),
        ]
    },
    "Matematica_Clasa_VIII": {
        "materie": "Matematica",
        "clasa": "VIII",
        "unitati": [
            ("UNITATEA 1 - Numere reale", 10),
            ("UNITATEA 2 - Calcul algebric", 10),
            ("UNITATEA 3 - Funcții", 9),
            ("UNITATEA 4 - Ecuații, inecuații, sisteme", 12),
            ("UNITATEA 5 - Elemente de geometrie în spațiu", 8),
            ("UNITATEA 6 - Arii și volume", 10),
        ]
    },
    "LimbaRomana_Clasa_V": {
        "materie": "Limba și literatura română",
        "clasa": "V",
        "unitati": [
            ("UNITATEA 1 - Comunicare și limbaj", 12),
            ("UNITATEA 2 - Ortografie și punctuație", 8),
            ("UNITATEA 3 - Morfologie", 10),
            ("UNITATEA 4 - Sintaxă", 10),
            ("UNITATEA 5 - Text și discurs", 9),
            ("UNITATEA 6 - Literatura", 8),
        ]
    },
    "LimbaRomana_Clasa_VI": {
        "materie": "Limba și literatura română",
        "clasa": "VI",
        "unitati": [
            ("UNITATEA 1 - Comunicare și exprimare", 11),
            ("UNITATEA 2 - Ortografie și punctuație avansată", 9),
            ("UNITATEA 3 - Morfologie avansată", 11),
            ("UNITATEA 4 - Sintaxă complexă", 10),
            ("UNITATEA 5 - Textul și genurile textuale", 10),
            ("UNITATEA 6 - Literatura și analiza textului", 9),
        ]
    },
    "LimbaRomana_Clasa_VII": {
        "materie": "Limba și literatura română",
        "clasa": "VII",
        "unitati": [
            ("UNITATEA 1 - Limba și comunicare", 10),
            ("UNITATEA 2 - Ortografie și punctuație", 8),
            ("UNITATEA 3 - Morfologia cuvintelor variabile", 10),
            ("UNITATEA 4 - Sintaxă și propoziția", 11),
            ("UNITATEA 5 - Textul și discursul", 10),
            ("UNITATEA 6 - Literatura și analiza literară", 11),
        ]
    },
    "LimbaRomana_Clasa_VIII": {
        "materie": "Limba și literatura română",
        "clasa": "VIII",
        "unitati": [
            ("UNITATEA 1 - Limba și comunicare", 11),
            ("UNITATEA 2 - Ortografie și punctuație avansate", 9),
            ("UNITATEA 3 - Morfologie și semantică", 10),
            ("UNITATEA 4 - Sintaxă avansată și analiza textului", 12),
            ("UNITATEA 5 - Genuri textuale și retorica", 10),
            ("UNITATEA 6 - Literatura universală și națională", 12),
        ]
    }
}

def create_lesson_object(title, order):
    """Create a lesson object with all required fields"""
    return {
        "title": f"L{order} - {title}",
        "order": order,
        "summary": title[:100] if len(title) > 100 else title,
        "theory": "",  # To be populated
        "examples": [],
        "tips": [],
        "estimatedTime": 45,
        "difficulty": "easy" if order <= 5 else ("medium" if order <= 10 else "hard"),
        "question": {
            "text": f"Întrebare despre {title.split('-')[0]}?",
            "options": [
                {"text": "Opțiunea A", "correct": False, "explanation": ""},
                {"text": "Opțiunea B", "correct": False, "explanation": ""},
                {"text": "Opțiunea C", "correct": True, "explanation": ""},
                {"text": "Opțiunea D", "correct": False, "explanation": ""}
            ]
        }
    }

def build_curriculum(file_key, spec):
    """Build a complete curriculum file"""
    data = {
        "materie": spec["materie"],
        "clasa": spec["clasa"],
        "level": {"V": 5, "VI": 6, "VII": 7, "VIII": 8}[spec["clasa"]],
        "unitati": []
    }

    for unit_order, (unit_name, lesson_count) in enumerate(spec["unitati"], start=1):
        # Create lessons for this unit
        lectii = []
        for lesson_order in range(1, lesson_count + 1):
            # Use generic title - will be populated with actual content
            title = f"Lecția {lesson_order}"
            lectii.append(create_lesson_object(title, lesson_order))

        # Create unit
        unit = {
            "name": unit_name,
            "order": unit_order,
            "descriere": unit_name.split(" - ")[1] if " - " in unit_name else unit_name,
            "capitole": [{
                "name": unit_name.split(" - ")[1] if " - " in unit_name else unit_name,
                "order": 1,
                "lectii": lectii
            }]
        }

        data["unitati"].append(unit)

    return data

def main():
    print("="*80)
    print("🔨 BUILDING ALL 8 CORRECT JSON STRUCTURES")
    print("="*80 + "\n")

    summary = []

    for file_key, spec in CURRICULUM_STRUCTURES.items():
        print(f"📚 Building {file_key}...")

        # Build the curriculum
        data = build_curriculum(file_key, spec)

        # Save to file
        filename = f"{file_key}_CORRECT.json"
        output_file = Path(OUTPUT_PATH) / filename

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        # Count lessons
        total_lessons = sum(len(u['capitole'][0]['lectii']) for u in data['unitati'])

        print(f"   ✅ {filename}")
        print(f"      Units: {len(data['unitati'])}, Total lessons: {total_lessons}")

        summary.append({
            'file': filename,
            'subject': spec['materie'],
            'grade': spec['clasa'],
            'units': len(data['unitati']),
            'lessons': total_lessons
        })

    print("\n" + "="*80)
    print("✅ ALL 8 FILES BUILT WITH CORRECT STRUCTURE")
    print("="*80 + "\n")

    print("📊 SUMMARY:\n")
    print(f"{'File':<45} {'Units':<8} {'Lessons':<10}")
    print("-" * 63)

    total_all_lessons = 0
    for item in summary:
        print(f"{item['file']:<45} {item['units']:<8} {item['lessons']:<10}")
        total_all_lessons += item['lessons']

    print("-" * 63)
    print(f"{'TOTAL':<45} {'':<8} {total_all_lessons:<10}\n")

    print("✅ All structures are ready for population with actual content from PDFs!")

if __name__ == "__main__":
    main()

