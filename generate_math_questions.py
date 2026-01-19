#!/usr/bin/env python3
"""
Generate Practice Questions for Matematica Clasa 5
Based on the lesson structure, this script generates realistic math questions
that can be used immediately while we work on extracting from the Manual PDF
"""

import json
from datetime import datetime

# Math questions generated from curriculum standards
math_questions = {
    "Capitol 1: Operații cu numere naturale": {
        "L1 - Scrierea și citirea numerelor naturale": [
            {
                "question": "Cum se citește numărul 5.247?",
                "options": [
                    {"text": "Cinci mii două sute patruzeci și șapte", "correct": True},
                    {"text": "Cincizeci și doi sute patruzeci și șapte", "correct": False},
                    {"text": "Cinci mii douăzeci și patru", "correct": False},
                    {"text": "Cinci mii o sută patruzeci și șapte", "correct": False}
                ],
                "explanation": "Cifrele se grupează în grupe de trei de la dreapta: 247 = două sute patruzeci și șapte, iar 5 = cinci mii."
            },
            {
                "question": "Scrie în cifre: nouă mii trei sute doi",
                "options": [
                    {"text": "9.302", "correct": True},
                    {"text": "9.320", "correct": False},
                    {"text": "9.032", "correct": False},
                    {"text": "9.223", "correct": False}
                ],
                "explanation": "9 mii = 9000, 3 sute = 300, 0 zeci = 0, 2 unități = 2. Total: 9.302"
            },
            {
                "question": "Care este cifra zecilor în numărul 7.485?",
                "options": [
                    {"text": "8", "correct": True},
                    {"text": "4", "correct": False},
                    {"text": "5", "correct": False},
                    {"text": "7", "correct": False}
                ],
                "explanation": "În numărul 7.485: 7 = mii, 4 = sute, 8 = zeci, 5 = unități"
            },
            {
                "question": "Care număr este mai mic: 3.214 sau 3.241?",
                "options": [
                    {"text": "3.214", "correct": True},
                    {"text": "3.241", "correct": False},
                    {"text": "Sunt egale", "correct": False},
                    {"text": "Nu se poate determina", "correct": False}
                ],
                "explanation": "Comparând: 3.2__ și 3.2__, apoi 1 < 4 la poziția zecilor, deci 3.214 < 3.241"
            }
        ],
        "L2 - Reprezentarea pe axa numerelor. Compararea și ordonarea": [
            {
                "question": "Pe axa numerelor, care număr este mai aproape de 0: 5 sau 12?",
                "options": [
                    {"text": "5", "correct": True},
                    {"text": "12", "correct": False},
                    {"text": "Sunt la fel de aproape", "correct": False},
                    {"text": "Nu se poate determina", "correct": False}
                ],
                "explanation": "Pe axa numerelor, 5 este mai apropiere de 0 decât 12."
            },
            {
                "question": "Ordonează crescător: 25, 15, 35, 5",
                "options": [
                    {"text": "5, 15, 25, 35", "correct": True},
                    {"text": "35, 25, 15, 5", "correct": False},
                    {"text": "5, 25, 15, 35", "correct": False},
                    {"text": "15, 5, 25, 35", "correct": False}
                ],
                "explanation": "Ordonare crescătoare = de la mic la mare: 5 < 15 < 25 < 35"
            },
            {
                "question": "Care este aproximarea numărului 48 la zeci?",
                "options": [
                    {"text": "50", "correct": True},
                    {"text": "40", "correct": False},
                    {"text": "45", "correct": False},
                    {"text": "48", "correct": False}
                ],
                "explanation": "48 este mai apropiere de 50 decât de 40 (48 > 45), deci se rotunjește la 50"
            }
        ],
        "L3 - Adunarea numerelor naturale, proprietăți": [
            {
                "question": "5 + 7 = ?",
                "options": [
                    {"text": "12", "correct": True},
                    {"text": "2", "correct": False},
                    {"text": "35", "correct": False},
                    {"text": "11", "correct": False}
                ],
                "explanation": "5 + 7 = 12"
            },
            {
                "question": "Care este suma 234 + 156?",
                "options": [
                    {"text": "390", "correct": True},
                    {"text": "378", "correct": False},
                    {"text": "380", "correct": False},
                    {"text": "400", "correct": False}
                ],
                "explanation": "234 + 156: 4+6=10 (0 și 1), 30+50=80, 200+100=300. Total: 300+80+10=390"
            },
            {
                "question": "3 + 5 = 5 + 3. Cum se numește această proprietate?",
                "options": [
                    {"text": "Comutativitate", "correct": True},
                    {"text": "Asociativitate", "correct": False},
                    {"text": "Distributivitate", "correct": False},
                    {"text": "Neutralitate", "correct": False}
                ],
                "explanation": "Proprietatea comutativă: a + b = b + a (ordinea nu contează la adunare)"
            }
        ],
        "L4 - Scăderea numerelor naturale": [
            {
                "question": "12 - 5 = ?",
                "options": [
                    {"text": "7", "correct": True},
                    {"text": "17", "correct": False},
                    {"text": "2", "correct": False},
                    {"text": "8", "correct": False}
                ],
                "explanation": "12 - 5 = 7. Verificare: 7 + 5 = 12 ✓"
            },
            {
                "question": "350 - 127 = ?",
                "options": [
                    {"text": "223", "correct": True},
                    {"text": "477", "correct": False},
                    {"text": "233", "correct": False},
                    {"text": "237", "correct": False}
                ],
                "explanation": "350 - 127: 10-7=3 (cu împrumut), 40-20=20 (după împrumut), 300-100=200. Total: 223"
            },
            {
                "question": "Dacă a - b = 15 și a = 42, cât este b?",
                "options": [
                    {"text": "27", "correct": True},
                    {"text": "57", "correct": False},
                    {"text": "15", "correct": False},
                    {"text": "42", "correct": False}
                ],
                "explanation": "Dacă 42 - b = 15, atunci b = 42 - 15 = 27. Verificare: 42 - 27 = 15 ✓"
            }
        ],
        "L5 - Înmulțirea numerelor naturale, proprietăți": [
            {
                "question": "6 × 7 = ?",
                "options": [
                    {"text": "42", "correct": True},
                    {"text": "13", "correct": False},
                    {"text": "67", "correct": False},
                    {"text": "48", "correct": False}
                ],
                "explanation": "6 × 7 = 42"
            },
            {
                "question": "12 × 8 = ?",
                "options": [
                    {"text": "96", "correct": True},
                    {"text": "20", "correct": False},
                    {"text": "108", "correct": False},
                    {"text": "84", "correct": False}
                ],
                "explanation": "12 × 8 = 96 (10 × 8 = 80 și 2 × 8 = 16, total 96)"
            },
            {
                "question": "4 × 0 = ?",
                "options": [
                    {"text": "0", "correct": True},
                    {"text": "4", "correct": False},
                    {"text": "1", "correct": False},
                    {"text": "40", "correct": False}
                ],
                "explanation": "Orice număr înmulțit cu 0 = 0"
            }
        ]
    }
}

# Add more questions for other capitole...
capitol_2_questions = {
    "Capitol 2: Metode aritmetice": {
        "L1 - Metoda reducerii la unitate": [
            {
                "question": "Dacă 4 kg de orez costă 20 lei, cât costă 7 kg?",
                "options": [
                    {"text": "35 lei", "correct": True},
                    {"text": "28 lei", "correct": False},
                    {"text": "40 lei", "correct": False},
                    {"text": "70 lei", "correct": False}
                ],
                "explanation": "1 kg costă: 20 ÷ 4 = 5 lei. 7 kg costă: 7 × 5 = 35 lei"
            },
            {
                "question": "3 caiete costă 12 lei. Cât costă 5 caiete?",
                "options": [
                    {"text": "20 lei", "correct": True},
                    {"text": "15 lei", "correct": False},
                    {"text": "36 lei", "correct": False},
                    {"text": "60 lei", "correct": False}
                ],
                "explanation": "1 caiet costă: 12 ÷ 3 = 4 lei. 5 caiete: 5 × 4 = 20 lei"
            }
        ]
    }
}

# Generate output
output = {
    "generated_date": datetime.now().isoformat(),
    "description": "Generated Math Questions for Matematica Clasa 5",
    "total_questions": 0,
    "questions_by_capitol": math_questions
}

# Count questions
for capitol, lessons in math_questions.items():
    for lesson, questions in lessons.items():
        output["total_questions"] += len(questions)

print(json.dumps(output, ensure_ascii=False, indent=2))

# Save to file
with open("Generated_Math_Questions.json", "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\n✅ Generated {output['total_questions']} questions")
print("📁 Saved to: Generated_Math_Questions.json")

