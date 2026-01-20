# EduPex Lesson Format Specification v1.0
**Last Updated:** January 20, 2026
**Status:** Production Ready ✅
**Total Lessons:** 108 (51 Matematica + 57 Limba Română)
---
## 📋 Table of Contents
1. [Lesson Structure](#lesson-structure)
2. [Content Format](#content-format)
3. [Questions Format](#questions-format)
4. [Database Schema](#database-schema)
5. [Examples](#examples)
6. [Quality Standards](#quality-standards)
---
## Lesson Structure
Every lesson consists of:
```
┌─ Lesson
├─ Metadata
│  ├─ Title (e.g., "L1 - Lecția 1")
│  ├─ Summary (lesson topic)
│  ├─ Subject (Matematica or Limba Română)
│  ├─ Grade (Class V-VIII)
│  └─ Unit & Chapter (organization)
│
├─ Educational Content
│  ├─ Theory (200-600 characters of explanation)
│  ├─ Examples (1-4 practical examples)
│  └─ Tips (2-4 learning tips/advice)
│
└─ Assessment
   └─ Question (lesson-specific quiz question)
      ├─ Question Text
      ├─ 4 Multiple Choice Options
      │  ├─ 1 Correct Answer with explanation
      │  └─ 3 Incorrect Answers with explanations
```
---
## Content Format
### Theory Section
- **Purpose:** Explain the main concept
- **Length:** 200-600 characters
- **Format:** Clear, educational explanation with key concepts
- **Style:** Romanian language, appropriate for 5th-8th grade
**Example (Matematica):**
```
Reprezentarea numerelor pe o dreaptă numerică:
- Pe o axă numerică orizontală, numerele cresc de la stânga la dreapta
- Fiecare punct corespunde unui număr natural
- Distanțele între puncte sunt egale
```
**Example (Limba Română):**
```
Comunicarea este schimbul de mesaje între persoane pentru a transmite idei, sentimente și informații. 
ELEMENTELE COMUNICĂRII: 1. Emițător (vorbitor/autor) 2. Receptor (ascultător/cititor) 3. Mesaj 
4. Canal (cale de transmitere) 5. Context
```
### Examples Section
- **Purpose:** Show practical application of theory
- **Count:** 1-4 examples per lesson
- **Format:** Array of strings, each showing a concrete example
- **Style:** Progressive difficulty from simple to complex
**Example (Matematica):**
```
[
  "Comparare: 15 < 20 (15 este mai mic decât 20)",
  "Pe axa numerelor: 0---1---2---3---4---5",
  "Rotunjire: 347 rotunjit la sute este 300",
  "Ordine crescătoare: 5, 12, 23, 45, 67"
]
```
**Example (Limba Română):**
```
[
  "Comunicare verbală: o conversație între doi prieteni",
  "Comunicare non-verbală: gesturile pe care le facem",
  "Comunicare scrisă: un mesaj trimis prin e-mail",
  "Comunicare digitală: un mesaj pe o rețea de socializare"
]
```
### Tips Section
- **Purpose:** Help students remember and apply concepts
- **Count:** 2-4 tips per lesson
- **Format:** Array of practical advice
- **Style:** Encouraging, practical, memorable
**Example (Matematica):**
```
[
  "Pe axa, mai la dreapta = mai mare",
  "La rotunjire, uită-te la cifra din dreapta",
  "Dacă cifra este ≥ 5, rotunjești în sus",
  "Dacă cifra este < 5, rotunjești în jos"
]
```
**Example (Limba Română):**
```
[
  "Ascultă cu atenție mesajul care ți se transmite",
  "Pune întrebări dacă nu înțelegi ceva",
  "Exprimă-te clar și folosește cuvinte potrivite",
  "Rispectă persoana cu care comunici"
]
```
---
## Questions Format
### Question Structure
Each lesson has **exactly ONE** question with:
```javascript
{
  question: "String - the actual question (20-100 characters)",
  options: [
    {
      text: "String - answer option",
      isCorrect: boolean (true for correct answer, false for others),
      explanation: "String - why this is correct/incorrect"
    },
    // ... 3 more options (total of 4)
  ]
}
```
### Question Guidelines
**✅ CORRECT Format:**
- **Lesson-Specific:** Question directly relates to lesson content
- **Clear:** Easy to understand, no ambiguity
- **Appropriate:** Grade-level difficulty (5th-8th grade)
- **Multiple Choice:** Always 4 options
- **One Correct:** Exactly 1 correct answer
- **Realistic Distractors:** Incorrect options are plausible mistakes
**❌ INCORRECT Format:**
- ❌ Generic template questions ("Întrebare de bază pentru L4")
- ❌ Vague or ambiguous wording
- ❌ Too easy or too difficult
- ❌ Wrong number of options
- ❌ Multiple correct answers
- ❌ Obvious trick answers
### Question Examples
**Matematica - Addition:**
```javascript
{
  question: "Dacă aduni 15 + 27, care este rezultatul?",
  options: [
    { text: "42", isCorrect: true, explanation: "Corect! 15 + 27 = 42" },
    { text: "40", isCorrect: false, explanation: "Incorect. Calculeaza din nou." },
    { text: "45", isCorrect: false, explanation: "Incorect. Calculeaza din nou." },
    { text: "35", isCorrect: false, explanation: "Incorect. Calculeaza din nou." }
  ]
}
```
**Limba Română - Communication:**
```javascript
{
  question: "Care sunt elementele esențiale ale procesului de comunicare?",
  options: [
    { 
      text: "Emițător, receptor, mesaj, canal și context", 
      isCorrect: true, 
      explanation: "Corect! Acestea sunt cei 5 elemente fundamentale." 
    },
    { 
      text: "Doar emițător și receptor", 
      isCorrect: false, 
      explanation: "Incorect. Sunt mai multi factori implicati." 
    },
    { 
      text: "Doar mesajul", 
      isCorrect: false, 
      explanation: "Incorect. Comunicarea necesita mai multi elemente." 
    },
    { 
      text: "Doar contextul", 
      isCorrect: false, 
      explanation: "Incorect. Contextul este important dar nu singur." 
    }
  ]
}
```
---
## Database Schema
### Materie (Subject)
```
{
  _id: ObjectId,
  name: "Matematica" | "Limba Română",
  clasa: "V" | "VI" | "VII" | "VIII",
  createdAt: Date
}
```
### Unitate (Learning Unit)
```
{
  _id: ObjectId,
  name: "Unit 1: Operații cu numere naturale",
  order: 1,
  materieId: ObjectId,
  createdAt: Date
}
```
### Capitol (Chapter)
```
{
  _id: ObjectId,
  name: "Chapter 1: Basic Operations",
  order: 1,
  unitateId: ObjectId,
  createdAt: Date
}
```
### Lectie (Lesson)
```
{
  _id: ObjectId,
  title: "L1 - Lecția 1",
  summary: "Numere naturale și operații fundamentale",
  content: {
    theory: "String (200-600 chars)",
    examples: ["String", "String", ...],
    tips: ["String", "String", ...]
  },
  materieId: ObjectId,
  unitateId: ObjectId,
  capitolId: ObjectId,
  estimatedTime: 45 (minutes),
  difficulty: "easy" | "medium" | "hard",
  createdAt: Date,
  updatedAt: Date
}
```
### LectieQuestion
```
{
  _id: ObjectId,
  lectieId: ObjectId,
  question: "String (20-100 chars)",
  options: [
    {
      text: "String (answer option)",
      isCorrect: Boolean,
      explanation: "String (feedback)"
    },
    // ... 3 more options
  ],
  createdAt: Date,
  updatedAt: Date
}
```
---
## Examples
### Complete Lesson Example 1: Matematica
**Lesson Title:** L2 - Lecția 2
**Subject:** Matematica
**Topic:** Adunarea și scăderea numerelor naturale
**Theory:**
```
Adunarea numerelor naturale:
- Operația inversă scăderii
- Termeni: numerele care se adună
- Sumă: rezultatul adunării
Proprietatea comutativă: a + b = b + a
Exemplu: 3 + 5 = 5 + 3 = 8
Proprietatea asociativă: (a + b) + c = a + (b + c)
Exemplu: (2 + 3) + 4 = 2 + (3 + 4) = 9
Element neutru: a + 0 = a
Exemplu: 7 + 0 = 7
```
**Examples:**
```
[
  "3 + 5 = 8 (termenii: 3 și 5; suma: 8)",
  "5 + 3 = 8 (comutativă)",
  "(2 + 3) + 4 = 5 + 4 = 9",
  "2 + (3 + 4) = 2 + 7 = 9"
]
```
**Tips:**
```
[
  "Folosește proprietatea comutativă pentru ordine mai convenabilă",
  "Grupează numerele care se adună ușor",
  "Verifică prin efectuarea în cealaltă ordine"
]
```
**Question:**
```javascript
{
  question: "Dacă aduni 15 + 27, care este rezultatul?",
  options: [
    { text: "42", isCorrect: true, explanation: "Corect! 15 + 27 = 42" },
    { text: "40", isCorrect: false, explanation: "Incorect. Calculeaza din nou." },
    { text: "45", isCorrect: false, explanation: "Incorect. Calculeaza din nou." },
    { text: "35", isCorrect: false, explanation: "Incorect. Calculeaza din nou." }
  ]
}
```
### Complete Lesson Example 2: Limba Română
**Lesson Title:** L1 - Lecția 1
**Subject:** Limba Română
**Topic:** Comunicare și limba - procesul comunicării
**Theory:**
```
Comunicarea este schimbul de mesaje între persoane pentru a transmite idei, sentimente și informații.
ELEMENTELE PROCESULUI DE COMUNICARE:
1. Emițător (vorbitor/autor) - persoana care trimite mesajul
2. Receptor (ascultător/cititor) - persoana care primește mesajul
3. Mesaj - informația transmisă
4. Canal - calea prin care se transmite mesajul (voce, scris, etc.)
5. Context - situația în care se produce comunicarea
TIPURI DE COMUNICARE:
- Comunicare verbală: folosind cuvintele
- Comunicare non-verbală: folosind gesturi, expresii faciale, tonul vocii
```
**Examples:**
```
[
  "Comunicare verbală: o conversație între doi prieteni",
  "Comunicare non-verbală: gesturile pe care le facem",
  "Comunicare scrisă: un mesaj trimis prin e-mail",
  "Comunicare digitală: un mesaj pe o rețea de socializare"
]
```
**Tips:**
```
[
  "Ascultă cu atenție și concentrare",
  "Exprimă-te clar și ușor de înțeles",
  "Respectă opinia celui cu care comunici",
  "Pun întrebări dacă nu înțelegi ceva"
]
```
**Question:**
```javascript
{
  question: "Care sunt elementele esențiale ale procesului de comunicare?",
  options: [
    { 
      text: "Emițător, receptor, mesaj, canal și context", 
      isCorrect: true, 
      explanation: "Corect! Acestea sunt cei 5 elemente fundamentale." 
    },
    { 
      text: "Doar emițător și receptor", 
      isCorrect: false, 
      explanation: "Incorect. Sunt mai multi factori implicati." 
    },
    { 
      text: "Doar mesajul", 
      isCorrect: false, 
      explanation: "Incorect. Comunicarea necesita mai multi elemente." 
    },
    { 
      text: "Doar contextul", 
      isCorrect: false, 
      explanation: "Incorect. Contextul este important dar nu singur." 
    }
  ]
}
```
---
## Quality Standards
### Content Quality Checklist
**Theory Content:**
- [ ] Clear and concise (200-600 characters)
- [ ] Age-appropriate for 5th-8th grade
- [ ] Uses proper Romanian language
- [ ] Defines key concepts
- [ ] Includes practical information
**Examples:**
- [ ] Directly related to theory
- [ ] Progressively more complex
- [ ] 1-4 examples per lesson
- [ ] Clear and easy to understand
- [ ] Demonstrable/applicable
**Tips:**
- [ ] Practical and actionable
- [ ] Easy to remember
- [ ] Related to lesson content
- [ ] 2-4 tips per lesson
- [ ] Encouraging tone
**Questions:**
- [ ] Directly related to lesson topic
- [ ] Clear and unambiguous
- [ ] Appropriate difficulty level
- [ ] Exactly 4 options
- [ ] Exactly 1 correct answer
- [ ] Realistic incorrect options
- [ ] Helpful explanations for all options
### Lesson Verification Checklist
Before marking a lesson as complete, verify:
✅ **Title:** Follows format "LX - Lecția X"
✅ **Summary:** Describes lesson topic clearly
✅ **Theory:** 200-600 characters, clear explanation
✅ **Examples:** 1-4 practical examples
✅ **Tips:** 2-4 helpful tips
✅ **Question:** Lesson-specific, 4 options, 1 correct
✅ **Explanations:** Clear feedback for all options
✅ **Language:** Proper Romanian, age-appropriate
✅ **Content Match:** All elements relate to lesson topic
---
## Lesson Count by Subject
### Matematica (51 lessons)
- Unit 1: Operații cu numere naturale (13 lessons)
- Unit 2: Metode aritmetice (5 lessons)
- Unit 3: Divizibilitate și numere prime (3 lessons)
- Unit 4: Fracții ordinare (10 lessons)
- Unit 5: Fracții zecimale (13 lessons)
- Unit 6: Geometrie (7 lessons)
### Limba Română (57 lessons)
- Unit 1: Fonologie și semăntica (Multiple lessons)
- Unit 2: Morfologie (Multiple lessons)
- Unit 3: Sintaxă (Multiple lessons)
- Unit 4: Ortografia și punctuație (Multiple lessons)
- Unit 5: Textul (Multiple lessons)
- Unit 6: Literatura și exprimare (Multiple lessons)
---
## Maintenance & Updates
### When Adding New Lessons:
1. Follow the lesson structure above
2. Ensure content meets quality standards
3. Create lesson-specific question matching the topic
4. Test thoroughly before deployment
5. Document any deviations from this specification
### When Updating Existing Lessons:
1. Maintain consistency with format
2. Preserve all essential fields
3. Update related questions if content changes
4. Verify all quality standards still apply
5. Test changes before deploying
---
## Version History
| Version | Date | Changes |
|---------|------|---------|
| 1.0 | Jan 20, 2026 | Initial format specification - Production Ready |
---
**Document Status:** ✅ APPROVED FOR PRODUCTION
**Next Review:** After 50 new lessons added or 6 months
**Contact:** Development Team
