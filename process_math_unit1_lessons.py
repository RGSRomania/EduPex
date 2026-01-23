#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Unit 1 lessons from Clasa a V a Matematica
Extract summaries and generate questions for each lesson
"""

import json

# Unit 1 Lesson Data with content summaries and questions
unit1_math_data = {
    "unit_number": "1",
    "unit_name": "Operații cu numere",
    "lessons": [
        {
            "number": "1",
            "name": "Scrierea și citirea numerelor naturale",
            "summary": """Numerele naturale sunt utilizate pentru a număra și pentru a ordona obiecte. Scrierea numerelor naturale 
            se face utilizând zece cifre: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. În sistemul de numerație zecimal (baza 10), poziția 
            unei cifre determină valoarea acesteia. De exemplu, în numărul 3245, cifra 3 reprezintă 3 mii, 2 reprezintă 2 sute, 
            4 reprezintă 4 zeci, iar 5 reprezintă 5 unități. Citirea numerelor naturale se face respectând poziția cifrelor și 
            grupurile de câte trei cifre (mii, milioane, miliarde). Aceasta este fundamentală pentru înțelegerea calculelor 
            matematice ulterioare.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Câte cifre sunt utilizate în sistemul de numerație zecimal?",
                    "options": [
                        "A. 9 cifre",
                        "B. 10 cifre (de la 0 la 9)",
                        "C. 8 cifre",
                        "D. 11 cifre"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este valoarea cifrei 5 în numărul 2531?",
                    "options": [
                        "A. 5 unități",
                        "B. 50 de unități",
                        "C. 500 de unități",
                        "D. 5000 de unități"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 3,
                    "questionText": "Cum se grupează cifrele pentru a citi numerele mari?",
                    "options": [
                        "A. Grupuri de 2 cifre",
                        "B. Grupuri de 5 cifre",
                        "C. Grupuri de 3 cifre",
                        "D. Grupuri de 4 cifre"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "2",
            "name": "Reprezentarea pe axa numerelor. Compararea și ordonarea numerelor naturale; aproximări, estimări",
            "summary": """Axa numerelor este o dreaptă pe care sunt marcate puncte corespunzătoare numerelor naturale. Reprezentarea 
            pe axa numerelor ajută la vizualizarea ordinii numerelor. Orice două numere naturale pot fi comparate: un număr este mai 
            mic, egal sau mai mare decât altul. Ordonarea numerelor naturale în ordine crescătoare sau descrescătoare este importantă 
            în rezolvarea problemelor. Aproximarea unui număr înseamnă a-l înlocui cu un alt număr apropiat (de obicei rotunjit). 
            Estimarea înseamnă a evalua o valoare aproximativă fără calcul exact. Aceste abilități sunt esențiale în viața practică.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este axa numerelor?",
                    "options": [
                        "A. O figură geometrică",
                        "B. O dreaptă pe care sunt marcate puncte corespunzătoare numerelor naturale",
                        "C. Un cerc cu numere",
                        "D. O tabel cu numere"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este semnul de comparație corect pentru numerele 234 și 432?",
                    "options": [
                        "A. 234 > 432",
                        "B. 234 = 432",
                        "C. 234 < 432",
                        "D. 234 >= 432"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce înseamnă aproximarea unui număr?",
                    "options": [
                        "A. A-l calcula exact",
                        "B. A-l înlocui cu altul apropiat, de obicei rotunjit",
                        "C. A-l ignora",
                        "D. A-l dubla"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "3",
            "name": "Adunarea numerelor naturale, proprietăți",
            "summary": """Adunarea este operația care reunește două sau mai multe cantități. În adunare, numerele care se adună se numesc 
            termeni, iar rezultatul se numește sumă. De exemplu, în 5 + 3 = 8, 5 și 3 sunt termeni, iar 8 este suma. Adunarea are 
            proprietăți importante: comutativitate (a + b = b + a), asociativitate ((a + b) + c = a + (b + c)), și element neutru 
            (a + 0 = a). Aceste proprietăți facilitează calculele și sunt fundamentale pentru algebră. Adunarea este inversă scăderii.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se numesc numerele care se adună?",
                    "options": [
                        "A. Factori",
                        "B. Termeni",
                        "C. Coeficienți",
                        "D. Variabile"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este proprietatea comutativității adunării?",
                    "options": [
                        "A. a + b = b * a",
                        "B. a + b = b + a",
                        "C. a + b = a - b",
                        "D. a + b = a + b + c"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care este elementul neutru al adunării?",
                    "options": [
                        "A. 1",
                        "B. -1",
                        "C. 0",
                        "D. 10"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "4",
            "name": "Scăderea numerelor naturale",
            "summary": """Scăderea este operația inversă adunării. În scădere, primul număr se numește descăzut, al doilea se numește scăzător, 
            iar rezultatul se numește rest sau diferență. De exemplu, în 10 - 3 = 7, 10 este descăzutul, 3 este scăzătorul, iar 7 este 
            diferența. Scăderea nu are proprietatea comutativității: 10 - 3 ≠ 3 - 10. Scăderea este posibilă în numerele naturale doar 
            dacă descăzutul este mai mare sau egal cu scăzătorul. Pentru a verifica corectitudinea unei scăderi, adunăm diferența cu scăzătorul 
            și trebuie să obținem descăzutul.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se numesc componentele scăderii a - b = c?",
                    "options": [
                        "A. a = minuend, b = subrahend, c = rezultat",
                        "B. a = descăzut, b = scăzător, c = diferență",
                        "C. a = sum, b = term, c = rest",
                        "D. a = factor, b = divizor, c = cât"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Este scăderea comutativă?",
                    "options": [
                        "A. Da, a - b = b - a",
                        "B. Nu, a - b ≠ b - a",
                        "C. Doar pentru numere pare",
                        "D. Doar pentru numere mari"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Calculează: 25 - 8 = ?",
                    "options": [
                        "A. 15",
                        "B. 17",
                        "C. 18",
                        "D. 20"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "5",
            "name": "Înmulțirea numerelor naturale, proprietăți",
            "summary": """Înmulțirea este o operație care repetă adunarea. De exemplu, 3 × 4 înseamnă 4 + 4 + 4 = 12. Numerele care se înmulțesc 
            se numesc factori, iar rezultatul se numește produs. Înmulțirea are proprietăți importante: comutativitate (a × b = b × a), 
            asociativitate ((a × b) × c = a × (b × c)), distributivitate (a × (b + c) = a × b + a × c), și element neutru (a × 1 = a). 
            Înmulțirea cu 0 dă întotdeauna 0. Aceste proprietăți facilitează calculele și sunt fundamentale pentru matematică. Înmulțirea 
            este inversă împărțirii.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se numesc numerele care se înmulțesc?",
                    "options": [
                        "A. Termeni",
                        "B. Factori",
                        "C. Coeficienți",
                        "D. Variabile"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este elementul neutru al înmulțirii?",
                    "options": [
                        "A. 0",
                        "B. -1",
                        "C. 1",
                        "D. 10"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce rezultă din înmulțirea unui număr cu 0?",
                    "options": [
                        "A. Același număr",
                        "B. 1",
                        "C. 0",
                        "D. Opusul numărului"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "6",
            "name": "Factor comun",
            "summary": """Factorul comun este o metodă de simplificare a expresiilor matematice. Dacă o expresie conține termeni care au un factor 
            comun, putem scoate acel factor în afara unei paranteze. De exemplu, 5 × 3 + 5 × 7 = 5 × (3 + 7) = 5 × 10 = 50. Aceasta este 
            aplicarea proprietății distributive a înmulțirii. Scoaterea factorului comun facilitează calculele și este importantă în algebră. 
            Aceasta se numește și factorizare. Prin scoaterea factorului comun, expresiile complexe devin mai simple și mai ușor de calculat.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este factorul comun?",
                    "options": [
                        "A. Un factor care apare în toți termenii unei expresii",
                        "B. Un factor care apare doar în unii termeni",
                        "C. Un factor care nu apare nicăieri",
                        "D. Un factor care este mai mare decât toți termenii"
                    ],
                    "correctAnswerIndex": 0
                },
                {
                    "questionNumber": 2,
                    "questionText": "Scoate factorul comun: 4 × 5 + 4 × 3 = ?",
                    "options": [
                        "A. 4 × (5 + 3) = 4 × 8 = 32",
                        "B. 4 × (5 × 3) = 4 × 15 = 60",
                        "C. (4 + 5) × (4 + 3) = 9 × 7 = 63",
                        "D. 4 + 5 + 4 + 3 = 16"
                    ],
                    "correctAnswerIndex": 0
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care proprietate permite scoaterea factorului comun?",
                    "options": [
                        "A. Comutativitate",
                        "B. Asociativitate",
                        "C. Distributivitate",
                        "D. Reflexivitate"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "7",
            "name": "Împărțirea cu rest 0 a numerelor naturale",
            "summary": """Împărțirea exactă (cu rest 0) este operația inversă înmulțirii. În împărțire, primul număr se numește deîmpărțit, al doilea 
            se numește împărțitor, iar rezultatul se numește cât. De exemplu, în 12 ÷ 3 = 4, 12 este deîmpărțitul, 3 este împărțitorul, iar 4 
            este câtul. Împărțirea cu rest 0 se petrece doar dacă deîmpărțitul este divizibil cu împărțitorul, adică restul este 0. Împărțirea 
            nu este comutativă și nici asociativă. Pentru a verifica corectitudinea împărțirii, înmulțim câtul cu împărțitorul și trebuie să 
            obținem deîmpărțitul.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se numesc componentele împărțirii a ÷ b = c?",
                    "options": [
                        "A. a = dividend, b = divisor, c = quotient",
                        "B. a = deîmpărțit, b = împărțitor, c = cât",
                        "C. a = factor, b = multiplicand, c = produs",
                        "D. a = descăzut, b = scăzător, c = diferență"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce condiție trebuie îndeplinită pentru ca împărțirea să fie exactă?",
                    "options": [
                        "A. Deîmpărțitul să fie mai mic decât împărțitorul",
                        "B. Deîmpărțitul să fie divizibil cu împărțitorul",
                        "C. Împărțitorul să fie 1",
                        "D. Deîmpărțitul și împărțitorul să fie egali"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Calculează: 20 ÷ 4 = ?",
                    "options": [
                        "A. 4",
                        "B. 5",
                        "C. 6",
                        "D. 24"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "8",
            "name": "Împărțirea cu rest a numerelor naturale",
            "summary": """Împărțirea cu rest este o extensie a împărțirii exacte. Când un număr nu este divizibil cu altul, rezultatul are un rest. 
            Formula este: deîmpărțit = împărțitor × cât + rest, unde restul este întotdeauna mai mic decât împărțitorul. De exemplu, în 17 ÷ 5, 
            câtul este 3 și restul este 2, deoarece 17 = 5 × 3 + 2. Restul trebuie să satisfacă condiția 0 ≤ rest < împărțitor. Împărțirea cu rest 
            este utilă în situații practice și în teoria numerelor. Verificarea se face prin formula menționată.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Care este formula pentru împărțirea cu rest?",
                    "options": [
                        "A. deîmpărțit = împărțitor + cât + rest",
                        "B. deîmpărțit = împărțitor × cât + rest",
                        "C. deîmpărțit = împărțitor - cât + rest",
                        "D. deîmpărțit = împărțitor ÷ cât - rest"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este restul din împărțirea 23 ÷ 7?",
                    "options": [
                        "A. 1",
                        "B. 2",
                        "C. 3",
                        "D. 4"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care condiție trebuie îndeplinită de rest?",
                    "options": [
                        "A. rest > împărțitor",
                        "B. rest = împărțitor",
                        "C. 0 ≤ rest < împărțitor",
                        "D. rest > deîmpărțit"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "9",
            "name": "Puterea cu exponent natural a unui număr natural. Pătratul unui număr natural",
            "summary": """Puterea unui număr este o notație pentru a exprima înmulțirea repetată. Dacă a este baza și n este exponentul, atunci 
            a^n = a × a × ... × a (de n ori). De exemplu, 2^3 = 2 × 2 × 2 = 8. Pătratul unui număr este cazul special când exponentul este 2: 
            a^2 = a × a. De exemplu, 5^2 = 5 × 5 = 25. Cubul unui număr este când exponentul este 3: a^3 = a × a × a. Puterea cu exponent 0 este 
            întotdeauna 1 (a^0 = 1), iar puterea cu exponent 1 este chiar baza (a^1 = a). Puterile sunt utilizate frecvent în matematică și știință.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se notează puterea unui număr?",
                    "options": [
                        "A. a (baza)",
                        "B. n (exponentul)",
                        "C. a^n (baza la puterea exponentului)",
                        "D. a × n"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 2,
                    "questionText": "Calculează 3^2",
                    "options": [
                        "A. 6",
                        "B. 8",
                        "C. 9",
                        "D. 12"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care este valoarea oricărei numere la puterea 0?",
                    "options": [
                        "A. 0",
                        "B. 1",
                        "C. Baza insăși",
                        "D. Nedefinit"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "10",
            "name": "Reguli de calcul cu puteri",
            "summary": """Regulile de calcul cu puteri facilitează simplificarea expresiilor cu exponenți. Principalele reguli sunt: înmulțirea de puteri 
            cu aceeași bază (a^m × a^n = a^(m+n)), împărțirea de puteri cu aceeași bază (a^m ÷ a^n = a^(m-n)), puterea unei puteri ((a^m)^n = a^(m×n)), 
            puterea unui produs ((a × b)^n = a^n × b^n), și puterea unui cât ((a ÷ b)^n = a^n ÷ b^n). Aceste reguli sunt esențiale pentru calculele 
            cu exponenți și pentru algebră. Trebuie memorate și practicate pentru a putea fi aplicate corect în diverse situații.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se calculează a^m × a^n?",
                    "options": [
                        "A. a^(m × n)",
                        "B. a^(m + n)",
                        "C. a^(m - n)",
                        "D. (a × a)^(m + n)"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Calculează 2^3 × 2^2",
                    "options": [
                        "A. 2^5 = 32",
                        "B. 2^6 = 64",
                        "C. 4^5 = 1024",
                        "D. 2^1 = 2"
                    ],
                    "correctAnswerIndex": 0
                },
                {
                    "questionNumber": 3,
                    "questionText": "Cum se calculează (a^m)^n?",
                    "options": [
                        "A. a^(m + n)",
                        "B. a^(m × n)",
                        "C. a^(m - n)",
                        "D. (a^n)^m"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "11",
            "name": "Compararea puterilor",
            "summary": """Compararea puterilor înseamnă a determina care dintre două puteri este mai mare, mai mică sau egală. Pentru a compara puteri, 
            putem: 1) calcula valorile și compara rezultatele, 2) reduce la aceeași bază și compara exponenții, 3) reduce la același exponent și compara 
            bazele. De exemplu, 2^3 și 3^2: 2^3 = 8 și 3^2 = 9, deci 2^3 < 3^2. Dacă bazele sunt egale și mai mari decât 1, atunci puterea cu exponent 
            mai mare este mai mare. Dacă exponenții sunt egali și pozitivi, atunci puterea cu baza mai mare este mai mare. Competența în compararea 
            puterilor este importantă în rezolvarea inegalităților.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Compară 2^4 și 4^2",
                    "options": [
                        "A. 2^4 > 4^2",
                        "B. 2^4 = 4^2",
                        "C. 2^4 < 4^2",
                        "D. 2^4 ≤ 4^2"
                    ],
                    "correctAnswerIndex": 0
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care putere este mai mare: 3^2 sau 2^3?",
                    "options": [
                        "A. 3^2 = 9, deci 3^2 > 2^3",
                        "B. 2^3 = 8, deci 2^3 > 3^2",
                        "C. Sunt egale",
                        "D. Nu se pot compara"
                    ],
                    "correctAnswerIndex": 0
                },
                {
                    "questionNumber": 3,
                    "questionText": "Dacă a^m > a^n și a > 1, ce relație există între m și n?",
                    "options": [
                        "A. m < n",
                        "B. m = n",
                        "C. m > n",
                        "D. m și n nu sunt comparabile"
                    ],
                    "correctAnswerIndex": 2
                }
            ]
        },
        {
            "number": "12",
            "name": "Scrierea în baza 10. Scrierea în baza 2",
            "summary": """Sistemul de numerație zecimal (baza 10) este cel pe care îl folosim zilnic. Orice număr în baza 10 poate fi scris ca o sumă de 
            puteri ale lui 10. De exemplu, 3245 = 3×10^3 + 2×10^2 + 4×10^1 + 5×10^0. Baza 2 (sistem binar) este utilizată în informatică. În baza 2, 
            se folosesc doar cifrele 0 și 1. De exemplu, 1011 în baza 2 este egal cu 1×2^3 + 0×2^2 + 1×2^1 + 1×2^0 = 8 + 0 + 2 + 1 = 11 în baza 10. 
            Conversia între baze necesită înțelegerea valorilor poziționale ale cifrelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cum se scrie 345 în descompunere în baza 10?",
                    "options": [
                        "A. 3×10 + 4×10 + 5×10",
                        "B. 3×10^2 + 4×10^1 + 5×10^0",
                        "C. 3×1000 + 4×100 + 5×10",
                        "D. 3 + 4 + 5"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care sunt cifrele utilizate în baza 2?",
                    "options": [
                        "A. 0, 1, 2",
                        "B. 0, 1",
                        "C. 0, 1, 2, ..., 9",
                        "D. 1, 2, 3, ..., 10"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Transformă 101 din baza 2 în baza 10",
                    "options": [
                        "A. 5",
                        "B. 3",
                        "C. 6",
                        "D. 101"
                    ],
                    "correctAnswerIndex": 0
                }
            ]
        },
        {
            "number": "13",
            "name": "Ordinea efectuării operațiilor; utilizarea parantezelor: rotunde, pătrate și acolade",
            "summary": """Ordinea efectuării operațiilor (PEMDAS/BODMAS) stabilește care operații să se efectueze mai întâi: 1) Parantezele (rotunde, 
            pătrate, acolade), 2) Exponenți/Puteri, 3) Înmulțire și Împărțire (de la stânga la dreapta), 4) Adunare și Scădere (de la stânga la dreapta). 
            De exemplu, în 2 + 3 × 4, se efectuează mai întâi 3 × 4 = 12, apoi 2 + 12 = 14. Parantezele se folosesc pentru a schimba ordinea. De exemplu, 
            (2 + 3) × 4 = 5 × 4 = 20. Parantezele pătrate și acolade se utilizează pentru gruparea operațiilor complexe. Respectarea acestei ordini este 
            esențială pentru obținerea rezultatelor corecte.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Care este ordinea de precedență a operațiilor?",
                    "options": [
                        "A. Adunare, Scădere, Înmulțire, Împărțire",
                        "B. Paranteze, Exponenți, Înmulțire/Împărțire, Adunare/Scădere",
                        "C. Înmulțire, Adunare, Exponenți, Paranteze",
                        "D. Împărțire, Scădere, Puteri, Paranteze"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Calculează: 2 + 3 × 4",
                    "options": [
                        "A. 20",
                        "B. 14",
                        "C. 12",
                        "D. 9"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Calculează: (2 + 3) × 4",
                    "options": [
                        "A. 14",
                        "B. 20",
                        "C. 12",
                        "D. 9"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        }
    ]
}

# Save to JSON file
output_path = "math_unit1_lessons_complete.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(unit1_math_data, f, ensure_ascii=False, indent=2)

print(f"✓ Matematica Unit 1 complete data saved to {output_path}")
print(f"✓ Total lessons processed: {len(unit1_math_data['lessons'])}")
print(f"✓ Total questions generated: {sum(len(lesson['questions']) for lesson in unit1_math_data['lessons'])}")

