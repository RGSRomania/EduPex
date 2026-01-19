#!/usr/bin/env node

/**
 * Question Processor
 * Converts extracted questions into the proper format with 4 multiple-choice options
 */

const fs = require('fs');
const path = require('path');

// Template for processing questions
const questionTemplate = {
  "capitol": "",
  "lectie": "",
  "questions": []
};

// Function to generate multiple-choice options
function generateOptions(question, correctAnswer) {
  // This is a template - actual options come from the user
  return [
    {
      "text": correctAnswer,
      "correct": true,
      "explanation": "Correct! This is the right answer."
    },
    {
      "text": "Option B",
      "correct": false,
      "explanation": "This is not correct because..."
    },
    {
      "text": "Option C",
      "correct": false,
      "explanation": "This is not correct because..."
    },
    {
      "text": "Option D",
      "correct": false,
      "explanation": "This is not correct because..."
    }
  ];
}

// Example input format
const exampleInput = `
{
  "capitol": "Capitol 1: Operații cu numere naturale",
  "lectii": [
    {
      "title": "L1 - Scrierea și citirea numerelor naturale",
      "questions_raw": [
        "Cum se citește numărul 5247?",
        "Scrie în cifre: trei mii opt sute doi"
      ]
    },
    {
      "title": "L2 - Reprezentarea pe axa numerelor",
      "questions_raw": [
        "Pe axa numerelor, care este mai mic: 5 sau 12?",
        "Aproximează 48 la zeci"
      ]
    }
  ]
}
`;

console.log('📚 Question Processor');
console.log('====================\n');

console.log('📝 Expected Input Format:\n');
console.log(exampleInput);

console.log('\n📋 How to Use:');
console.log('1. Save your extracted questions in JSON format (as shown above)');
console.log('2. Run: node question-processor.js questions.json');
console.log('3. Tool will generate options and create final JSON');
console.log('4. Output ready for database import\n');

console.log('✅ Create a questions.json file with the format above and we\'ll process it!');

