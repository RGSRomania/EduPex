const fs = require('fs');
const path = require('path');
// Load the Complete JSON files which have proper questions for each lesson
const matPath = './Matematica_Clasa_5_Complete.json';
const limbaPath = './LimbaRomana_Clasa_5_Complete.json';
console.log('Extracting real questions from JSON files...\n');
const matData = JSON.parse(fs.readFileSync(matPath, 'utf8'));
const limbaData = JSON.parse(fs.readFileSync(limbaPath, 'utf8'));
// Map lessons to their questions
const matQuestionsMap = {};
const limbaQuestionsMap = {};
console.log('=== MATEMATICA LESSONS WITH QUESTIONS ===\n');
(matData.unitati || []).forEach((unitate, unitIdx) => {
  (unitate.capitole || []).forEach((capitol, capIdx) => {
    (capitol.lectii || []).forEach((lectie, lectieIdx) => {
      const lessonNum = lectieIdx + 1;
      const title = lectie.title;
      const questions = lectie.questions || [];
      console.log(`L${lessonNum}: ${title}`);
      console.log(`  Question count: ${questions.length}`);
      if (questions.length > 0) {
        console.log(`  Question: "${questions[0].question}"`);
        console.log(`  Options: ${questions[0].options?.length || 0}`);
        // Store for database update
        matQuestionsMap[`L${lessonNum}`] = {
          unitIdx,
          capIdx,
          lectieIdx,
          title,
          question: questions[0]
        };
      }
      console.log();
    });
  });
});
console.log('\n=== LIMBA ROMANA LESSONS WITH QUESTIONS ===\n');
(limbaData.unitati || []).forEach((unitate, unitIdx) => {
  (unitate.capitole || []).forEach((capitol, capIdx) => {
    (capitol.lectii || []).forEach((lectie, lectieIdx) => {
      const lessonNum = lectieIdx + 1;
      const title = lectie.title;
      const questions = lectie.questions || [];
      console.log(`L${lessonNum}: ${title}`);
      console.log(`  Question count: ${questions.length}`);
      if (questions.length > 0) {
        console.log(`  Question: "${questions[0].question}"`);
        console.log(`  Options: ${questions[0].options?.length || 0}`);
        // Store for database update
        limbaQuestionsMap[`L${lessonNum}`] = {
          unitIdx,
          capIdx,
          lectieIdx,
          title,
          question: questions[0]
        };
      }
      console.log();
    });
  });
});
// Save mapping for next script
fs.writeFileSync('/tmp/questions_map.json', JSON.stringify({
  matematica: matQuestionsMap,
  limba: limbaQuestionsMap
}, null, 2));
console.log('✅ Saved questions map to /tmp/questions_map.json');
console.log(`Total Mat lessons with questions: ${Object.keys(matQuestionsMap).length}`);
console.log(`Total Limba lessons with questions: ${Object.keys(limbaQuestionsMap).length}`);
