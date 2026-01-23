#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Units 3-6 lessons from Clasa a V a Matematica
"""

import json

# Unit 3: Divizibilitatea (3 lessons)
unit3_math_data = {
    "unit_number": "3",
    "unit_name": "Divizibilitatea",
    "lessons": [
        {
            "number": "1",
            "name": "Divizibilitatea numerelor naturale",
            "summary": """Divizibilitatea este relația dintre două numere naturale unde unul se divide exact de altul. Un număr a se divide cu 
            numărul b dacă există un număr c așa încât a = b × c. Se spune că a este divizibil cu b, sau b divide a, notat b|a. De exemplu, 12 
            se divide cu 3 deoarece 12 = 3 × 4. Proprietăți importante: orice număr se divide cu 1 și cu el însuși; 0 se divide cu orice număr; 
            dacă a se divide cu b și b se divide cu c, atunci a se divide cu c (tranzitivitate); dacă a se divide cu b și a se divide cu c, 
            atunci a se divide cu (b + c). Divisibilitatea este fundamentală pentru teoria numerelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce înseamnă că a se divide cu b?",
                    "options": [
                        "A. a este mai mic decât b",
                        "B. Există c așa încât a = b × c",
                        "C. a este mai mare decât b",
                        "D. a și b sunt egale"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Se divide 24 cu 6?",
                    "options": [
                        "A. Nu, pentru că 24 nu este mai mic decât 6",
                        "B. Da, pentru că 24 = 6 × 4",
                        "C. Nu, pentru că nu sunt egale",
                        "D. Nu se poate determina"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Cu ce se divide orice număr natural?",
                    "options": [
                        "A. Doar cu el însuși",
                        "B. Cu 1 și cu el însuși",
                        "C. Doar cu 0",
                        "D. Cu toate numerele"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "2",
            "name": "Criterii de divizibilitate",
            "summary": """Criteriile de divizibilitate sunt reguli care permit determinarea rapidă dacă un număr se divide cu altul, fără a efectua 
            împărțirea. Criterii importante: 1) Divisibilitate cu 2: ultimul digit este par (0, 2, 4, 6, 8). 2) Divisibilitate cu 3: suma cifrelor 
            este divizibilă cu 3. 3) Divisibilitate cu 5: ultimul digit este 0 sau 5. 4) Divisibilitate cu 10: ultimul digit este 0. 5) Divisibilitate 
            cu 4: ultimele două cifre formează un număr divizibil cu 4. 6) Divisibilitate cu 9: suma cifrelor este divizibilă cu 9. Aceste criterii 
            economisesc timp și sunt esențiale în teoria numerelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se determină dacă un număr se divide cu 2?",
                    "options": [
                        "A. Prin efectuarea împărțirii",
                        "B. Dacă ultimul digit este par",
                        "C. Dacă suma cifrelor este pară",
                        "D. Dacă are 2 cifre"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Se divide 315 cu 3?",
                    "options": [
                        "A. Nu",
                        "B. Da, deoarece 3 + 1 + 5 = 9, care se divide cu 3",
                        "C. Doar dacă se divide și cu 5",
                        "D. Nu se poate determina"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care este criteriul de divizibilitate cu 5?",
                    "options": [
                        "A. Suma cifrelor trebuie să fie 5",
                        "B. Ultimul digit trebuie să fie 0 sau 5",
                        "C. Numărul trebuie să fie mai mare decât 5",
                        "D. Trebuie să împărțim la 5"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "3",
            "name": "Numere prime. Numere compuse",
            "summary": """Numerele prime sunt numerele naturale mai mari decât 1 care au exact doi divizori: 1 și el însuși. De exemplu, 2, 3, 5, 7, 
            11, 13 sunt prime. Numerele compuse sunt numerele naturale mai mari decât 1 care au mai mult de doi divizori. De exemplu, 4, 6, 8, 9, 10 
            sunt compuse. Numărul 1 nu este nici prim, nici compus, prin definiție. Două numere sunt coprime (relativ prime) dacă cmmdc-ul lor este 
            1. Importanța numerelor prime: orice număr compus poate fi descompus unic în produs de numere prime (teorema fundamentală a aritmeticii). 
            Numerele prime sunt ''blocuri de construcție'' ale tuturor numerelor naturale.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este un număr prim?",
                    "options": [
                        "A. Un număr care se divide cu orice număr",
                        "B. Un număr care are exact doi divizori: 1 și el însuși",
                        "C. Un număr care este par",
                        "D. Un număr care este mai mic decât 10"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Este 7 un număr prim?",
                    "options": [
                        "A. Nu, pentru că este impar",
                        "B. Da, deoarece are doar divizorii 1 și 7",
                        "C. Nu, pentru că este mai mic decât 10",
                        "D. Nu se poate determina"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care dintre următoarele este număr compus?",
                    "options": [
                        "A. 2",
                        "B. 3",
                        "C. 5",
                        "D. 6"
                    ],
                    "correctAnswerIndex": 3
                }
            ]
        }
    ]
}

# Unit 4: Fracții ordinare (10 lessons)
unit4_math_data = {
    "unit_number": "4",
    "unit_name": "Fracții ordinare",
    "lessons": [
        {"number": "1", "name": "Fracții ordinare. Fracții echivalente. Procente", "summary": "Fracția ordinară este o parte din întreg, reprezentată ca a/b, unde a este numărătorul și b este numitorul. Fracțiile echivalente sunt fracții care reprezintă aceeași valoare, de exemplu 1/2 = 2/4 = 3/6. Pentru a obține fracții echivalente, înmulțim sau împărțim atât numărătorul cât și numitorul cu același număr. Procentul este o fracție cu numitorul 100, de exemplu 25% = 25/100 = 1/4. Fracțiile sunt utilizate frecvent pentru a exprima părți din întreg și rapoarte.", "questions": [{"questionNumber": 1, "questionText": "Ce este o fracție ordinară?", "options": ["A. Un număr întreg", "B. O parte din întreg, reprezentată ca a/b", "C. Un procent", "D. O putere"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Care fracție este echivalentă cu 1/2?", "options": ["A. 2/3", "B. 3/5", "C. 2/4", "D. 1/3"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Ce este un procent?", "options": ["A. O fracție cu numitorul 10", "B. O fracție cu numitorul 100", "C. Un număr mai mare decât 1", "D. Un număr negativ"], "correctAnswerIndex": 1}]},
        {"number": "2", "name": "Compararea fracțiilor cu același numitor/numărător. Reprezentarea fracțiilor ordinare pe axa numerelor", "summary": "Pentru a compara fracții cu același numitor, se compară numărătorii: fracția cu numărător mai mare este mai mare. De exemplu, 3/5 > 2/5. Pentru a compara fracții cu același numărător, se compară numitorii: fracția cu numitor mai mic este mai mare. De exemplu, 3/4 > 3/5. Reprezentarea pe axa numerelor ajută la vizualizarea ordinii fracțiilor. Pe axa numerelor, 0 este la stânga, iar 1 este la dreapta. Fracții între 0 și 1 sunt fracții proprii.", "questions": [{"questionNumber": 1, "questionText": "Compară 2/7 și 5/7", "options": ["A. 2/7 > 5/7", "B. 2/7 = 5/7", "C. 2/7 < 5/7", "D. Nu se pot compara"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Compară 3/4 și 3/8", "options": ["A. 3/4 < 3/8", "B. 3/4 = 3/8", "C. 3/4 > 3/8", "D. Nu se pot compara"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Unde se află 1/2 pe axa numerelor?", "options": ["A. La 0", "B. La 1", "C. La jumătatea dintre 0 și 1", "D. La dreapta lui 1"], "correctAnswerIndex": 2}]},
        {"number": "3", "name": "Introducerea și scoaterea întregilor dintr-o fracție", "summary": "O fracție improprie (numărător > numitor) poate fi transformată într-un număr mixt: o parte întreagă și o fracție proprie. De exemplu, 7/3 = 2 1/3 (2 întregi și 1/3). Pentru a introduce întregi: 7 ÷ 3 = 2 rest 1, deci 7/3 = 2 1/3. Pentru a scoate întregi: 2 1/3 = (2×3 + 1)/3 = 7/3. Numerele mixte sunt utile pentru reprezentarea cantităților care depășesc un întreg.", "questions": [{"questionNumber": 1, "questionText": "Transformă 11/4 într-un număr mixt", "options": ["A. 2 1/4", "B. 2 3/4", "C. 3 1/4", "D. 1 3/4"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Transformă 3 1/2 într-o fracție improprie", "options": ["A. 5/2", "B. 7/2", "C. 6/2", "D. 4/2"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Care este relația dintre numerele mixte și fracțiile improprii?", "options": ["A. Nu sunt legate", "B. Sunt identice", "C. Exprimă aceeași valoare în forme diferite", "D. Numerele mixte sunt mai mari"], "correctAnswerIndex": 2}]},
        {"number": "4", "name": "Cel mai mare divizor comun a două numere naturale. Amplificarea și simplificarea fracțiilor. Fracții ireductibile", "summary": "Cel mai mare divizor comun (cmmdc) a două numere este cel mai mare număr care le divide pe amândouă. De exemplu, cmmdc(12, 18) = 6. Amplificarea fracției înseamnă a înmulți atât numărătorul cât și numitorul cu același număr. Simplificarea fracției înseamnă a împărți atât numărătorul cât și numitorul cu același număr. O fracție ireductibilă este o fracție care nu mai poate fi simplificată, adică cmmdc-ul numărătorului și numitorului este 1. De exemplu, 3/5 este ireductibilă.", "questions": [{"questionNumber": 1, "questionText": "Care este cmmdc-ul numerelor 12 și 8?", "options": ["A. 2", "B. 4", "C. 6", "D. 12"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Simplifică 12/18", "options": ["A. 2/3", "B. 6/9", "C. 4/6", "D. 1/2"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Ce este o fracție ireductibilă?", "options": ["A. O fracție care poate fi simplificată", "B. O fracție care nu mai poate fi simplificată", "C. O fracție cu numitor 1", "D. O fracție mai mare decât 1"], "correctAnswerIndex": 1}]},
        {"number": "5", "name": "Cel mai mic multiplu comun a două numere naturale. Aducerea fracțiilor la un numitor comun", "summary": "Cel mai mic multiplu comun (cmmmc) a două numere este cel mai mic număr care se divide cu ambele. De exemplu, cmmmc(4, 6) = 12. Aducerea fracțiilor la un numitor comun înseamnă a găsi un numitor comun pentru două fracții, de obicei cmmmc-ul numitorilor. De exemplu, 1/4 și 1/6: cmmmc(4, 6) = 12, deci 1/4 = 3/12 și 1/6 = 2/12. Aceasta este necesară pentru a aduna sau scădea fracții cu numitori diferiți.", "questions": [{"questionNumber": 1, "questionText": "Care este cmmmc-ul numerelor 4 și 6?", "options": ["A. 2", "B. 12", "C. 24", "D. 4"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Aducă la numitor comun 1/3 și 1/4", "options": ["A. 3/12 și 4/12", "B. 4/12 și 3/12", "C. 1/12 și 1/12", "D. 3/7 și 4/7"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "De ce avem nevoie să aducem fracții la numitor comun?", "options": ["A. Pentru a face calculele mai dificile", "B. Pentru a putea aduna sau scădea fracții", "C. Pentru a înmulți fracții", "D. Nu este necesar"], "correctAnswerIndex": 1}]},
        {"number": "6", "name": "Adunarea și scăderea fracțiilor", "summary": "Pentru a aduna sau scădea fracții cu același numitor, se adună sau se scad numărătorii și se păstrează numitorul. De exemplu, 2/5 + 1/5 = 3/5. Pentru fracții cu numitori diferiți, se aduc mai întâi la numitor comun, apoi se efectuează operația. De exemplu, 1/4 + 1/6: cmmmc(4, 6) = 12, deci 3/12 + 2/12 = 5/12. Rezultatul trebuie să fie o fracție ireductibilă.", "questions": [{"questionNumber": 1, "questionText": "Calculează 2/5 + 1/5", "options": ["A. 2/10", "B. 3/5", "C. 3/10", "D. 1/5"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Calculează 1/4 + 1/2", "options": ["A. 1/6", "B. 2/6", "C. 3/4", "D. 1/8"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Calculează 3/4 - 1/4", "options": ["A. 2/4 = 1/2", "B. 2/8", "C. 4/4", "D. 3/8"], "correctAnswerIndex": 0}]},
        {"number": "7", "name": "Înmulțirea fracțiilor", "summary": "Pentru a înmulți două fracții, se înmulțesc numărătorii între ei și numitorii între ei: (a/b) × (c/d) = (a×c)/(b×d). De exemplu, (2/3) × (3/4) = 6/12 = 1/2. Simplificarea se poate face înainte de înmulțire (simplificare ''pe diagonală''). De exemplu, (2/3) × (3/4) = (2×3)/(3×4) = 2/4 = 1/2. Înmulțirea fracțiilor este mai simplă decât adunarea pentru că nu necesită numitor comun.", "questions": [{"questionNumber": 1, "questionText": "Calculează (1/2) × (2/3)", "options": ["A. 2/6 = 1/3", "B. 3/5", "C. 2/5", "D. 1/6"], "correctAnswerIndex": 0}, {"questionNumber": 2, "questionText": "Calculează (2/5) × (5/4)", "options": ["A. 10/20 = 1/2", "B. 7/9", "C. 10/9", "D. 2/4"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Care este regula pentru înmulțirea fracțiilor?", "options": ["A. Se adună numărătorii și numitorii", "B. Se înmulțesc numărătorii și numitorii", "C. Se scad numărătorii", "D. Se împart numitorii"], "correctAnswerIndex": 1}]},
        {"number": "8", "name": "Împărțirea fracțiilor ordinare", "summary": "Pentru a împărți două fracții, se înmulțește prima fracție cu inversa (reciproca) celei de-a doua: (a/b) ÷ (c/d) = (a/b) × (d/c) = (a×d)/(b×c). De exemplu, (2/3) ÷ (1/4) = (2/3) × (4/1) = 8/3. Inversa unei fracții a/b este b/a. De exemplu, inversa lui 2/3 este 3/2. Împărțirea fracțiilor se reduce la înmulțire după înlocuirea cu inversa.", "questions": [{"questionNumber": 1, "questionText": "Calculează (1/2) ÷ (1/4)", "options": ["A. 1/8", "B. 1/6", "C. 2", "D. 1/4"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Care este inversa fracției 3/5?", "options": ["A. 5/3", "B. 3/5", "C. -3/5", "D. 1/3"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Cum se calculează (a/b) ÷ (c/d)?", "options": ["A. (a/b) × (c/d)", "B. (a/b) × (d/c)", "C. (a+b) ÷ (c+d)", "D. (a-b) × (c-d)"], "correctAnswerIndex": 1}]},
        {"number": "9", "name": "Puterea cu exponent natural a unei fracții ordinare", "summary": "Puterea unei fracții cu exponent natural n se calculează prin înmulțirea fracției cu ea însăși de n ori: (a/b)^n = (a^n)/(b^n). De exemplu, (2/3)^2 = (2^2)/(3^2) = 4/9. Pentru (a/b)^0 = 1 (pentru orice a/b ≠ 0), și (a/b)^1 = a/b. Regulile pentru exponenți la numere naturale se aplică și la fracții.", "questions": [{"questionNumber": 1, "questionText": "Calculează (1/2)^2", "options": ["A. 1/2", "B. 1/4", "C. 1/8", "D. 2/4"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Calculează (2/3)^3", "options": ["A. 6/9", "B. 8/27", "C. 6/27", "D. 2/3"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Care este valoarea (3/4)^0?", "options": ["A. 0", "B. 1", "C. 3/4", "D. 4/3"], "correctAnswerIndex": 1}]},
        {"number": "10", "name": "Fracții/procente dintr-un număr natural sau dintr-o fracție ordinară", "summary": "A afla o fracție dintr-un număr înseamnă a înmulți fracția cu acel număr: (a/b) × n. De exemplu, 1/2 din 10 = (1/2) × 10 = 5. A afla o fracție dintr-o fracție înseamnă a înmulți fracțiile: (a/b) × (c/d). De exemplu, 1/2 din 3/4 = (1/2) × (3/4) = 3/8. Procente funcționează similar: p% din n = (p/100) × n. De exemplu, 25% din 100 = (25/100) × 100 = 25. Aceste abilități sunt esențiale pentru probleme practice.", "questions": [{"questionNumber": 1, "questionText": "Calculează 1/3 din 12", "options": ["A. 3", "B. 4", "C. 5", "D. 6"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Calculează 50% din 200", "options": ["A. 50", "B. 100", "C. 150", "D. 200"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Calculează 1/4 din 2/3", "options": ["A. 2/12 = 1/6", "B. 3/4", "C. 1/2", "D. 2/7"], "correctAnswerIndex": 0}]}
    ]
}

# Unit 5: Fracții zecimale (9 lessons)
unit5_math_data = {
    "unit_number": "5",
    "unit_name": "Fracții zecimale",
    "lessons": [
        {"number": "1", "name": "Fracții zecimale; scrierea fracțiilor ordinare...", "summary": "Fracțiile zecimale sunt fracții cu numitorul o putere a lui 10 (10, 100, 1000, etc.). Se scriu folosind virgulă: 0,5 = 5/10, 0,25 = 25/100. Fiecare poziție după virgulă reprezentează o putere negativă a lui 10: prima poziție = zecimi (1/10), a doua = sutimi (1/100), a treia = miimi (1/1000). De exemplu, 3,25 = 3 + 2/10 + 5/100. Conversia fracțiilor ordinare în zecimale se face prin împărțire.", "questions": [{"questionNumber": 1, "questionText": "Ce este o fracție zecimală?", "options": ["A. O fracție cu numitorul 10", "B. O fracție cu numitorul o putere a lui 10", "C. O fracție cu numitor orice", "D. O fracție negativa"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Transformă 3/4 în fracție zecimală", "options": ["A. 0,25", "B. 0,5", "C. 0,75", "D. 1,25"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Ce reprezintă cifra din a doua poziție după virgulă?", "options": ["A. Zecimi", "B. Sutimi", "C. Miimi", "D. Zeci"], "correctAnswerIndex": 1}]},
        {"number": "2", "name": "Aproximări; compararea, ordonarea și reprezentarea pe axa numerelor...", "summary": "Aproximarea unei fracții zecimale se face rotunjind la o anumită poziție: rotunjire la zecimi (o poziție), la sutimi (două poziții), etc. De exemplu, 3,257 rotunjit la sutimi este 3,26. Compararea se face din stânga: mai întâi se compară părțile întregi, apoi zecimile, sutimile, etc. De exemplu, 3,2 < 3,25 < 3,3. Reprezentarea pe axa numerelor ajută la vizualizare.", "questions": [{"questionNumber": 1, "questionText": "Rotunjește 2,34 la zecimi", "options": ["A. 2,3", "B. 2,4", "C. 2,34", "D. 2,0"], "correctAnswerIndex": 0}, {"questionNumber": 2, "questionText": "Compară 2,5 și 2,50", "options": ["A. 2,5 > 2,50", "B. 2,5 < 2,50", "C. 2,5 = 2,50", "D. Nu se pot compara"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Compară 1,234 și 1,324", "options": ["A. 1,234 > 1,324", "B. 1,234 = 1,324", "C. 1,234 < 1,324", "D. Nu se pot compara"], "correctAnswerIndex": 2}]},
        {"number": "3", "name": "Adunarea și scăderea fracțiilor zecimale cu un număr finit de zecimale nenule", "summary": "Adunarea și scăderea fracțiilor zecimale se face alinând punctul zecimal: numerele se aliniază vertical, iar operația se efectuează normal. De exemplu, 2,5 + 1,23 = 3,73. Se poate gândi și ca adunare de fracții: 2,5 = 2 5/10, 1,23 = 1 23/100, deci 2,5 + 1,23 = 2,50 + 1,23 = 3,73. Scăderea se face similar.", "questions": [{"questionNumber": 1, "questionText": "Calculează 2,5 + 1,3", "options": ["A. 3,2", "B. 3,8", "C. 3,7", "D. 4,1"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Calculează 5,6 - 2,1", "options": ["A. 3,3", "B. 3,4", "C. 3,5", "D. 7,7"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Calculează 3,25 + 1,75", "options": ["A. 4,50 = 4,5", "B. 5,0", "C. 5,00 = 5", "D. 4,100"], "correctAnswerIndex": 2}]},
        {"number": "4", "name": "Înmulțirea fracțiilor zecimale cu un număr finit de zecimale nenule", "summary": "Înmulțirea fracțiilor zecimale se face ca înmulțire de numere întregi, apoi se plasează virgulă la poziția corespunzătoare. Regula: numărul de zecimale din rezultat = suma numărului de zecimale din factori. De exemplu, 2,5 × 1,3: se calculează 25 × 13 = 325, și din moment ce avem 1 + 1 = 2 zecimale, rezultatul este 3,25.", "questions": [{"questionNumber": 1, "questionText": "Calculează 2,5 × 2", "options": ["A. 4,5", "B. 5", "C. 5,5", "D. 4"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Calculează 0,5 × 0,2", "options": ["A. 0,10 = 0,1", "B. 0,25", "C. 1,0", "D. 0,02"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Câte zecimale are rezultatul lui 1,5 × 2,25?", "options": ["A. 1 zecimală", "B. 2 zecimale", "C. 3 zecimale", "D. 4 zecimale"], "correctAnswerIndex": 2}]},
        {"number": "5", "name": "Împărțirea a două numere naturale cu rezultat fracție zecimală...", "summary": "Când se împarte un număr natural la altul și rezultatul nu este întreg, se obține o fracție zecimală. De exemplu, 5 ÷ 2 = 2,5. Pentru a calcula, se continuă împărțirea după virgulă: 5 ÷ 2 = 2 rest 1, 10 ÷ 2 = 5, deci 5 ÷ 2 = 2,5. Media aritmetică a numerelor se calculează ca suma lor împărțită la cantitate: (a + b) ÷ 2 = media.", "questions": [{"questionNumber": 1, "questionText": "Calculează 7 ÷ 2", "options": ["A. 3", "B. 3,25", "C. 3,5", "D. 4"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Calculează media aritmetică a numerelor 10 și 20", "options": ["A. 15", "B. 20", "C. 25", "D. 10"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Calculează 9 ÷ 4", "options": ["A. 2,2", "B. 2,25", "C. 2,5", "D. 3"], "correctAnswerIndex": 1}]},
        {"number": "6", "name": "Împărțirea unei fracții zecimale cu un număr finit de zecimale nenule...", "summary": "Împărțirea fracțiilor zecimale se poate face prin transformarea împărțitorului în număr întreg (deplasând virgula și multiplicând ambele numere cu puteri ale lui 10), apoi efectuând împărțirea. De exemplu, 6,25 ÷ 2,5 = 62,5 ÷ 25 = 2,5. Regula: se deplasează virgula în ambele numere cu același număr de poziții, astfel încât împărțitorul să devină întreg.", "questions": [{"questionNumber": 1, "questionText": "Calculează 10 ÷ 2,5", "options": ["A. 2", "B. 3", "C. 4", "D. 5"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Calculează 0,8 ÷ 0,4", "options": ["A. 1", "B. 2", "C. 0,5", "D. 4"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Calculează 6 ÷ 0,5", "options": ["A. 3", "B. 6", "C. 12", "D. 0,5"], "correctAnswerIndex": 2}]},
        {"number": "7", "name": "Număr rațional pozitiv; ordinea efectuării operațiilor cu numere raționale pozitive", "summary": "Numărul rațional pozitiv este orice număr care poate fi exprimat ca o fracție p/q unde p și q sunt numere naturale și q ≠ 0. Aceasta include fracții ordinare, fracții zecimale și numere întregi. Ordinea operațiilor cu numere raționale este aceeași ca și cu numere naturale: 1) Paranteze, 2) Exponenți, 3) Înmulțire și Împărțire, 4) Adunare și Scădere.", "questions": [{"questionNumber": 1, "questionText": "Care dintre următoarele este un număr rațional?", "options": ["A. √2", "B. π", "C. 3/4", "D. ∞"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Calculează 2 + 3 × 0,5", "options": ["A. 2,5", "B. 3,5", "C. 1,5", "D. 4"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Calculează (1 + 0,5) × 2", "options": ["A. 2", "B. 2,5", "C. 3", "D. 3,5"], "correctAnswerIndex": 2}]},
        {"number": "8", "name": "Metode aritmetice pentru rezolvarea problemelor cu fracții...", "summary": "Metodele aritmetice (reducerea la unitate, comparația, figurativă, mersul invers, falsa ipoteză) se pot aplica și la probleme cu fracții și numere zecimale. De exemplu, metoda reducerii la unitate: dacă 5 kg de mere (fracționate) costă 10,5 lei, 1 kg costă 10,5 ÷ 5 = 2,1 lei. Metodele rămân aceleași, doar că lucrăm cu numere raționale în loc de numere naturale.", "questions": [{"questionNumber": 1, "questionText": "Dacă 3 cărți costă 21,6 lei, cât costă 5 cărți?", "options": ["A. 28 lei", "B. 30 lei", "C. 36 lei", "D. 40 lei"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Care metodă folosim pentru a afla preț unitar?", "options": ["A. Metoda falsei ipoteze", "B. Metoda reducerii la unitate", "C. Metoda mersului invers", "D. Metoda figurativă"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Calculează 2/3 din 15,6", "options": ["A. 10", "B. 10,2", "C. 10,4", "D. 11"], "correctAnswerIndex": 1}]},
        {"number": "9", "name": "Probleme de organizare a datelor. Frecvență. Grafice cu linii. Media unui set de date statistice", "summary": "Organizarea datelor presupune colectarea și aranjarea informației pentru a o putea analiza. Frecvența este numărul de ori pe care apare o valoare. Graficele cu linii sunt folosite pentru a arăta evoluția datelor în timp. Media unui set de date este suma tuturor valorilor împărțită la numărul de valori. De exemplu, media setului {2, 3, 4} = (2+3+4)/3 = 9/3 = 3. Acestea sunt baze ale statisticii.", "questions": [{"questionNumber": 1, "questionText": "Ce este frecvența în statistica?", "options": ["A. Valoarea cea mai mică", "B. Valoarea cea mai mare", "C. Numărul de ori pe care apare o valoare", "D. Suma tuturor valorilor"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Calculează media setului {2, 4, 6, 8}", "options": ["A. 4", "B. 5", "C. 6", "D. 7"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Pentru ce sunt folosite graficele cu linii?", "options": ["A. Pentru a arăta doar numere întregi", "B. Pentru a arăta evoluția datelor în timp", "C. Pentru a compara fracții", "D. Pentru a calcula media"], "correctAnswerIndex": 1}]}
    ]
}

# Unit 6: Elemente de geometrie și unități de măsură (9 lessons)
unit6_math_data = {
    "unit_number": "6",
    "unit_name": "Elemente de geometrie și unități de măsură",
    "lessons": [
        {"number": "1", "name": "Punct, dreaptă, plan, semiplan, semidreaptă, segment de dreaptă", "summary": "Geometria se bazează pe concepte fundamentale: Punctul este cea mai mică unitate, fără dimensiuni. Dreapta este o linie infinită în ambele direcții. Planul este o suprafață infinită bidimensională. Semiplanul este o jumătate de plan delimitată de o dreaptă. Semidreapta este o jumătate de dreaptă care are o origine dar se întinde infinit. Segmentul de dreaptă este porțiunea dintre două puncte. Aceste concepte sunt fundamentale în geometrie.", "questions": [{"questionNumber": 1, "questionText": "Care este diferența dintre o dreaptă și un segment?", "options": ["A. Dreapta este finită, segmentul este infinit", "B. Dreapta este infinită, segmentul are două capete", "C. Nu există diferență", "D. Segmentul este mai lung"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Ce este un punct în geometrie?", "options": ["A. O linie mică", "B. O figură cu o dimensiune", "C. Cea mai mică unitate, fără dimensiuni", "D. Un pătrat mic"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Ce este o semidreaptă?", "options": ["A. O dreapta întreagă", "B. O jumătate de dreaptă cu origine și infinit", "C. Un segment scurt", "D. Un punct"], "correctAnswerIndex": 1}]},
        {"number": "2", "name": "Pozițiile relative ale unui punct față de o dreaptă. Puncte coliniare. Pozițiile relative a două drepte: drepte concurente, drepte paralele", "summary": "Un punct poate fi pe dreapta (incident) sau în afara dreptei (nu incident). Punctele coliniare sunt puncte care se află pe aceeași dreaptă. Trei sau mai multe puncte pot fi coliniare (pe aceeași dreaptă) sau necoliniare. Două drepte pot fi: 1) Concurente - au un punct în comun, 2) Paralele - nu au niciun punct în comun și nu se întâlnesc niciodată, 3) Confundate - sunt aceeași dreaptă. Aceste relații sunt importante în geometrie.", "questions": [{"questionNumber": 1, "questionText": "Ce sunt punctele coliniare?", "options": ["A. Puncte care sunt foarte departe", "B. Puncte care se află pe aceeași dreaptă", "C. Puncte care sunt în afara unei drepte", "D. Puncte care sunt identice"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Cum se numesc două drepte care au un punct în comun?", "options": ["A. Paralele", "B. Confundate", "C. Concurente", "D. Perpendiculare"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Cum se numesc două drepte care nu au niciun punct în comun?", "options": ["A. Concurente", "B. Confundate", "C. Paralele", "D. Sechante"], "correctAnswerIndex": 2}]},
        {"number": "3", "name": "Lungimea unui segment. Distanța dintre două puncte. Segmente congruente", "summary": "Lungimea unui segment este distanța dintre capetele sale, măsurată în unități (cm, m, etc.). Distanța dintre două puncte este lungimea segmentului care le unește. Segmentele congruente sunt segmentele care au aceeași lungime. De exemplu, dacă AB = 5 cm și CD = 5 cm, atunci AB ≡ CD (AB este congruent cu CD). Congruența este echivalentă cu egalitatea pentru segmente.", "questions": [{"questionNumber": 1, "questionText": "Ce este congruența pentru segmente?", "options": ["A. Paralelsimul lor", "B. Aceeași lungime", "C. Aceeași poziție", "D. Aceeași direcție"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Cum se notează că segment AB este congruent cu segment CD?", "options": ["A. AB = CD", "B. AB ≡ CD", "C. AB ∥ CD", "D. AB ⊥ CD"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Care este distanța dintre punctele A și B dacă AB = 7 cm?", "options": ["A. 7 puncte", "B. 14 cm", "C. 7 cm", "D. 3,5 cm"], "correctAnswerIndex": 2}]},
        {"number": "4", "name": "Mijlocul unui segment. Simetricul unui punct față de un punct", "summary": "Mijlocul unui segment este punctul care împarte segmentul în două segmente congruente. De exemplu, dacă AB = 8 cm și M este mijlocul lui AB, atunci AM = MB = 4 cm. Simetricul unui punct A față de un punct M este punctul A' care se află pe dreapta AM, la aceeași distanță de M ca și A, dar pe cealaltă parte. De exemplu, dacă AM = 3 cm, atunci MA' = 3 cm, și A, M, A' sunt coliniare.", "questions": [{"questionNumber": 1, "questionText": "Ce este mijlocul unui segment?", "options": ["A. Un punct care îl împarte în două segmente inegale", "B. Un punct care îl împarte în două segmente congruente", "C. Capătul segmentului", "D. Un punct în afara segmentului"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Dacă AB = 10 cm și M este mijlocul lui AB, care este AM?", "options": ["A. 5 cm", "B. 10 cm", "C. 15 cm", "D. 20 cm"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Ce este simetricul unui punct A față de un punct O?", "options": ["A. Punctul A însuși", "B. Punctul pe cealaltă parte a lui O la aceeași distanță", "C. Un punct pe dreapta A", "D. Originea"], "correctAnswerIndex": 1}]},
        {"number": "5", "name": "Unghi: definiție, notații, elemente. Interiorul unui unghi, exteriorul unui unghi", "summary": "Unghiul este format din două semidrepte cu aceeași origine (vârf). Se notează cu ∠ABC sau ∠B, unde B este vârful. Elementele unui unghi sunt: vârful și laturile (semidreptele). Interiorul unghiului este regiunea dintre laturile unghiului. Exteriorul unghiului este restul planului. Unghiurile nule (0°), ascuțite (<90°), drepte (90°), obtuze (>90°, <180°), plate (180°) sunt clasificări după mărime.", "questions": [{"questionNumber": 1, "questionText": "Cum se notează un unghi cu vârf în B?", "options": ["A. [AB", "B. ∠ABC", "C. B∠", "D. AB°"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Ce este vârful unui unghi?", "options": ["A. Una dintre laturile unghiului", "B. Punctul de origine al unghiului", "C. Interiorul unghiului", "D. O latură a unghiului"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Ce este interiorul unui unghi?", "options": ["A. Doar vârful", "B. Doar laturile", "C. Regiunea dintre laturile unghiului", "D. Exteriorul unghiului"], "correctAnswerIndex": 2}]},
        {"number": "6", "name": "Măsura unui unghi. Unghiuri congruente (măsurarea și construcția cu raportorul)", "summary": "Măsura unui unghi se exprimă în grade (°). Un unghi complet (360°), unghi drept (90°), unghi plat (180°). Raportorul este instrumentul folosit pentru a măsura și construi unghiuri. Unghiurile congruente sunt unghiurile cu aceeași măsură. De exemplu, ∠ABC ≡ ∠DEF dacă ambele au 45°. Măsurarea cu raportorul: se aliniază centrul raportorului cu vârful unghiului, iar una dintre laturile unghiului cu baza raportorului.", "questions": [{"questionNumber": 1, "questionText": "Cât este măsura unui unghi drept?", "options": ["A. 45°", "B. 90°", "C. 180°", "D. 360°"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Ce sunt unghiurile congruente?", "options": ["A. Unghiuri cu vârfuri diferite", "B. Unghiuri cu aceeași măsură", "C. Unghiuri paralele", "D. Unghiuri perpendiculare"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Cu ce instrument se măsoară unghiurile?", "options": ["A. Riglă", "B. Compas", "C. Raportor", "D. Echer"], "correctAnswerIndex": 2}]},
        {"number": "7", "name": "Clasificarea unghiurilor. Calcule cu măsuri de unghiuri", "summary": "Clasificarea unghiurilor după mărime: Unghi nul (0°), Unghi ascuțit (0° < măsura < 90°), Unghi drept (90°), Unghi obtuz (90° < măsura < 180°), Unghi plat (180°), Unghi reflex (180° < măsura < 360°), Unghi complet (360°). Unghiurile complementare au suma 90°. Unghiurile suplimentare au suma 180°. Calcule cu unghiuri: adunare, scădere, înmulțire cu scalari. De exemplu, 30° + 45° = 75°, 90° - 30° = 60°.", "questions": [{"questionNumber": 1, "questionText": "Care este un unghi ascuțit?", "options": ["A. 90°", "B. 180°", "C. 45°", "D. 360°"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Ce sunt unghiurile complementare?", "options": ["A. Unghiuri cu suma 180°", "B. Unghiuri cu suma 90°", "C. Unghiuri cu suma 360°", "D. Unghiuri paralele"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Dacă unghiul A măsoară 60°, cât măsoară complementul său?", "options": ["A. 30°", "B. 90°", "C. 120°", "D. 180°"], "correctAnswerIndex": 0}]},
        {"number": "8", "name": "Unități de măsură pentru lungime, arie, volum, capacitate, masă, timp și unități monetare", "summary": "Unitățile de măsură fundamentale: Lungime: mm, cm, m, km. Arie: mm², cm², m², km², hectar. Volum: mm³, cm³, m³, litru. Capacitate: ml, l. Masă: mg, g, kg, t. Timp: s, min, h, zile, luni, ani. Unități monetare: bani, lei (RON), euro, dolari, etc. Conversiile între unități: 1 m = 100 cm, 1 km = 1000 m, 1 kg = 1000 g, 1 h = 60 min, etc.", "questions": [{"questionNumber": 1, "questionText": "Câți centimetri sunt într-un metru?", "options": ["A. 10 cm", "B. 100 cm", "C. 1000 cm", "D. 1 cm"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Câte grame sunt într-un kilogram?", "options": ["A. 100 g", "B. 1000 g", "C. 10 g", "D. 10000 g"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Câte minute sunt într-o oră?", "options": ["A. 30 min", "B. 60 min", "C. 100 min", "D. 120 min"], "correctAnswerIndex": 1}]},
        {"number": "9", "name": "Perimetrul și aria unei figuri geometrice. Aria discului. Lungimea cercului", "summary": "Perimetrul este suma lungimilor laturilor unei figuri. De exemplu, perimetrul pătratului cu latura a este 4a. Aria este măsura suprafeței unei figuri. De exemplu, aria pătratului cu latura a este a². Pentru cerc: Lungimea cercului (circumferința) = 2πr, unde r este raza. Aria discului = πr². Aceste formule sunt esențiale pentru calculele geometrice.", "questions": [{"questionNumber": 1, "questionText": "Care este formula perimetrului pătratului cu latura a?", "options": ["A. a", "B. a²", "C. 4a", "D. 2a"], "correctAnswerIndex": 2}, {"questionNumber": 2, "questionText": "Care este formula ariei unui dreptunghi cu laturile a și b?", "options": ["A. a + b", "B. 2a + 2b", "C. a × b", "D. a² + b²"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Care este formula lungimii unui cerc cu raza r?", "options": ["A. πr", "B. 2πr", "C. πr²", "D. r²"], "correctAnswerIndex": 1}]}
    ]
}

# Save all units
for unit_data, filename in [
    (unit3_math_data, "math_unit3_lessons_complete.json"),
    (unit4_math_data, "math_unit4_lessons_complete.json"),
    (unit5_math_data, "math_unit5_lessons_complete.json"),
    (unit6_math_data, "math_unit6_lessons_complete.json")
]:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(unit_data, f, ensure_ascii=False, indent=2)
    print(f"✓ {filename}: {len(unit_data['lessons'])} lessons, {sum(len(l['questions']) for l in unit_data['lessons'])} questions")

