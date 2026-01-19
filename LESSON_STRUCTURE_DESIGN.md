# EduPex Lesson Structure - Design & Architecture

## 📚 Lesson Hierarchy

```
Materie (Subject)
├── Matematica
└── Limba Romana
    │
    ├── Clasă (Grade) - V, VI, VII, VIII
    │   │
    │   ├── Unitate de învățare (Learning Unit)
    │   │   │
    │   │   ├── Capitol (Chapter)
    │   │   │   │
    │   │   │   └── Lecție (Lesson) - L1, L2, L3...
    │   │   │       │
    │   │   │       └── Content:
    │   │   │           - Summary (text explanation)
    │   │   │           - Question (text + 4 multiple choice options)
    │   │   │           - Feedback
    │   │   │           - Progress tracking
```

## 🗄️ Database Schema

### 1. Materie (Subject)
```javascript
{
  _id: ObjectId,
  name: String, // "Matematica", "Limba Romana"
  description: String,
  icon: String,
  order: Number
}
```

### 2. Clasa (Grade)
```javascript
{
  _id: ObjectId,
  materieId: ObjectId,
  name: String, // "V", "VI", "VII", "VIII"
  level: Number, // 5, 6, 7, 8
  order: Number
}
```

### 3. UnitateDeInvatare (Learning Unit)
```javascript
{
  _id: ObjectId,
  clasaId: ObjectId,
  materieId: ObjectId,
  name: String, // e.g., "Numere și operații"
  description: String,
  order: Number
}
```

### 4. Capitol (Chapter)
```javascript
{
  _id: ObjectId,
  unitateId: ObjectId,
  name: String, // e.g., "Adunarea și scăderea"
  description: String,
  order: Number
}
```

### 5. Lectie (Lesson)
```javascript
{
  _id: ObjectId,
  capitolId: ObjectId,
  unitateId: ObjectId,
  clasaId: ObjectId,
  materieId: ObjectId,
  title: String, // e.g., "L1 - Adunarea numerelor"
  order: Number,
  summary: String, // Educational content/explanation
  content: {
    theory: String, // Detailed explanation
    examples: [String], // Example problems
    tips: [String] // Learning tips
  }
}
```

### 6. LectieQuestion (Questions/Exercises)
```javascript
{
  _id: ObjectId,
  lectieId: ObjectId,
  question: String, // The question text
  options: [
    {
      text: String,
      isCorrect: Boolean,
      explanation: String // Why is this correct/wrong?
    }
  ],
  difficulty: String, // "easy", "medium", "hard"
  order: Number,
  type: String, // "multiple-choice", "true-false"
}
```

### 7. UserProgress (User's Learning Progress)
```javascript
{
  _id: ObjectId,
  userId: ObjectId,
  lectieId: ObjectId,
  questionsCompleted: [
    {
      questionId: ObjectId,
      selectedAnswerId: Number, // Index of selected option
      isCorrect: Boolean,
      timestamp: Date,
      attemptNumber: Number
    }
  ],
  lectieStatus: String, // "not-started", "in-progress", "completed"
  completionDate: Date,
  score: Number, // Percentage: 0-100
  timeSpent: Number, // In seconds
  attempts: Number
}
```

### 8. UserAchievement/Streak
```javascript
{
  _id: ObjectId,
  userId: ObjectId,
  currentStreak: Number, // Days
  longestStreak: Number,
  lastActivityDate: Date,
  totalLessonsCompleted: Number,
  totalPointsEarned: Number,
  badges: [String]
}
```

---

## 🎯 Lesson Flow (Like Duolingo)

### User's Journey:
1. **Select Subject** → Matematica or Limba Romana
2. **Select Grade** → V, VI, VII, VIII
3. **View Learning Units** → List of units
4. **Select Chapter** → Choose chapter within unit
5. **Start Lesson** → View summary + complete questions
6. **Question Screen** → Display question + 4 options
7. **Answer Check** → Show if correct/wrong + explanation
8. **Progress** → Save to database + show streak
9. **Complete** → Mark lesson complete + earn points

---

## 💾 Progress Tracking Strategy

### What to Save:
- ✅ Which lessons user completed
- ✅ Answers selected
- ✅ Correct/incorrect answers
- ✅ Time spent per lesson
- ✅ Current streak (consecutive days)
- ✅ Total points earned
- ✅ Accuracy percentage

### Where to Save:
- **UserProgress** collection → Individual lesson attempts
- **UserAchievement** collection → Overall stats and streaks
- **Local Storage** → Current session data (optional caching)

---

## 🛠️ Implementation Approach

### Phase 1: Database Structure
1. Create MongoDB collections (models)
2. Create API routes to:
   - GET all Materii (subjects)
   - GET Clase for a Materie
   - GET UnitatiDeInvatare for a Clasa
   - GET Capitole for a Unitate
   - GET Lectii for a Capitol
   - GET Lectie details + questions

### Phase 2: Frontend - Lesson Navigation
1. Subject Selection Screen
2. Grade Selection Screen
3. Learning Units List
4. Chapters List
5. Lessons List

### Phase 3: Frontend - Lesson Player
1. Lesson Summary Screen
2. Question Display
3. Multiple Choice Selection
4. Feedback/Explanation
5. Progress Indicator
6. Next Lesson Button

### Phase 4: Progress Tracking
1. Save answers to UserProgress
2. Calculate score
3. Update streaks
4. Show statistics dashboard

### Phase 5: Data Import
1. Import your Unitati, Capitole, Lectii
2. Link them properly in hierarchy
3. Add questions for each lesson

---

## 📱 Frontend Structure

```
LessonApp/
├── pages/
│   ├── SubjectSelection.js      # Choose subject
│   ├── GradeSelection.js         # Choose grade
│   ├── LessonUnits.js            # Show units
│   ├── Chapters.js               # Show chapters
│   ├── Lessons.js                # Show lessons
│   └── LessonPlayer.js           # Main lesson interface
│       ├── LessonSummary.js      # Summary view
│       ├── Question.js            # Question + options
│       └── Results.js             # Feedback
│
├── components/
│   ├── ProgressBar.js            # Progress indicator
│   ├── StreakCounter.js           # Streak display
│   ├── QuestionOption.js          # Answer option button
│   └── LessonCard.js              # Lesson preview card
│
├── services/
│   ├── lessonService.js           # API calls for lessons
│   └── progressService.js         # API calls for progress
│
└── redux/
    └── lessonSlice.js             # State management
```

---

## ✨ Best Practices Implemented

1. **Normalized Database** - Separate collections for each entity
2. **Foreign Keys** - Proper linking between collections
3. **Denormalization** - Store parentIds for quick access
4. **Progress Tracking** - Comprehensive user activity logging
5. **Scalability** - Can handle thousands of lessons
6. **User Engagement** - Streaks, points, badges
7. **Analytics Ready** - Tracks everything for insights

---

## 🎓 Your Next Steps

1. **Prepare Data**: Organize your Unitati, Capitole, Lectii
2. **Provide Content**: Summary + Questions for each lesson
3. **Format**: Send in JSON or CSV format
4. **I'll Create**: All backend models, routes, and frontend UI

---

## 📋 Data Format Expected From You

For each Lectie, provide:

```json
{
  "unitate": "Numere și operații",
  "capitol": "Adunarea și scăderea",
  "lectie": "L1 - Adunarea numerelor naturale",
  "clasaGrada": 5,
  "materie": "Matematica",
  "summary": "Adunarea este operația prin care...",
  "theory": "Explicație detaliată...",
  "examples": ["2 + 3 = 5", "10 + 15 = 25"],
  "questions": [
    {
      "question": "Care este rezultatul: 5 + 3?",
      "options": [
        {"text": "8", "correct": true, "explanation": "Corect!"},
        {"text": "2", "correct": false, "explanation": "Greșit. 5 + 3 = 8"},
        {"text": "15", "correct": false, "explanation": "Greșit. 5 + 3 = 8"},
        {"text": "10", "correct": false, "explanation": "Greșit. 5 + 3 = 8"}
      ]
    }
  ]
}
```

---

**Ready to start building? Send me your first batch of Unitati & Lectii!** 📚

