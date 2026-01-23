#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Unit 2 lessons from Clasa a V a Matematica
Extract summaries and generate questions for each lesson
"""

import json

# Unit 2 Lesson Data with content summaries and questions
unit2_math_data = {
    "unit_number": "2",
    "unit_name": "Metode aritmetice",
    "lessons": [
        {
            "number": "1",
            "name": "Metoda reducerii la unitate",
            "summary": """Metoda reducerii la unitate este o metodă de rezolvare a problemelor în care se cunosc mai multe unități și se dorește 
            să se afle valoarea unei singure unități, apoi a unui număr dat de unități. De exemplu, dacă 5 cărți costă 50 de lei, metoda reducerii 
            la unitate presupune: 1) aflarea preţului unei cărți (50 ÷ 5 = 10 lei), 2) aflarea preţului pentru numărul dorit de cărți (10 × 8 = 80 
            lei pentru 8 cărți). Această metodă este utilă pentru probleme de proporționalitate directă. Pasii sunt: 1) calculează valoarea unei 
            unități, 2) calculează valoarea pentru numărul de unități dorit. Este una dintre cele mai frecvent utilizate metode aritmetice.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Care este primul pas în metoda reducerii la unitate?",
                    "options": [
                        "A. Calcularea valorii pentru toate unitățile",
                        "B. Calcularea valorii unei singure unități",
                        "C. Dublarea valorii totale",
                        "D. Împărțirea la 10"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Dacă 4 kg de mere costă 12 lei, cât costă 7 kg de mere?",
                    "options": [
                        "A. 19 lei",
                        "B. 21 lei",
                        "C. 24 lei",
                        "D. 28 lei"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Pentru ce tip de probleme este utilă metoda reducerii la unitate?",
                    "options": [
                        "A. Pentru probleme cu numere negative",
                        "B. Pentru probleme de proporționalitate directă",
                        "C. Pentru probleme cu puteri",
                        "D. Pentru probleme cu unghiuri"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "2",
            "name": "Metoda comparației",
            "summary": """Metoda comparației este o metodă de rezolvare a sistemelor de ecuații în care se compară două situații pentru a elimina una 
            dintre necunoscute. De exemplu: dacă 3 creioane și 2 pixuri costă 11 lei, iar 3 creioane și 4 pixuri costă 17 lei, prin scăderea primei 
            ecuații din a doua, obținem 2 pixuri = 6 lei. Pasii sunt: 1) scriem datele pentru două situații, 2) selectăm una dintre necunoscute și 
            o facem egală prin amplificare, 3) scădem o ecuație din cealaltă pentru a elimina acea necunoscută, 4) calculăm valoarea necunoscutei 
            rămase, 5) înlocuim pentru a afla și cealaltă necunoscută. Această metodă este eficientă pentru probleme cu două necunoscute.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Care este scopul metodei comparației?",
                    "options": [
                        "A. Să adune toate valorile",
                        "B. Să elimine una dintre necunoscute prin comparație",
                        "C. Să înmulțească toate datele",
                        "D. Să ridice la pătrat valorile"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce facem după ce comparăm două situații în metoda comparației?",
                    "options": [
                        "A. Adunăm ecuațiile",
                        "B. Scădem o ecuație din cealaltă pentru a elimina o necunoscută",
                        "C. Înmulțim ecuațiile",
                        "D. Împărțim ecuațiile"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Pentru câte necunoscute este utilă metoda comparației?",
                    "options": [
                        "A. Pentru o singură necunoscută",
                        "B. Pentru două necunoscute",
                        "C. Pentru trei necunoscute",
                        "D. Pentru mai mult de patru necunoscute"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "3",
            "name": "Metoda figurativă",
            "summary": """Metoda figurativă este o metodă de rezolvare a problemelor în care se folosesc figuri (segmente, desene) pentru a representa 
            datele problemei. De exemplu, dacă într-o clasă sunt fete și băieți, și știm că sunt 5 mai mulți băieți decât fete, putem desena segmente 
            pentru a reprezenta fiecare grup și a afla numerele. Pasii sunt: 1) desenezi segmente egale pentru a reprezenta parți egale, 2) adaugi 
            segmente suplimentare pentru diferență, 3) calculezi valoarea unui segment, 4) afli valorile pentru fiecare grup. Această metodă este 
            vizuală și ajută la înțelegerea mai bună a problemei, mai ales pentru copiii mai mici.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce se folosește în metoda figurativă?",
                    "options": [
                        "A. Formule algebrice",
                        "B. Figuri și segmente pentru a reprezenta datele",
                        "C. Doar numere",
                        "D. Doar litere"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este primul pas în metoda figurativă?",
                    "options": [
                        "A. Calcularea rezultatului final",
                        "B. Desenarea segmentelor pentru a reprezenta parți egale",
                        "C. Scăderea numerelor",
                        "D. Înmulțirea datelor"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "De ce este utilă metoda figurativă?",
                    "options": [
                        "A. Pentru că e complicată",
                        "B. Pentru că ajută la înțelegerea vizuală a problemei",
                        "C. Pentru că necesită mai mult timp",
                        "D. Pentru că e doar pentru joc"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "4",
            "name": "Metoda mersului invers",
            "summary": """Metoda mersului invers este o metodă de rezolvare a problemelor în care se cunosce rezultatul final și trebuie să se afle 
            valoarea inițială. Se numește ''mersul invers'' deoarece operațiile se efectuează în ordine inversă, cu operatori inverși. De exemplu: 
            dacă după ce am cheltuit 50 de lei și apoi am primit 20 de lei, îmi rămân 100 de lei, cât am avut inițial? Mersul invers: 100 - 20 + 
            50 = 130 lei. Pasii sunt: 1) identifici rezultatul final, 2) identifici operațiile în ordine, 3) efectuezi operațiile inverse în ordine 
            inversă. Această metodă este foarte utilă pentru probleme în care nu cunoaștem valoarea inițială.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce se cunoaște în problemele rezolvate prin metoda mersului invers?",
                    "options": [
                        "A. Valoarea inițială",
                        "B. Valoarea finală și operațiile efectuate",
                        "C. Doar operațiile",
                        "D. Nimic din datele de mai sus"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Cum se numesc operațiile efectuate în metoda mersului invers?",
                    "options": [
                        "A. Aceleași operații",
                        "B. Operații inverse ale celor inițiale",
                        "C. Operații mai complicate",
                        "D. Nu se schimbă operațiile"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Dacă x + 30 - 15 = 50, care este valoarea lui x?",
                    "options": [
                        "A. 35",
                        "B. 45",
                        "C. 55",
                        "D. 65"
                    ],
                    "correctAnswerIndex": 0
                }
            ]
        },
        {
            "number": "5",
            "name": "Metoda falsei ipoteze",
            "summary": """Metoda falsei ipoteze este o metodă de rezolvare a problemelor în care se presupune (ipoteza) o valoare pentru o necunoscută, 
            se calculează consequențele acestei ipoteze, și dacă nu se potrivesc cu datele reale, se corespunde. De exemplu: problemă cu găini și 
            iepuri. Presupunem că toate sunt găini (care au 2 picioare). Calculăm total picioare. Dacă nu se potrivește cu realitatea, calculăm 
            diferența și o corespundem. Pasii sunt: 1) faci o ipoteză asupra unei necunoscute, 2) calculezi consequențele, 3) compari cu realitatea, 
            4) corespunzi ipoteza pe bază de diferență. Aceasta este o metodă prin încercare și eroare, dar sistematică și eficientă.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce face metoda falsei ipoteze?",
                    "options": [
                        "A. Face calcule fără logică",
                        "B. Presupune o valoare și o corespunde pe bază de diferență",
                        "C. Ghicește răspunsul",
                        "D. Nu are nici o bază"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este al doilea pas în metoda falsei ipoteze?",
                    "options": [
                        "A. Să presupunem o altă valoare",
                        "B. Să calculez consequențele ipotezei",
                        "C. Să verific răspunsul",
                        "D. Să renunț"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Pentru ce tip de probleme este utilă metoda falsei ipoteze?",
                    "options": [
                        "A. Pentru probleme cu o singură necunoscută",
                        "B. Pentru probleme cu două categorii diferite (ex: găini și iepuri)",
                        "C. Pentru probleme cu geometrie",
                        "D. Pentru probleme cu fracții"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        }
    ]
}

# Save to JSON file
output_path = "math_unit2_lessons_complete.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(unit2_math_data, f, ensure_ascii=False, indent=2)

print(f"✓ Matematica Unit 2 complete data saved to {output_path}")
print(f"✓ Total lessons processed: {len(unit2_math_data['lessons'])}")
print(f"✓ Total questions generated: {sum(len(lesson['questions']) for lesson in unit2_math_data['lessons'])}")

