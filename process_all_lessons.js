#!/usr/bin/env node

/**
 * Bulk Lesson Processor
 * Process multiple lessons with questions at once
 * This script creates a template for processing all 13 lessons in Capitol 1
 */

const fs = require('fs');
const path = require('path');

// Template for creating lessons with questions
const createLessonTemplate = (title, order, lessonsData) => {
  return {
    title,
    order,
    summary: lessonsData.summary,
    theory: lessonsData.theory,
    examples: lessonsData.examples,
    tips: lessonsData.tips,
    estimatedTime: lessonsData.estimatedTime || 12,
    difficulty: lessonsData.difficulty || 'medium',
    questions: lessonsData.questions || []
  };
};

// All 13 lessons for Capitol 1
const capitol1Lessons = {
  "L2": {
    summary: "Înțelege cum se reprezintă numerele pe o dreaptă și cum să le compari și să le ordonezi.",
    theory: "Pe axa numerelor, numerele cresc de la stânga la dreapta. Pentru a compara: dacă a < b, atunci a se află la stânga lui b pe axă. Aproximarea înseamnă rotunjire la zeci, sute, mii, etc.",
    examples: [
      "3 < 5 (3 este mai mic decât 5)",
      "15 rotunjit la zeci este 20"
    ],
    tips: [
      "Folosește semnele: < (mai mic), > (mai mare), = (egal)",
      "La rotunjire, privește cifra din dreapta"
    ],
    estimatedTime: 12,
    difficulty: 'easy',
    questions: [
      {
        question: "Pe axa numerelor, care număr este mai aproape de 0: 5 sau 12?",
        options: [
          { text: "5", isCorrect: true, explanation: "Corect! Pe axa numerelor, 5 este mai apropiere de 0 decât 12." },
          { text: "12", isCorrect: false, explanation: "Greșit. 12 este mai departe de 0 decât 5." },
          { text: "Sunt la fel de aproape", isCorrect: false, explanation: "Greșit. 5 este mai aproape de 0." },
          { text: "Nu se poate determina", isCorrect: false, explanation: "Greșit. Se poate determina ușor pe axa numerelor." }
        ],
        difficulty: 'easy'
      },
      {
        question: "Ordonează crescător: 25, 15, 35, 5",
        options: [
          { text: "5, 15, 25, 35", isCorrect: true, explanation: "Corect! Ordonare crescătoare = de la mic la mare: 5 < 15 < 25 < 35" },
          { text: "35, 25, 15, 5", isCorrect: false, explanation: "Greșit. Aceasta este ordonare descrescătoare, nu crescătoare." },
          { text: "5, 25, 15, 35", isCorrect: false, explanation: "Greșit. Ordinea nu este corectă. Trebuie: 5, 15, 25, 35." },
          { text: "15, 5, 25, 35", isCorrect: false, explanation: "Greșit. 5 ar trebui înaintea lui 15." }
        ],
        difficulty: 'easy'
      },
      {
        question: "Care este aproximarea numărului 48 la zeci?",
        options: [
          { text: "50", isCorrect: true, explanation: "Corect! 48 este mai apropiere de 50 decât de 40 (48 > 45), deci se rotunjește la 50." },
          { text: "40", isCorrect: false, explanation: "Greșit. 48 este mai apropiere de 50. Trebuia să se rotunjească la 50." },
          { text: "45", isCorrect: false, explanation: "Greșit. 45 nu este o aproximare la zeci. Trebuie 50 sau 40." },
          { text: "48", isCorrect: false, explanation: "Greșit. Aceasta este numărul original, nu aproximarea." }
        ],
        difficulty: 'easy'
      }
    ]
  },
  "L3": {
    summary: "Descoperă regulile adunării și proprietățile speciale ale acestei operații.",
    theory: "Adunarea este comutativă: a + b = b + a. Adunarea este asociativă: (a + b) + c = a + (b + c). Elementul neutru al adunării este 0: a + 0 = a.",
    examples: [
      "3 + 5 = 5 + 3 = 8",
      "(2 + 3) + 4 = 2 + (3 + 4) = 9"
    ],
    tips: [
      "Folosește proprietatea comutativă pentru a face calcule mai ușoare",
      "Grupează numerele care se adună ușor"
    ],
    estimatedTime: 12,
    difficulty: 'easy',
    questions: [
      {
        question: "Care este suma 234 + 156?",
        options: [
          { text: "390", isCorrect: true, explanation: "Corect! 234 + 156 = 390. Calcul: 4+6=10, 30+50=80, 200+100=300. Total: 390." },
          { text: "378", isCorrect: false, explanation: "Greșit. Ai greșit la calcul. Trebuie 390." },
          { text: "380", isCorrect: false, explanation: "Greșit. Lipsește 10 din calcul. Trebuie 390." },
          { text: "400", isCorrect: false, explanation: "Greșit. Ai rotunjit prea mult. Exactul este 390." }
        ],
        difficulty: 'easy'
      },
      {
        question: "3 + 5 = 5 + 3. Cum se numește această proprietate?",
        options: [
          { text: "Comutativitate", isCorrect: true, explanation: "Corect! Proprietatea comutativă: a + b = b + a (ordinea nu contează la adunare)." },
          { text: "Asociativitate", isCorrect: false, explanation: "Greșit. Asociativitatea este (a+b)+c = a+(b+c)." },
          { text: "Distributivitate", isCorrect: false, explanation: "Greșit. Distributivitatea este pentru înmulțire și adunare combinat." },
          { text: "Neutralitate", isCorrect: false, explanation: "Greșit. Neutralitatea este când a+0=a." }
        ],
        difficulty: 'medium'
      }
    ]
  },
  "L4": {
    summary: "Învață cum să scazi numerele naturale și înțelege relația cu adunarea.",
    theory: "Scăderea este operația inversă a adunării. Dacă a - b = c, atunci c + b = a. Descăzut - Scăzător = Diferență.",
    examples: [
      "10 - 3 = 7, verificare: 7 + 3 = 10",
      "25 - 8 = 17"
    ],
    tips: [
      "Verifica rezultatul adunând înapoi",
      "Nu poți scădea din zero un număr pozitiv"
    ],
    estimatedTime: 12,
    difficulty: 'easy',
    questions: [
      {
        question: "12 - 5 = ?",
        options: [
          { text: "7", isCorrect: true, explanation: "Corect! 12 - 5 = 7. Verificare: 7 + 5 = 12 ✓" },
          { text: "17", isCorrect: false, explanation: "Greșit. Ai adunat în loc să scazi." },
          { text: "2", isCorrect: false, explanation: "Greșit. Calculul este incorect. Trebuie 7." },
          { text: "8", isCorrect: false, explanation: "Greșit. Nu este corect. Răspunsul este 7." }
        ],
        difficulty: 'easy'
      }
    ]
  },
  "L5": {
    summary: "Explorează înmulțirea și descoperă proprietățile ei importante.",
    theory: "Înmulțirea este comutativă: a × b = b × a. Înmulțirea este asociativă: (a × b) × c = a × (b × c). Elementul neutru al înmulțirii este 1: a × 1 = a.",
    examples: [
      "3 × 4 = 4 × 3 = 12",
      "2 × (3 + 5) = 2 × 3 + 2 × 5 = 6 + 10 = 16"
    ],
    tips: [
      "Folosește proprietatea comutativă pentru a înmulți mai ușor",
      "Memorează tabla înmulțirii"
    ],
    estimatedTime: 15,
    difficulty: 'medium',
    questions: [
      {
        question: "6 × 7 = ?",
        options: [
          { text: "42", isCorrect: true, explanation: "Corect! 6 × 7 = 42" },
          { text: "13", isCorrect: false, explanation: "Greșit. Ai adunat, nu ai înmulțit." },
          { text: "67", isCorrect: false, explanation: "Greșit. Nu concatenezi cifrele. 6 × 7 = 42." },
          { text: "48", isCorrect: false, explanation: "Greșit. Calculul este incorect. Trebuie 42." }
        ],
        difficulty: 'easy'
      }
    ]
  },
  "L6": {
    summary: "Înțelege cum să identifici și să extragi factorul comun din expresii.",
    theory: "Factorul comun este numărul care se repetă în fiecare termen. Formula: a × b + a × c = a × (b + c). Pentru a extrage factorul comun, împarți fiecare termen la factor și adscrieți factorul în paranteză.",
    examples: [
      "6 + 9 = 3 × 2 + 3 × 3 = 3 × (2 + 3) = 3 × 5 = 15",
      "12 + 18 = 6 × 2 + 6 × 3 = 6 × (2 + 3) = 6 × 5 = 30"
    ],
    tips: [
      "Caută cel mai mare factor comun",
      "Verifică prin distribuire"
    ],
    estimatedTime: 12,
    difficulty: 'medium',
    questions: []
  },
  "L7": {
    summary: "Aprinde cum să împarți numere naturale când nu rămâne rest.",
    theory: "Împărțirea cu rest 0 (exactă): Deîmpărțit : Împărțitor = Cât. Verificare: Cât × Împărțitor = Deîmpărțit.",
    examples: [
      "20 : 4 = 5, verificare: 5 × 4 = 20",
      "36 : 6 = 6"
    ],
    tips: [
      "Verifica înmulțind rezultatul cu împărțitorul",
      "Folosește tabla înmulțirii"
    ],
    estimatedTime: 12,
    difficulty: 'medium',
    questions: []
  },
  "L8": {
    summary: "Descoperă cum se face împărțirea când rămâne rest și cum verific rezultatul.",
    theory: "Împărțirea cu rest: Deîmpărțit : Împărțitor = Cât rest Rest. Formula: Deîmpărțit = Cât × Împărțitor + Rest, unde Rest < Împărțitor.",
    examples: [
      "23 : 5 = 4 rest 3, verificare: 4 × 5 + 3 = 23",
      "17 : 3 = 5 rest 2"
    ],
    tips: [
      "Restul trebuie să fie mai mic decât împărțitorul",
      "Verifica: Cât × Împărțitor + Rest = Deîmpărțit"
    ],
    estimatedTime: 12,
    difficulty: 'medium',
    questions: []
  },
  "L9": {
    summary: "Înțelege exponenții și cum să calcula puteri ale numerelor naturale.",
    theory: "Puterea: a^n = a × a × a ... × a (de n ori). a se numește bază, n se numește exponent. Pătratul unui număr: a² = a × a. Exemplu: 3² = 3 × 3 = 9.",
    examples: [
      "2³ = 2 × 2 × 2 = 8",
      "5² = 5 × 5 = 25",
      "10² = 100"
    ],
    tips: [
      "Pătratele numerelor 1-10: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100",
      "a¹ = a și a⁰ = 1 (cu a ≠ 0)"
    ],
    estimatedTime: 12,
    difficulty: 'medium',
    questions: []
  },
  "L10": {
    summary: "Aprinde regulile care fac calculele cu puteri mai ușoare.",
    theory: "a^m × a^n = a^(m+n), a^m : a^n = a^(m-n), (a^m)^n = a^(m×n), a^n × b^n = (a×b)^n, a^n : b^n = (a:b)^n",
    examples: [
      "2³ × 2² = 2⁵ = 32",
      "(3²)² = 3⁴ = 81",
      "2³ × 5³ = (2 × 5)³ = 10³ = 1000"
    ],
    tips: [
      "Când înmulțești puteri cu aceeași bază, aduni exponenții",
      "Când împarți puteri cu aceeași bază, scazi exponenții"
    ],
    estimatedTime: 12,
    difficulty: 'medium',
    questions: []
  },
  "L11": {
    summary: "Învață cum să compari numere exprimate ca puteri.",
    theory: "Pentru a compara a^m și b^n: 1) Dacă au aceeași bază, compară exponenții. 2) Dacă au același exponent, compară bazele. 3) Dacă nu au nici baza nici exponentul egal, calculează valorile.",
    examples: [
      "2³ < 2⁴ (3 < 4)",
      "2³ < 3³ (2 < 3)",
      "2³ = 8 și 3² = 9, deci 2³ < 3²"
    ],
    tips: [
      "Convertește la aceeași bază sau exponent dacă se poate",
      "Calculează valorile dacă este necesar"
    ],
    estimatedTime: 11,
    difficulty: 'medium',
    questions: []
  },
  "L12": {
    summary: "Descoperă cum funcționează sistemele de numerație cu baze diferite.",
    theory: "Baza 10: fiecare cifră poate fi 0-9. Baza 2: fiecare cifră poate fi doar 0 sau 1. În baza 10: 1234 = 1×10³ + 2×10² + 3×10¹ + 4×10⁰. În baza 2: 1011 = 1×2³ + 0×2² + 1×2¹ + 1×2⁰ = 11 în baza 10.",
    examples: [
      "3210₁₀ = 3×10³ + 2×10² + 1×10¹ + 0×10⁰",
      "101₂ = 1×2² + 0×2¹ + 1×2⁰ = 5₁₀"
    ],
    tips: [
      "Baza 10 folosește cifrele 0-9",
      "Baza 2 folosește cifrele 0-1"
    ],
    estimatedTime: 12,
    difficulty: 'hard',
    questions: []
  },
  "L13": {
    summary: "Învață ordinea corectă a operațiilor pentru a obține rezultatul corect.",
    theory: "Ordinea operațiilor: 1) Parantezele (rotunde, pătrate, acolade) 2) Puteri 3) Înmulțire și împărțire (de la stânga la dreapta) 4) Adunare și scădere (de la stânga la dreapta). Mnemotehnica: PEMDAS (Parentheses, Exponents, Multiply/Divide, Add/Subtract).",
    examples: [
      "2 + 3 × 4 = 2 + 12 = 14 (nu 5 × 4 = 20)",
      "[2 + (3 × 4)] × 2 = [2 + 12] × 2 = 14 × 2 = 28"
    ],
    tips: [
      "Mereu respectă ordinea operațiilor",
      "Lucreaza din interior spre exterior pentru paranteze"
    ],
    estimatedTime: 12,
    difficulty: 'hard',
    questions: []
  }
};

console.log('📚 Capitol 1 Lessons Template Created');
console.log('====================================\n');

// Count questions
let totalQuestions = 0;
Object.keys(capitol1Lessons).forEach(lesson => {
  const q = capitol1Lessons[lesson].questions || [];
  totalQuestions += q.length;
  console.log(`${lesson}: ${q.length} questions`);
});

console.log(`\n📊 Summary:`);
console.log(`- Total Lessons: ${Object.keys(capitol1Lessons).length}`);
console.log(`- Total Questions Prepared: ${totalQuestions}`);
console.log(`- L2-L13 structure ready for questions`);

console.log('\n✅ Next Steps:');
console.log('1. Extract remaining lesson questions from Manual.pdf');
console.log('2. Add to L2-L13 questions arrays');
console.log('3. Run seed script to import all');
console.log('4. Test API endpoints');
console.log('5. Build frontend UI\n');

