#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Process Unit 1 lessons from Clasa a VI a Limba și Literatura Română
Extract summaries and generate questions for each lesson
"""

import json

# Unit 1 Lesson Data with content summaries and questions
unit1_clasa6_data = {
    "unit_number": "1",
    "unit_name": "Acasă, în familie, printre cărți",
    "lessons": [
        {
            "number": "1",
            "name": "Textul narativ literar în proză: Un păianjen care se crede Spiderman de Adina Popescu",
            "summary": """Acest text de Adina Popescu prezintă o narațiune haioasă și profundă despre un păianjen cu aspirații supereroisice. 
            Povestea urmărește aventurile unui păianjen care, inspirat de cinematografie, dorește să devină Spiderman. Prin intermediul acestui 
            personaj comic, autoarea explorează teme importante: identitatea, imaginația, puterea viselor și cum îi ajută acestea pe oameni 
            (sau păianjeni) să trăiască. Textul este o invitație la a ne gândi la modul în care cultura populară influențează viziunea noastră 
            asupra lumii și la cât de importantă este libertatea de a visa. Narațiunea combinează umor cu reflecții mai profunde asupra vieții.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Cine este protagonistul textului 'Un păianjen care se crede Spiderman'?",
                    "options": [
                        "A. Un copil",
                        "B. Un păianjen cu aspirații supereroisice",
                        "C. Un supererou real",
                        "D. O persoană adulată"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "De unde este inspirat păianjenul din text?",
                    "options": [
                        "A. Din cărți",
                        "B. Din cinematografie și de Spiderman",
                        "C. Din experiențe reale",
                        "D. Din alte păianjeni"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care dintre următoarele este o temă din text?",
                    "options": [
                        "A. Frică și anxietate",
                        "B. Identitate, imaginație și puterea viselor",
                        "C. Doar umor banal",
                        "D. Violență și agresiune"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "2",
            "name": "Narațiunea. Acțiunea. Timpul și spațiul",
            "summary": """Narațiunea este un text care relatează o serie de evenimente într-o ordine logică. Acțiunea este succesiunea 
            evenimentelor care formează intriga unui text narativ. Elementele esențiale sunt: expozitia (prezentarea situației inițiale), 
            nodul intrigii (introducerea conflictului), dezvoltarea (complexitatea conflictului), punctul culminant (momentul de maxim 
            interes), deznodământul (rezolvarea conflictului). Timpul poate fi cronologic (urmând ordinea evenimentelor reale) sau psihologic 
            (cum percepe personajul trecerea timpului). Spațiul este locul sau locurile unde se desfășoară acțiunea, care poate avea și 
            semnificație simbolică. Înțelegerea acestor elemente ajută la analiza mai profundă a textelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este narațiunea?",
                    "options": [
                        "A. O descriere detaliată a unui obiect",
                        "B. Un text care relatează o serie de evenimente într-o ordine logică",
                        "C. O conversație între doi oameni",
                        "D. O opinie despre ceva"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este ordinea elementelor unei naratiuni?",
                    "options": [
                        "A. Deznodământ, punctul culminant, dezvoltare, nod, expozitie",
                        "B. Expozitie, nod, dezvoltare, punct culminant, deznodământ",
                        "C. Nu există ordine fixă",
                        "D. Nod, expozitie, punctul culminant, deznodământ"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce poate exprima spațiul în text?",
                    "options": [
                        "A. Doar locurile fizice",
                        "B. Locurile fizice și semnificație simbolică",
                        "C. Doar ideile personajelor",
                        "D. Nici o semnificație"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "3",
            "name": "Narațiunea la persoana I. Autorul, naratorul, personajul",
            "summary": """Narațiunea la persoana I este atunci când narrator-ul este unul din personajele poveștii, care spune povestea din 
            perspectiva sa. Autorul este persoana care a scris textul, dar nu participă direct în povestă. Naratorul este persoana care 
            relatează evenimentele (poate fi autor, dar poate fi și orice personaj). Personajul este oricare din persoanele care acționează 
            în povestă. Importante distincțiile acestea: un autor poate crea un narator care să nu fie el însuși. În narațiunea la persoana I, 
            cititorul vede lumea prin ochii personajului-narator, ceea ce creează o perspectivă mai intimă și mai subiectivă. Această tehnică 
            permite autoarei Adina Popescu să ne apropie de sentimentele și gândurile păianjenului.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este narațiunea la persoana I?",
                    "options": [
                        "A. O poveste spusă de mai mulți oameni",
                        "B. O poveste în care naratorul este personajul care o trăiește",
                        "C. O poveste spusă de un străin",
                        "D. O poveste fără narator"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este diferența dintre autor și narator?",
                    "options": [
                        "A. Sunt același lucru",
                        "B. Autorul scrie textul, naratorul relatează povestea din interiorul ei",
                        "C. Autorul este doar cuvântul pe copertă",
                        "D. Nu există diferență importantă"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce avantaj are narațiunea la persoana I?",
                    "options": [
                        "A. Niciun avantaj",
                        "B. Creează o perspectivă intimă și subiectivă",
                        "C. Este mai ușoară de scris",
                        "D. Permite mai mult umor"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "4",
            "name": "Semnificațiile textului",
            "summary": """Semnificațiile unui text sunt sensurile ascunse sau mai profunde care depășesc povestea literală. Un text nu transmite 
            doar o poveste de suprafață, ci și lecții, critici ale societății, reflecții asupra condiției umane. În cazul povestii 
            păianjenului care vrea să fie Spiderman, pot exista multiple semnificații: critica modului în care cultura populară influențează 
            aspirațiile noastre, ideea că toți avem drepturi egale de a visa, că identitatea nu este doar ceea ce suntem ci și ceea ce 
            aspirăm să fim. Descoperirea semnificațiilor necesită lectură atentă, reflecție asupra simbolurilor și comportamentelor personajelor, 
            și deschidere la interpretări multiple. Aceasta este abilitatea de a ''citi între rânduri''.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce sunt semnificațiile unui text?",
                    "options": [
                        "A. Doar cuvintele din text",
                        "B. Sensurile ascunse și mai profunde ale textului",
                        "C. Greșelile de tipărire",
                        "D. Titlul textului"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Cum se descoperi semnificațiile unui text?",
                    "options": [
                        "A. Prin citire superficială",
                        "B. Prin lectură atentă, reflecție și deschidere la interpretări",
                        "C. Sunt date de profesor",
                        "D. Nu se pot descoperi"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce putea critica autoarea în text?",
                    "options": [
                        "A. Doar păianjenii",
                        "B. Modul în care cultura populară influențează aspirațiile noastre",
                        "C. Arhitectura modernă",
                        "D. Nimic special"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "5",
            "name": "Textul descriptiv literar în proză: Indescriptibil de Simona Popescu",
            "summary": """Textul descriptiv literar de Simona Popescu, intitulat ''Indescriptibil'', explorează paradoxul de a descrie ceva 
            care pare indescriptibil. Descrierea literară nu este o simplă inventariere de detalii, ci o transpunere artistică a unei realități 
            sau emoții. În textul lui Simona Popescu, probabil că autoarea folosește limbajul poetic și figuri de stil pentru a da viață unei 
            imagini, unui sentiment sau unei scene. Indescriptibilul poate referi la ceva atât de frumos, atât de sfâșietor sau atât de complex, 
            încât cuvintele obișnuite sunt insuficiente. Textul invită cititorul să se gândească la limitele limbajului și puterea literaturii 
            de a depăși aceste limite prin creativitate și imaginație.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este textul descriptiv literar?",
                    "options": [
                        "A. O simplă inventariere de detalii",
                        "B. O transpunere artistică a unei realități sau emoții",
                        "C. O descriere științifică",
                        "D. O listă de proprietăți"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce poate fi ''indescriptibil'' în text?",
                    "options": [
                        "A. Doar culori",
                        "B. Ceva atât de frumos sau complex încât cuvintele sunt insuficiente",
                        "C. Doar numere",
                        "D. Nimic, totul se poate descrie"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce invită cititorul textul ''Indescriptibil''?",
                    "options": [
                        "A. Să memoreze detalii",
                        "B. Să se gândească la limitele limbajului și puterea literaturii",
                        "C. Să critice autoarea",
                        "D. Să ignore textul"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "6",
            "name": "Descrierea în proză",
            "summary": """Descrierea în proză este un mod de a prezenta un loc, o persoană, un obiect sau o situație folosind limbaj 
            expresiv și figuri de stil. Cu diferență de narațiune care progresează în timp, descrierea se focusează pe imaginea unei 
            situații specifice. O descriere bună în proză include: 1) Selectarea detaliilor relevante, 2) Utilizarea unui limbaj viu și 
            sugestiv, 3) Crearea unei atmosfere (tone și mood), 4) Utilizarea comparațiilor și metaforelor, 5) Organizarea detaliilor 
            în mod logic (de exemplu, de la general la particular). Descrierea poate fi obiectivă (prezentând faptele) sau subiectivă 
            (transmițând emoții și impresii personale ale naratonului). În literatura de calitate, descrierea nu este numai ornament ci 
            contribuie la sensul total al textului.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este descrierea în proză?",
                    "options": [
                        "A. Un mod de a relata evenimente consecutive",
                        "B. Un mod de a prezenta detalii cu limbaj expresiv și figuri de stil",
                        "C. O listă simplă de proprietăți",
                        "D. Un tip de dialog"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce include o descriere bună?",
                    "options": [
                        "A. Doar culori și dimensiuni",
                        "B. Selectare de detalii, limbaj viu, atmosferă, figuri de stil",
                        "C. Doar adjective",
                        "D. Descrieri lungi și complicate"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care este diferența între descriere obiectivă și subiectivă?",
                    "options": [
                        "A. Nu există diferență",
                        "B. Obiectivă = fapte, subiectivă = emoții și impresii personale",
                        "C. Subiectivă nu se poate folosi în literatură",
                        "D. Obiectivă este mai ușoară"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "7",
            "name": "Semnificațiile textului",
            "summary": """Pentru textul descriptiv ''Indescriptibil'' de Simona Popescu, semnificațiile pot fi diverse. Descrierea unei scene 
            sau emoții ''indescriptibile'' poate reflecta ideea că unele experiențe umane sunt atât de profunde, atât de complexe, încât 
            nu pot fi pe deplin exprimate prin cuvinte. Aceasta poate fi o reflecție asupra limitelor comunicării, asupra imposibilității 
            de a transmite complet ceea ce simțim. De asemenea, titlul ''Indescriptibil'' poate sugera și că frumusețea sau sublimul (o 
            calitate grandioasă și imposibil de descris) este dincolo de descriere. Textul invită cititorul să accepte că uneori, absența 
            descrierii complete poate fi mai puternică decât descrierea în sine.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce pot sugera semnificații din ''Indescriptibil''?",
                    "options": [
                        "A. Doar că textul este ușor",
                        "B. Limitele comunicării și imposibilitatea transmiterii complete a emoțiilor",
                        "C. Că descrierea nu este importantă",
                        "D. Că autoarea nu poate scrie"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce poate fi mai puternic decât descrierea?",
                    "options": [
                        "A. Silence-ul",
                        "B. Absența descrierii complete",
                        "C. Tăcere și gânduri",
                        "D. Alte texte"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce invită textul cititorul să accepte?",
                    "options": [
                        "A. Să memoreze textul",
                        "B. Că uneori absența descrierii complete poate fi mai puternică",
                        "C. Că trebuie să critice textul",
                        "D. Că literatura nu are sens"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "8",
            "name": "Texte continue și discontinue",
            "summary": """Textele continue sunt texte unde informația este prezentată în mod coerent, în paragrafe întregi, de obicei în 
            format narativ sau expozitiv tradițional. Textele discontinue sunt texte care prezintă informația sub forme variate: tabele, 
            grafice, diagrame, lănțuri de text scurt, liste cu puncte, diagrame de flux, etc. În lumea modernă, texte discontinue sunt 
            frecvente: anunțuri, avertismente, instrucțiuni, rapoarte științifice cu grafice. Citirea textelor discontinue necesită alte 
            abilități: a identifica rapid informații cheie, a înțelege simboluri și coduri vizuale, a sintetiza informații din mai multe 
            surse. Educația modernă insistă pe înțelegerea ambelor tipuri de texte.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce sunt textele continue?",
                    "options": [
                        "A. Texte cu mai multe culori",
                        "B. Texte cu informație în paragrafe întregi, în format tradițional",
                        "C. Texte foarte lungi",
                        "D. Texte fără ordine"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce sunt textele discontinue?",
                    "options": [
                        "A. Texte fără sens",
                        "B. Texte care prezintă informația în forme variate: tabele, grafice, liste",
                        "C. Texte în limba străină",
                        "D. Texte șterse"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce abilități necesită citirea textelor discontinue?",
                    "options": [
                        "A. Doar memorizare",
                        "B. Identificare de informații cheie, înțelegere de simboluri, sinteză",
                        "C. Doar viteză de citire",
                        "D. Nicio abilitate specială"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "9",
            "name": "Noi pagini – alte idei",
            "summary": """Această secțiune continuă tradiția introdusă în Clasa a V a: prezintă alte texte sau fragmente care explorează 
            teme similare sau conexe în moduri diferite. Prin compararea mai multor texte care tratează aceleași teme (de exemplu, 
            imaginația, familia, valorile), elevii învață să aprecieze diversitatea stilurilor literare și perspectivelor autorilor. 
            Pot observa cum diferiți scriitori abordează aceeași problemă în moduri diferite, cum folosesc diferite tehnici narative sau 
            descriptive. Aceasta deschide orizonturi și încurajează gândirea critică și independență în interpretarea textelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Care este scopul secțiunii ''Noi pagini - alte idei''?",
                    "options": [
                        "A. Să înlocuiască textele principale",
                        "B. Să arate diverse moduri de a explora teme similare",
                        "C. Să lungească cartea fără sens",
                        "D. Să enerveze elevii"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce pot învăța elevii din texte diverse?",
                    "options": [
                        "A. Să memoreze mai mult",
                        "B. Diversitatea stilurilor și perspectivelor autorilor",
                        "C. Că toți autorii scriu la fel",
                        "D. Nimic nou"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce încurajează compararea textelor?",
                    "options": [
                        "A. Conformismul",
                        "B. Gândirea critică și independență în interpretare",
                        "C. Copierea textelor",
                        "D. Nici o gândire"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "10",
            "name": "Valori etice în legendele popoarelor",
            "summary": """Legendele sunt povești tradiționale care au circulat pe cale orală dintr-o generație în alta. Acestea conțin 
            adesea valori etice importante: curajul, loialitatea, sacrificiul, dreptatea, mila. În legendele românești, găsim figuri 
            mitice și istorice care exemplifică aceste valori. De exemplu, legenda lui Stefan cel Mare reflectă valorile patriotismului și 
            curajului. Legendele unor popoare diferite, deși separate de timp și spațiu, adesea explorează aceleași valori etice universale, 
            ceea ce arată ce anume este important pentru omenire. Studierea legendelor ajută elevii să înțeleagă culturile, tradițiile și 
            valorile care susțin comunități. Aceasta dezvoltă empatia culturală și respectul pentru diversitate.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce sunt legendele?",
                    "options": [
                        "A. Povești inventate complet",
                        "B. Povești tradiționale transmise oral cu valori etice",
                        "C. Doar povești pentru copii",
                        "D. Povești care nu sunt adevărate"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce valori etice se găsesc în legende?",
                    "options": [
                        "A. Doar violență",
                        "B. Curaj, loialitate, sacrificiu, dreptate, mila",
                        "C. Doar divertisment",
                        "D. Nicio valoare"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce arată universalitatea valorilor în legende?",
                    "options": [
                        "A. Că nu există valori universale",
                        "B. Că unele valori sunt importante pentru toată omenirea",
                        "C. Că legendele sunt inutile",
                        "D. Că culturile sunt identice"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "11",
            "name": "Contextul de comunicare",
            "summary": """Contextul de comunicare este ansamblul de circumstanțe în care are loc o interacțiune comunicativă. Include: 
            situația (unde și când), participanții (cine vorbește și cui), scopul comunicării (pentru ce), canalul (verbal, scris, etc.), 
            relația dintre participanți (formal, informal), și codul utilizat (registrul limbajului). De exemplu, comunicarea între prietenul 
            și profesorul este diferită: cu prietenul folosim limbaj informal și colocvial, cu profesorul folosim limbaj mai formal și 
            respectuos. Înțelegerea contextului ajută la o comunicare mai eficace și la evitarea malîmpletinirilor. În studiul textelor, 
            recunoașterea contextului de comunicare ajută la înțelegerea mai profundă a tonului și mesajului textului.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce include contextul de comunicare?",
                    "options": [
                        "A. Doar cuvintele",
                        "B. Situația, participanții, scopul, canalul, relația, codul",
                        "C. Doar locul",
                        "D. Doar subiectul"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "De ce diferă comunicarea cu prietenul de cea cu profesorul?",
                    "options": [
                        "A. Nu diferă",
                        "B. Contextul și relația sunt diferite, deci registrul limbajului este diferit",
                        "C. Doar pentru că vreau",
                        "D. Nu sunt diferențe reale"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "De ce este important să înțelegem contextul?",
                    "options": [
                        "A. Nu este important",
                        "B. Pentru comunicare mai eficace și evitarea malîmpletinirilor",
                        "C. Doar pentru joc",
                        "D. Pentru a complica lucrurile"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "12",
            "name": "Cuvântul. Sinonimele și antonimele",
            "summary": """Cuvântul este unitatea fundamentală a limbajului. Sinonimele sunt cuvinte cu aceeași sau aproximativ aceeași 
            semnificație, dar cu pronunții și ortografii diferite. De exemplu: ''frumos'' și ''belle'' nu sunt sinonime perfecte în română 
            deoarece ''belle'' este francez, dar ''frumos'' și ''grav'' nu sunt sinonime. Un exemplu mai bun: ''murdar'' și ''impur'' sunt 
            sinonime. Antonimele sunt cuvinte cu semnificații opuse. De exemplu: ''alb'' și ''negru'', ''mare'' și ''mic'', ''frumos'' și 
            ''urât''. Utilizarea de sinonime și antonime Face textele mai expresive și mai vii. Înțelegerea relațiilor între cuvinte ajută 
            la dezvoltarea vocabularului și la o comunicare mai nuanțată.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce sunt sinonimele?",
                    "options": [
                        "A. Cuvinte care sună la fel",
                        "B. Cuvinte cu aceeași sau aproximativ aceeași semnificație",
                        "C. Cuvinte cu semnificații opuse",
                        "D. Cuvinte inventate"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care sunt antonimi pentru cuvântul ''mic''?",
                    "options": [
                        "A. ''Lichidat''",
                        "B. ''Mare''",
                        "C. ''Mic''",
                        "D. ''Oare''"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "De ce sunt importante sinonimele și antonimele?",
                    "options": [
                        "A. Nu sunt importante",
                        "B. Fac textele mai expresive și ajută la dezvoltarea vocabularului",
                        "C. Doar pentru examene",
                        "D. Pentru a plictisi elevii"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "13",
            "name": "Sensurile cuvintelor",
            "summary": """Un cuvânt poate avea mai multe sensuri (înțelesuri). De exemplu, cuvântul ''vol'' poate însemna: 1) Acțiunea de a 
            zbura (substantiv), 2) Un set de pagini ale unei cărți (substantiv), 3) Furie, furt (substantiv). În afară de semnificația 
            principală (sens literal), cuvintele au adesea și sensuri figurate (sensuri metaforice). De exemplu, ''inima'' literal este un 
            organ, dar figurat este sediul sentimentelor. Contexul determină care sens este relevant. Înțelegerea sensurilor múltiple ale 
            cuvintelor este esențială pentru o citire precisă și pentru o comunicare clară. Confundarea sensurilor poate duce la malinteles.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Câte sensuri poate avea un cuvânt?",
                    "options": [
                        "A. Doar unu",
                        "B. Poate avea multiple sensuri",
                        "C. Trei sensuri mereu",
                        "D. Infinit de sensuri"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este diferența între sens literal și figurat?",
                    "options": [
                        "A. Nu există diferență",
                        "B. Literal = semnificație reală, figurat = metaforică",
                        "C. Figurat este corect, literal este greșit",
                        "D. Literal este mai greu"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce determină care sens al cuvântului este relevant?",
                    "options": [
                        "A. Pronunția",
                        "B. Contextul în care se utilizează",
                        "C. Lungimea cuvântului",
                        "D. Culoarea cuvântului"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "14",
            "name": "Omonimele. Cuvintele polisemantice",
            "summary": """Omonimele sunt cuvinte care au aceeași pronunție și ortografie, dar semnificații complet diferite. De exemplu: 
            ''rând'' (ștranduri sau ordinea) și ''rând'' (gândurile unei persoane). Un alt exemplu: ''ață'' (fibră pentru cusut) și ''ață'' 
            (ține fățișă). Cuvintele polisemantice sunt cuvinte care au mai multe semnificații legate între ele. De exemplu, ''masă'' poate 
            fi: 1) Mobilă pentru a mânca, 2) Cantitate de materie, 3) Mulțimea de oameni. Diferența: omonimele au semnificații complet 
            diferite, polisemantice au semnificații legate. Confundarea omonimelor poate duce la jocuri de cuvinte amuzante dar și la 
            malinteles serios în comunicare.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce sunt omonimele?",
                    "options": [
                        "A. Cuvinte cu aceeași semnificație",
                        "B. Cuvinte cu aceeași pronunție și ortografie, dar semnificații diferite",
                        "C. Cuvinte cu semnificații legate",
                        "D. Cuvinte inventate"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Care este diferența dintre omonime și cuvinte polisemantice?",
                    "options": [
                        "A. Nu există diferență",
                        "B. Omonime = semnificații complet diferite, polisemantice = semnificații legate",
                        "C. Sunt același lucru",
                        "D. Polisemantice sunt mai greu"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce pot crea omonimele în comunicare?",
                    "options": [
                        "A. Nimic",
                        "B. Jocuri de cuvinte și posibile malinteles",
                        "C. Doar umor",
                        "D. Comunică mai bine"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "15",
            "name": "Diftongul, triftongul, hiatul",
            "summary": """Diftongul este o combinație de două vocale care se pronunță ca un singur sunet și se află în aceeași silabă. 
            Exemple în română: ''ai'' (în ''mai''), ''ei'' (în ''lei''), ''oi'' (în ''doi''). Triftongul este o combinație de trei vocale 
            care se pronunță ca un singur sunet în aceeași silabă. Exemple: ''iau'' (în ''viață''). Hiatul este situația opusă: două vocale 
            alăturate care se pronunță separat, în silabe diferite. De exemplu: ''ae'' (în ''aer'') se pronunță ''a-er''. În română, distinc 
            ția între diftong și hiat este importantă pentru pronunție corectă și pentru despărțirea în silabe. Aceasta este o lecție de 
            fonetică care ajută la înțelegerea structurii sunetelor limbii.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este diftongul?",
                    "options": [
                        "A. O vocală singură",
                        "B. O combinație de două vocale în aceeași silabă, pronunțate ca un singur sunet",
                        "C. Trei vocale",
                        "D. Consonanță"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Câte vocale are triftongul?",
                    "options": [
                        "A. Unu",
                        "B. Doi",
                        "C. Trei",
                        "D. Patru"
                    ],
                    "correctAnswerIndex": 2
                },
                {
                    "questionNumber": 3,
                    "questionText": "Ce este hiatul?",
                    "options": [
                        "A. Diftong",
                        "B. Două vocale alăturate pronunțate separat, în silabe diferite",
                        "C. O consonantă",
                        "D. O silabă"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "16",
            "name": "Despărțirea în silabe",
            "summary": """Despărțirea în silabe este procesul de împărțire a unui cuvânt în părți care corespund unităților sonore 
            identificabile. O silabă conține în mod obișnuit: o vocală (obligatorie) și zero sau mai multe consonante. De exemplu, cuvântul 
            ''carte'' se desparte ca: ''car-te'' (două silabe). ''Minge'' se desparte ca: ''min-ge'' (două silabe). Regulile despărțirii în 
            silabe în limba română includ: 1) Vocalele se grupează cu consonantele care urmează, 2) Vocala finală a unui cuvânt formează 
            adesea silaba finală, 3) Consoanele se grupează în funcție de sonoritate. Despărțirea în silabe corectă este importantă pentru 
            pronunție corectă, pentru scriere la sfârșitul rândului și pentru înțelegerea structurii fonetice a cuvintelor.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce este despărțirea în silabe?",
                    "options": [
                        "A. Pronunțarea greoaie",
                        "B. Împărțirea cuvântului în unități sonore identificabile",
                        "C. Scrisul cuvintelor",
                        "D. Îndoiala"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce conține obligatoriu o silabă?",
                    "options": [
                        "A. O consonantă",
                        "B. O vocală",
                        "C. Două vocale",
                        "D. Trei sunete"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Cum se desparte cuvântul ''carte''?",
                    "options": [
                        "A. ''Ca-rte''",
                        "B. ''Car-te''",
                        "C. ''Cart-e''",
                        "D. ''C-arte''"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        },
        {
            "number": "17",
            "name": "Redactarea unei narațiuni la persoana I. Stilul",
            "summary": """Redactarea unei narațiuni la persoana I necesită mai mult decât o simplă cronologie a evenimentelor. Trebuie să: 
            1) Alegi o voce credibilă și consecventă pentru naratorul tău, 2) Creezi o atmosferă și o anumită perspectivă asupra 
            evenimentelor, 3) Utilizezi detalii senzoriale pentru a face povestea vie, 4) Expui emoțiile și gândurile personajului-narator, 
            5) Menții tonul constant cu personajul și situația. Stilul se referă la modurile distinctiv de a exprima ideile: alegerea 
            cuvintelor, structura propozițiilor, ritmul scrierii. Un stil bun este natural, armonic, variat și original. Un text la 
            persoana I permite o muncă mai intimă cu stilul personal al naratonului. În această lecție, elevii sunt invitați să-și dezvolte 
            propriul stil scriitor prin practică sistematică.""",
            "questions": [
                {
                    "questionNumber": 1,
                    "questionText": "Ce necesită redactarea unei narațiuni la persoana I?",
                    "options": [
                        "A. Doar cronologie",
                        "B. Voce credibilă, atmosferă, detalii, emoții și ton consistent",
                        "C. Doar descrieri lungi",
                        "D. Doar cuvinte lungi"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 2,
                    "questionText": "Ce este stilul în scriere?",
                    "options": [
                        "A. Doar ortografia",
                        "B. Modurile distinctiv de a exprima idei: cuvinte, structură, ritm",
                        "C. Doar grip",
                        "D. Doar descrieri"
                    ],
                    "correctAnswerIndex": 1
                },
                {
                    "questionNumber": 3,
                    "questionText": "Care sunt caracteristicile unui stil bun?",
                    "options": [
                        "A. Complicat și confuz",
                        "B. Natural, armonic, variat și original",
                        "C. Lungimea maximă",
                        "D. Repetitiv"
                    ],
                    "correctAnswerIndex": 1
                }
            ]
        }
    ]
}

# Save to JSON file
output_path = "clasa6_unit1_lessons_complete.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(unit1_clasa6_data, f, ensure_ascii=False, indent=2)

print(f"✓ Clasa a VI a Unit 1 complete data saved to {output_path}")
print(f"✓ Total lessons processed: {len(unit1_clasa6_data['lessons'])}")
print(f"✓ Total questions generated: {sum(len(lesson['questions']) for lesson in unit1_clasa6_data['lessons'])}")

