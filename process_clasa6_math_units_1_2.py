#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Clasa a VI a Matematica - All Units
Extract summaries and generate questions for each lesson
"""

import json

# Unit 1: Mulțimi. Mulțimea numerelor naturale (7 lessons)
unit1_data = {
    "unit_number": "1",
    "unit_name": "Mulțimi. Mulțimea numerelor naturale",
    "lessons": [
        {
            "number": "1",
            "name": "Mulțimi: descriere, notații, reprezentări. Mulțimi numerice/nenumerice. Relația dintre un element și o mulțime",
            "summary": "O mulțime este o colecție de elemente bine definite. Se notează cu litere mari: A, B, C și elementele cu litere mici: a, b, c. Reprezentări: enumerare {1, 2, 3}, diagramă Venn, sau proprietate P(x). Relația dintre element și mulțime: x ∈ A (x aparține A) sau x ∉ A (x nu aparține A). Mulțimi numerice: conțin numere (ℕ, ℤ, ℚ, ℝ). Mulțimi nenumerice: conțin alte obiecte (copaci, culori). Conceptul de mulțime este fundamental în matematică modernă și permite definirea altor concepte.",
            "questions": [
                {"questionNumber": 1, "questionText": "Ce este o mulțime?", "options": ["A. Un singur element", "B. O colecție de elemente bine definite", "C. Doar numere", "D. Un set neordonat"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "Cum se notează relația 'x aparține A'?", "options": ["A. x ⊂ A", "B. x ∉ A", "C. x ∈ A", "D. x = A"], "correctAnswerIndex": 2},
                {"questionNumber": 3, "questionText": "Care sunt tipuri de mulțimi?", "options": ["A. Doar numerice", "B. Numerice și nenumerice", "C. Doar infinite", "D. Doar ordonate"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "2",
            "name": "Relații între mulțimi",
            "summary": "Relații importante între mulțimi: Egalitate (A = B dacă au aceleași elemente), Incluziune (A ⊆ B dacă orice element al A este în B), Incluziune strictă (A ⊂ B dacă A ⊆ B dar A ≠ B), Mulțimea vidă (∅ = mulțimea fără elemente). Diagramele Venn sunt utile pentru vizualizare. Exemple: {1, 2} ⊂ {1, 2, 3}, {a} ⊆ {a}, ∅ ⊆ orice mulțime. Înțelegerea acestor relații este esențială pentru operații cu mulțimi.",
            "questions": [
                {"questionNumber": 1, "questionText": "Ce înseamnă A ⊆ B?", "options": ["A. A este mai mare decât B", "B. Orice element al A este în B", "C. A și B sunt disjuncte", "D. A este infinit"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "Care este diferența între ⊆ și ⊂?", "options": ["A. Nu există diferență", "B. ⊆ permite egalitate, ⊂ nu", "C. ⊂ permite egalitate, ⊆ nu", "D. ⊂ este pentru numere"], "correctAnswerIndex": 1},
                {"questionNumber": 3, "questionText": "Ce este mulțimea vidă?", "options": ["A. Mulțimea cu infinit elemente", "B. Mulțimea fără elemente", "C. Mulțimea cu 1 element", "D. Mulțimea tuturor numerelor"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "3",
            "name": "Mulțimi finite, cardinalul unei mulțimi finite. Mulțimi infinite. Mulțimea numerelor naturale",
            "summary": "Mulțimi finite: au un număr finit de elemente. Cardinalul |A| = numărul de elemente. Exemple: |{1, 2, 3}| = 3. Mulțimi infinite: au infinit de elemente. Mulțimea numerelor naturale ℕ = {0, 1, 2, 3, ...} este infinită. Diferența între |A| și cardinal abstract. Teorema: dacă A ⊂ B și A finit, atunci |A| < |B|. Pentru mulțimi infinite, cardinalii sunt mai complexi (cardinali transfinici). Această lecție introduce conceptul fundamental de mărime a unei mulțimi.",
            "questions": [
                {"questionNumber": 1, "questionText": "Ce este cardinalul unei mulțimi?", "options": ["A. Suma elementelor", "B. Numărul de elemente", "C. Ordinea elementelor", "D. Forma mulțimii"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "Este ℕ finit sau infinit?", "options": ["A. Finit cu 10 elemente", "B. Finit dar mare", "C. Infinit", "D. Gol"], "correctAnswerIndex": 2},
                {"questionNumber": 3, "questionText": "Care este |∅|?", "options": ["A. 1", "B. 0", "C. ∞", "D. Nedefinit"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "4",
            "name": "Operații cu mulțimi: reuniune, intersecție, diferență",
            "summary": "Operații fundamentale: Reuniune (A ∪ B) = {x | x ∈ A sau x ∈ B} = toate elementele din A sau B. Intersecție (A ∩ B) = {x | x ∈ A și x ∈ B} = elemente comune. Diferență (A \\ B) = {x | x ∈ A și x ∉ B} = elemente doar în A. Proprietăți: comutativitate, asociativitate, distributivitate. Exemple: {1,2} ∪ {2,3} = {1,2,3}, {1,2} ∩ {2,3} = {2}, {1,2} \\ {2,3} = {1}. Diagramele Venn sunt esențiale pentru vizualizare. Aceste operații sunt fundamentale în teoria mulțimilor.",
            "questions": [
                {"questionNumber": 1, "questionText": "Ce este A ∪ B?", "options": ["A. Elementele comune", "B. Toate elementele din A sau B", "C. Elementele doar din A", "D. Mulțimea vidă"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "{1,2} ∩ {2,3} = ?", "options": ["A. {1,2,3}", "B. {2}", "C. {1,3}", "D. ∅"], "correctAnswerIndex": 1},
                {"questionNumber": 3, "questionText": "Ce este A \\ B?", "options": ["A. Elementele din ambele", "B. Elementele doar din A", "C. Toate elementele", "D. Niciunul"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "5",
            "name": "Descompunerea numerelor naturale în produs de puteri de numere prime",
            "summary": "Orice număr natural > 1 poate fi scris unic ca produs de puteri de numere prime (Teorema Fundamentală a Aritmeticii). Proces: împarte la cel mai mic divizor prim, repetă până obții 1. Exemplu: 60 = 2² × 3 × 5. Forma standard: n = p₁^a₁ × p₂^a₂ × ... × pₖ^aₖ. Importanță: calculul cmmdc și cmmmc, teoria numerelor. Algoritmul este sistematic și întotdeauna dă același rezultat. Descompunerea este crucială pentru înțelegerea structurii numerelor.",
            "questions": [
                {"questionNumber": 1, "questionText": "Cum se descompune 12?", "options": ["A. 2 × 6", "B. 2² × 3", "C. 3 × 4", "D. 2 × 2 × 3"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "Care este descompunerea lui 30?", "options": ["A. 2 × 15", "B. 3 × 10", "C. 2 × 3 × 5", "D. 5 × 6"], "correctAnswerIndex": 2},
                {"questionNumber": 3, "questionText": "Ce garantează Teorema Fundamentală?", "options": ["A. Doar un singur prim", "B. Descompunere unică", "C. Numai numere pare", "D. Exponenți egali"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "6",
            "name": "Determinarea celui mai mare divizor comun și a celui mai mic multiplu comun. Numere prime între ele",
            "summary": "cmmdc(a,b) = cel mai mare număr care divide ambele. cmmmc(a,b) = cel mai mic număr care este multiplu al ambelor. Calcul: folosind descompunere în factori primi, cmmdc = produsul factorilor comuni cu exponenți minimi, cmmmc = produsul tuturor factorilor cu exponenți maximi. Identitate: cmmdc(a,b) × cmmmc(a,b) = a × b. Numere prime între ele: cmmdc = 1. Exemplu: cmmdc(12,18) = 2×3 = 6, cmmmc(12,18) = 2²×3² = 36. Aplicații: fracții, probleme practice.",
            "questions": [
                {"questionNumber": 1, "questionText": "Care este cmmdc(12, 18)?", "options": ["A. 2", "B. 3", "C. 6", "D. 36"], "correctAnswerIndex": 2},
                {"questionNumber": 2, "questionText": "Care este cmmmc(4, 6)?", "options": ["A. 2", "B. 12", "C. 24", "D. 8"], "correctAnswerIndex": 1},
                {"questionNumber": 3, "questionText": "Ce sunt numere prime între ele?", "options": ["A. Ambele prime", "B. cmmdc = 1", "C. cmmmc maxim", "D. Ambele impare"], "correctAnswerIndex": 1}
            ]
        },
        {
            "number": "7",
            "name": "Proprietăți ale divizibilității în ℕ",
            "summary": "Proprietăți: Reflexivitate (a | a), Tranzitivitate (a | b și b | c ⇒ a | c), Simetria în egalitate (a | b și b | a ⇒ a = b), Liniaritate (a | b și a | c ⇒ a | b+c și a | b-c). Reguli: a | 0, 1 | a pentru orice a. Dacă a | b atunci a | kb pentru orice k. Dacă a | b și a | c atunci a | (mb + nc) pentru orice m, n. Aceste proprietăți sunt fundamentale pentru teoria numerelor și sunt folosite în demonstrații. Înțelegerea acestora este esențială pentru rezolvarea problemelor de divizibilitate.",
            "questions": [
                {"questionNumber": 1, "questionText": "Este divizibilitatea reflexivă?", "options": ["A. Nu", "B. Da, a | a", "C. Doar pentru numere prime", "D. Depinde de a"], "correctAnswerIndex": 1},
                {"questionNumber": 2, "questionText": "Dacă 2 | 6 și 6 | 12, ce poți spune?", "options": ["A. 2 | 12", "B. 12 | 2", "C. 2 = 12", "D. Nu e relație"], "correctAnswerIndex": 0},
                {"questionNumber": 3, "questionText": "Dacă a | b și a | c, ce poți spune?", "options": ["A. a | (b + c)", "B. b = c", "C. Nu e relație", "D. a > b"], "correctAnswerIndex": 0}
            ]
        }
    ]
}

# Unit 2: Rapoarte, proporții (9 lessons)
unit2_data = {
    "unit_number": "2",
    "unit_name": "Rapoarte, proporții",
    "lessons": [
        {"number": "1", "name": "Rapoarte", "summary": "Raportul a : b = a/b compară două mărimi. De exemplu, raportul dintre băieți și fete. Proprietăți: rapoartele egale se obțin amplificând/simplificând. Raportul kan:kb = a:b. Aplicații: scări pe hărți, procentaje. Interpretare: raportul 3:2 înseamnă că pentru fiecare 3 unități din prima mărime, sunt 2 din a doua. Raporturile sunt fundamentale pentru proporții și proporționalitate. Exemplu: dacă într-o clasă sunt 12 băieți și 8 fete, raportul este 12:8 = 3:2.", "questions": [{"questionNumber": 1, "questionText": "Ce este raportul a:b?", "options": ["A. a + b", "B. a/b", "C. a × b", "D. a - b"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Care este raportul 12:8 simplificat?", "options": ["A. 6:4", "B. 3:2", "C. 4:3", "D. 1:2"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Ce înseamnă raportul 5:3?", "options": ["A. 5 > 3", "B. Pentru 5 unități din A, 3 din B", "C. 5/3 = 1", "D. Sunt egale"], "correctAnswerIndex": 1}]},
        {"number": "2", "name": "Proporții. Proprietatea fundamentală a proporțiilor. Determinarea unui termen necunoscut dintr-o proporție", "summary": "Proporție: egalitate de două rapoarte a/b = c/d. Proprietatea fundamentală: a×d = b×c (produsul extremilor = produsul mezilor). Determinarea necunoscutei: x/4 = 6/8 ⇒ x×8 = 4×6 ⇒ x = 3. Verificare: 3/4 = 6/8 = 0,75. Aplicații practice: scară, viteză, densitate. Proporții directe și inverse. Seria de proporții egale: a/b = c/d = e/f. Proporțiile sunt instrumente puternice în matematică aplicată și științe.", "questions": [{"questionNumber": 1, "questionText": "Ce este proporția?", "options": ["A. Un raport", "B. Egalitate de două rapoarte", "C. O operație", "D. O inegalitate"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Care este proprietatea fundamentală?", "options": ["A. a + d = b + c", "B. a × d = b × c", "C. a × c = b × d", "D. a/d = b/c"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Rezolvă x/5 = 4/10", "options": ["A. x = 2", "B. x = 4", "C. x = 5", "D. x = 10"], "correctAnswerIndex": 0}]},
        {"number": "3", "name": "Proporții derivate", "summary": "Din proporția a/b = c/d, putem obține alte proporții derivate: a/c = b/d (inversarea rapoartelor), (a+b)/b = (c+d)/d (adunare la numărător), (a-b)/b = (c-d)/d (scădere), (a+b)/(a-b) = (c+d)/(c-d) (combinații). Aceste transformări sunt utile pentru rezolvarea problemelor complexe. De exemplu, dacă 2/3 = 4/6, atunci și 2/4 = 3/6. Proporțiile derivate permit flexibilitate în abordare și sunt instrumentale în algebra clasică.", "questions": [{"questionNumber": 1, "questionText": "Dacă a/b = c/d, ce alte proporții sunt adevărate?", "options": ["A. a/c = b/d", "B. a/d = c/b", "C. a = b", "D. c/a = d/b"], "correctAnswerIndex": 0}, {"questionNumber": 2, "questionText": "Ce înseamnă (a+b)/b = (c+d)/d?", "options": ["A. Proporție derivată", "B. Adunare la numărător", "C. Ambele răspunsuri", "D. Nicio relație"], "correctAnswerIndex": 2}, {"questionNumber": 3, "questionText": "Din 3/4 = 6/8, derivă 3/6 = ?", "options": ["A. 4/8", "B. 8/4", "C. 4/3", "D. Imposibil"], "correctAnswerIndex": 0}]},
        {"number": "4", "name": "Șir de rapoarte egale", "summary": "Șir de rapoarte egale: a₁/b₁ = a₂/b₂ = ... = aₙ/bₙ = k (constanta rapoartelor). Proprietate: (a₁ + a₂ + ... + aₙ)/(b₁ + b₂ + ... + bₙ) = k. Exemplu: 2/3 = 4/6 = 6/9 = 2/3. Aplicații: împărțire în raport, probleme cu proporții. Dacă 2/3 = 4/6 = 6/9, atunci (2+4+6)/(3+6+9) = 12/18 = 2/3. Șirurile de rapoarte sunt importante în proporționalitate și în probleme practice de distribuție.", "questions": [{"questionNumber": 1, "questionText": "Ce este constanta rapoartelor?", "options": ["A. Suma rapoartelor", "B. Valoarea comună a/b", "C. Produsul rapoartelor", "D. Diferența"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Dacă a/b = c/d = e/f = k, atunci?", "options": ["A. (a+c+e)/(b+d+f) ≠ k", "B. (a+c+e)/(b+d+f) = k", "C. a + b = c + d", "D. Nu e relație"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Care e constanta pentru 3/2 = 6/4 = 9/6?", "options": ["A. 2", "B. 3/2", "C. 4", "D. 1.5"], "correctAnswerIndex": 1}]},
        {"number": "5", "name": "Mărimi direct proporționale", "summary": "Mărimi direct proporționale: dacă una se multiplică cu k, cealaltă se multiplică cu k. Notație: y = kx (k = constanta proporționalității). Graficul este o linie dreaptă prin origine. Exemplu: distanță = viteză × timp. Dacă mergem dublu mai repede, distanța parcursă în timp fix se dublează. Aplicații: scară, viteză constantă, preț. Proporționalitatea directă este unul din cele mai importante concepte în matematică aplicată. Raportul y/x rămâne constant.", "questions": [{"questionNumber": 1, "questionText": "Ce sunt mărimi direct proporționale?", "options": ["A. Mereu egale", "B. y = kx, raportul constant", "C. Mereu crescătoare", "D. Opuse"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Dacă y = 2x și x se dublează, ce se întâmplă cu y?", "options": ["A. Se dublează", "B. Se înjumătățește", "C. Rămâne aceeași", "D. Se ridică la pătrat"], "correctAnswerIndex": 0}, {"questionNumber": 3, "questionText": "Care este graficul proporționalității directe?", "options": ["A. Parabolă", "B. Linie dreaptă prin origine", "C. Cerc", "D. Hiperbolă"], "correctAnswerIndex": 1}]},
        {"number": "6", "name": "Mărimi invers proporționale", "summary": "Mărimi invers proporționale: dacă una se multiplică cu k, cealaltă se împarte la k. Notație: y = k/x sau xy = k. Graficul este o hiperbolă. Exemplu: timp = distanță/viteză; viteza dublată = timp înjumătățit. Produsul xy rămâne constant. Aplicații: lucru și timp, presiune și volum. Diferență cu proporționalitate directă: aici graficul nu trece prin origine și nu e liniar. Proporționalitatea inversă este esențială pentru înțelegerea relațiilor inverse în fizică și economie.", "questions": [{"questionNumber": 1, "questionText": "Ce sunt mărimi invers proporționale?", "options": ["A. y = kx", "B. y = k/x, produsul constant", "C. Mereu negative", "D. Opuse"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Dacă xy = 6 și x se dublează, ce se întâmplă cu y?", "options": ["A. Se dublează", "B. Se înjumătățește", "C. Rămâne aceeași", "D. Se ridică la pătrat"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Care este graficul proporționalității inverse?", "options": ["A. Linie dreaptă", "B. Parabolă", "C. Hiperbolă", "D. Cerc"], "correctAnswerIndex": 2}]},
        {"number": "7", "name": "Regula de trei simplă", "summary": "Regula de trei simplă: dacă a mărimi corespund b unități din a doua mărime, câte unități din a doua mărime corespund c unități din prima? Soluție: x = (b × c)/a. Pentru proporționalitate directă și inversă. Exemplu direct: dacă 3 kg costă 6 lei, 5 kg costă (5 × 6)/3 = 10 lei. Exemplu invers: dacă la viteză 60 km/h durează 2 ore, la viteză 40 km/h durează (60 × 2)/40 = 3 ore. Regula de trei este instrument practic și intuitiv pentru rezolvarea problemelor zilnice.", "questions": [{"questionNumber": 1, "questionText": "Dacă 2 kg costă 8 lei, cât costă 5 kg?", "options": ["A. 16 lei", "B. 20 lei", "C. 10 lei", "D. 24 lei"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Dacă 4 muncitori termină în 6 zile, 3 muncitori termină în?", "options": ["A. 4 zile", "B. 8 zile", "C. 6 zile", "D. 9 zile"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Ce determină tipul: directă sau inversă?", "options": ["A. Numerele", "B. Relația dintre mărimi", "C. Ordinea", "D. Semnele"], "correctAnswerIndex": 1}]},
        {"number": "8", "name": "Elemente de organizare a datelor. Reprezentarea datelor prin grafice în contextul proporționalității. Reprezentarea datelor cu ajutorul unor softuri matematice", "summary": "Organizarea datelor: tabele, liste, frecvență. Reprezentări grafice: diagrame cu bare, histograme, grafice liniare, diagrame circulare. În context proporționalitate: grafice care arată relații directe/inverse. Software: GeoGebra, Excel, Python matplotlib. Graficele liniare pentru proporționalitate directă, hiperbolice pentru inversă. Alegerea reprezentării depinde de tip de date și scop. Competențe digitale sunt importante în matematică modernă. Interpretarea graficelor ajută la înțelegerea datelor și a relațiilor dintre mărimi.", "questions": [{"questionNumber": 1, "questionText": "Ce tip de grafic pentru proporționalitate directă?", "options": ["A. Linie dreaptă prin origine", "B. Hiperbolă", "C. Parabolă", "D. Cerc"], "correctAnswerIndex": 0}, {"questionNumber": 2, "questionText": "Care sunt reprezentări date?", "options": ["A. Doar tabele", "B. Tabele, grafice, diagrame", "C. Doar numere", "D. Doar cuvinte"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "De ce folosim software?", "options": ["A. Pentru divertisment", "B. Pentru construire și analiză grafice", "C. Sunt obligatorii", "D. Nu sunt utile"], "correctAnswerIndex": 1}]},
        {"number": "9", "name": "Probabilități", "summary": "Probabilitate = șanse ca un eveniment să se întâmple. P(E) = (cazuri favorabile)/(cazuri totale). P(E) ∈ [0, 1]. P(E) = 0 = eveniment imposibil. P(E) = 1 = eveniment sigur. Exemple: P(cap la monedă) = 1/2, P(6 la zar) = 1/6. Evenimente: sigure, imposibile, aleatorii. Reguli: P(E) + P(¬E) = 1 (complementar). Aplicații: statistică, decizii, jocuri. Probabilitatea introduceți incertitudinea în matematică de manieră riguroasă. Este fundamentală pentru statistică și aplicații practice.", "questions": [{"questionNumber": 1, "questionText": "Ce este probabilitatea?", "options": ["A. Certitudine", "B. Șanse ca eveniment să se întâmple", "C. Imposibilitate", "D. Raritate"], "correctAnswerIndex": 1}, {"questionNumber": 2, "questionText": "Care e P(cap la monedă)?", "options": ["A. 0", "B. 1/2", "C. 1", "D. Imposibil"], "correctAnswerIndex": 1}, {"questionNumber": 3, "questionText": "Dacă P(E) = 0.3, cât e P(¬E)?", "options": ["A. 0.3", "B. 0.7", "C. 1.3", "D. 0"], "correctAnswerIndex": 1}]}
    ]
}

# Save all units
for unit_data, filename in [
    (unit1_data, "clasa6_math_unit1_complete.json"),
    (unit2_data, "clasa6_math_unit2_complete.json")
]:
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(unit_data, f, ensure_ascii=False, indent=2)
    print(f"✓ {filename}: {len(unit_data['lessons'])} lessons, {sum(len(l['questions']) for l in unit_data['lessons'])} questions")

