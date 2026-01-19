# ✅ LECTIE QUESTION SCHEMA MISMATCH - FIXED

## The Problem

The import script was trying to create LectieQuestion documents with fields that don't match the database schema:

**What the script was sending:**
```javascript
{
  lectieId: "...",
  text: "Question text",           // ❌ Schema expects "question"
  options: [
    {
      text: "Option",
      correct: true,               // ❌ Schema expects "isCorrect"
      explanation: ""
    }
  ]
}
```

**What the schema expects:**
```javascript
{
  lectieId: "...",
  question: "Question text",       // ✅ Correct field name
  options: [
    {
      text: "Option",
      isCorrect: true,             // ✅ Correct field name
      explanation: ""
    }
  ]
}
```

## The Solution

Updated all 3 import scripts to map the JSON structure to the database schema:

```javascript
// Map JSON structure to schema structure
const mappedOptions = lectie.question.options.map(opt => ({
  text: opt.text,
  isCorrect: opt.correct || false,           // Convert "correct" → "isCorrect"
  explanation: opt.explanation || ''
}));

await LectieQuestion.create({
  lectieId: lectieDoc._id,
  question: lectie.question.text,            // Use "question" field
  options: mappedOptions,
  order: 1
});
```

## Files Fixed

✅ **directImport.js** - Updated question creation logic
✅ **importSimple.js** - Updated question creation logic
✅ **importCurriculum.js** - Updated question creation logic

## How to Run Now

Run the import command again:

```bash
cd /Users/mdica/PycharmProjects/EduPex
node backend/scripts/directImport.js
```

Expected output:
```
✅ Connected to MongoDB
✅ Created/Updated: Matematica
✅ Created/Updated: Limba Romana

Processing: Matematica_Clasa_V_CORRECT.json
  Subject: Matematica → Matematica
  Grade: V
  Units: 6
✅ Imported: Matematica_Clasa_V_CORRECT.json

Processing: LimbaRomana_Clasa_V_CORRECT.json
  Subject: Limba și literatura română → Limba Romana
  Grade: V
  Units: 6
✅ Imported: LimbaRomana_Clasa_V_CORRECT.json

[STEP 4] Verifying Counts...
✅ Lessons in database: 114
✅ Questions in database: 114
✅ Units in database: 12
✅ Grades in database: 2

================================================================================
🎉 IMPORT COMPLETE!
================================================================================
```

## Summary

| Field | JSON Has | Schema Expects | Fix |
|-------|----------|---|---|
| Question field | `question.text` | `question` | ✅ Mapped |
| Option property | `correct` | `isCorrect` | ✅ Mapped |
| Options structure | Direct array | Array with mapping | ✅ Mapped |

All scripts now handle the conversion automatically!

