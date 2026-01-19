# 📱 FRONTEND + BACKEND INTEGRATION ROADMAP

## Current Status

### ✅ What's Ready to Use RIGHT NOW

#### Backend ✅
- ✅ Express.js server running
- ✅ MongoDB models defined (Materie, Clasa, Unitate, Lectie, Question, Progress, User)
- ✅ Authentication routes (login, register, JWT)
- ✅ API endpoints for lessons (get all, get by ID, etc.)
- ✅ API for progress tracking
- ✅ API for user stats
- ✅ 8 CORRECT curriculum JSON files
- ✅ Import script to populate database

#### Frontend ✅
- ✅ React app structure
- ✅ Capacitor for mobile (iOS/Android)
- ✅ Build pipeline for APK

---

## What Needs To Be Built

### Frontend Components Needed (2-3 weeks)

#### 1. **Curriculum Browser** (1 week)
```
CurriculumScreen
├── SubjectsList
│   ├── Matematica
│   └── Limba Română
├── GradeSelector (V, VI, VII, VIII)
├── UnitsList
│   ├── UNITATEA 1 - Name [Progress bar 80%]
│   ├── UNITATEA 2 - Name [Progress bar 0%]
│   └── ... more units
└── LessonsInUnit
    ├── L1 - Lesson Title [✅ Completed]
    ├── L2 - Lesson Title [🔒 Locked]
    └── ... more lessons
```

#### 2. **Lesson View Component** (1 week)
```
LessonScreen
├── LessonHeader
│   ├── Title
│   ├── Progress (X of Y questions)
│   └── Back button
├── LessonContent
│   ├── Theory section
│   ├── Examples
│   └── Tips
├── QuestionComponent
│   ├── Question text
│   ├── 4 Answer options (A, B, C, D)
│   ├── Submit button
│   └── Feedback (✅ Correct! / ❌ Wrong!)
└── NavigationButtons
    ├── Previous
    └── Next / Complete
```

#### 3. **Duolingo-Style UI Components** (3-4 days)
```
Header
├── 🔥 Streak: 5 days
├── ⭐ XP: 1,250
├── ❤️ Hearts: 5/5

ProgressCard
├── Total lessons: 463
├── Completed: 87
├── Progress: 18.8%
├── Total XP: 4,350

AchievementBadges
├── First 10 lessons
├── 1 week streak
├── 100 XP earned
└── ... more achievements
```

#### 4. **User Profile** (3-4 days)
```
ProfileScreen
├── User info
├── Stats
│   ├── Level: 5
│   ├── Total XP: 4,350
│   ├── Streak: 5 days
│   └── Total time: 12 hours
├── Progress by subject
│   ├── Matematica: 45%
│   └── Limba Română: 23%
└── Achievements list
```

---

## Step-by-Step Implementation Guide

### STEP 1: Import Curriculum (2 hours) 🚀

```bash
# Run this command
node backend/scripts/importCurriculum.js

# Verify in MongoDB
mongosh
use edupex
db.lecties.countDocuments()  # Should show 463
```

### STEP 2: Create Curriculum Screen (2-3 days)

```jsx
// frontend/src/screens/CurriculumScreen.jsx

import React, { useState, useEffect } from 'react';
import { getUserProgress, getCurriculum } from '../api/lessonApi';

export default function CurriculumScreen() {
  const [subjects, setSubjects] = useState([]);
  const [selectedSubject, setSelectedSubject] = useState(null);
  const [units, setUnits] = useState([]);
  const [userProgress, setUserProgress] = useState({});

  useEffect(() => {
    loadCurriculum();
    loadProgress();
  }, []);

  const loadCurriculum = async () => {
    const data = await getCurriculum();
    setSubjects(data.subjects);
  };

  const loadProgress = async () => {
    const progress = await getUserProgress();
    setUserProgress(progress);
  };

  const handleSelectSubject = async (subject) => {
    setSelectedSubject(subject);
    const subjectUnits = await getUnits(subject.id);
    setUnits(subjectUnits);
  };

  return (
    <div className="curriculum-screen">
      {!selectedSubject ? (
        // Show subjects
        <div className="subjects-list">
          {subjects.map(subject => (
            <div key={subject.id} className="subject-card">
              <h2>{subject.name}</h2>
              <button onClick={() => handleSelectSubject(subject)}>
                Select
              </button>
            </div>
          ))}
        </div>
      ) : (
        // Show units and lessons
        <div className="units-list">
          <button onClick={() => setSelectedSubject(null)}>Back</button>
          {units.map(unit => (
            <UnitCard key={unit.id} unit={unit} progress={userProgress[unit.id]} />
          ))}
        </div>
      )}
    </div>
  );
}
```

### STEP 3: Create Lesson Screen (3-4 days)

```jsx
// frontend/src/screens/LessonScreen.jsx

import React, { useState, useEffect } from 'react';
import { getLesson, submitAnswer } from '../api/lessonApi';

export default function LessonScreen({ lessonId }) {
  const [lesson, setLesson] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [userAnswers, setUserAnswers] = useState([]);
  const [feedback, setFeedback] = useState(null);
  const [xpEarned, setXpEarned] = useState(0);

  useEffect(() => {
    loadLesson();
  }, [lessonId]);

  const loadLesson = async () => {
    const data = await getLesson(lessonId);
    setLesson(data);
  };

  const handleAnswerSubmit = async (optionIndex) => {
    const question = lesson.questions[currentQuestion];
    const isCorrect = question.options[optionIndex].correct;

    // Show feedback
    setFeedback({
      isCorrect,
      explanation: question.options[optionIndex].explanation,
      correctIndex: question.options.findIndex(o => o.correct)
    });

    // Save progress
    const result = await submitAnswer({
      lessonId,
      questionIndex: currentQuestion,
      userAnswer: optionIndex,
      correct: isCorrect,
      timeSpent: 30 // seconds
    });

    if (isCorrect) {
      setXpEarned(xpEarned + 10);
    }
  };

  const handleNext = () => {
    if (currentQuestion < lesson.questions.length - 1) {
      setCurrentQuestion(currentQuestion + 1);
      setFeedback(null);
    } else {
      // Lesson complete
      handleLessonComplete();
    }
  };

  const handleLessonComplete = () => {
    // Show completion screen
    alert(`Lesson complete! You earned ${xpEarned} XP!`);
  };

  if (!lesson) return <div>Loading...</div>;

  const question = lesson.questions[currentQuestion];

  return (
    <div className="lesson-screen">
      {/* Header */}
      <div className="lesson-header">
        <h1>{lesson.title}</h1>
        <p>Question {currentQuestion + 1} of {lesson.questions.length}</p>
      </div>

      {/* Theory Section */}
      {currentQuestion === 0 && (
        <div className="theory-section">
          <h2>Theory</h2>
          <p>{lesson.theory}</p>
          {lesson.examples && (
            <>
              <h3>Examples</h3>
              {lesson.examples.map((ex, i) => <p key={i}>{ex}</p>)}
            </>
          )}
        </div>
      )}

      {/* Question */}
      <div className="question-section">
        <h2>{question.text}</h2>
        <div className="options">
          {question.options.map((option, index) => (
            <button
              key={index}
              className={`option-btn ${
                feedback && index === feedback.correctIndex ? 'correct' : ''
              } ${feedback && index !== feedback.correctIndex && feedback.isCorrect === false ? 'wrong' : ''}`}
              onClick={() => !feedback && handleAnswerSubmit(index)}
              disabled={!!feedback}
            >
              {String.fromCharCode(65 + index)}. {option.text}
            </button>
          ))}
        </div>
      </div>

      {/* Feedback */}
      {feedback && (
        <div className={`feedback ${feedback.isCorrect ? 'correct' : 'incorrect'}`}>
          <p>{feedback.isCorrect ? '✅ Correct!' : '❌ Wrong!'}</p>
          <p>{feedback.explanation}</p>
          <button onClick={handleNext}>
            {currentQuestion < lesson.questions.length - 1 ? 'Next Question' : 'Complete Lesson'}
          </button>
        </div>
      )}
    </div>
  );
}
```

### STEP 4: Create Duolingo-Style Header (1-2 days)

```jsx
// frontend/src/components/DuolingoHeader.jsx

import React, { useState, useEffect } from 'react';
import { getUserStats } from '../api/userApi';

export default function DuolingoHeader() {
  const [stats, setStats] = useState({
    streak: 0,
    xp: 0,
    hearts: 5,
    level: 1
  });

  useEffect(() => {
    loadStats();
  }, []);

  const loadStats = async () => {
    const data = await getUserStats();
    setStats(data);
  };

  return (
    <header className="duolingo-header">
      <div className="header-item">
        <span className="emoji">🔥</span>
        <span className="text">Streak: {stats.streak} days</span>
      </div>
      <div className="header-item">
        <span className="emoji">⭐</span>
        <span className="text">XP: {stats.xp}</span>
      </div>
      <div className="header-item">
        <span className="emoji">❤️</span>
        <span className="text">Hearts: {stats.hearts}/5</span>
      </div>
      <div className="header-item">
        <span className="emoji">📊</span>
        <span className="text">Level: {stats.level}</span>
      </div>
    </header>
  );
}
```

### STEP 5: Create API Service Layer (1 day)

```javascript
// frontend/src/api/lessonApi.js

export async function getCurriculum() {
  const response = await fetch('http://localhost:5000/api/lessons/materii');
  return response.json();
}

export async function getUnits(clasaId) {
  const response = await fetch(
    `http://localhost:5000/api/lessons/clase/${clasaId}/unitati`
  );
  return response.json();
}

export async function getLesson(lessonId) {
  const response = await fetch(
    `http://localhost:5000/api/lessons/lectii/${lessonId}`,
    {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    }
  );
  return response.json();
}

export async function submitAnswer(data) {
  const response = await fetch(
    `http://localhost:5000/api/lessons/${data.lessonId}/submit-answer`,
    {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      },
      body: JSON.stringify(data)
    }
  );
  return response.json();
}

export async function getUserProgress() {
  const response = await fetch(
    'http://localhost:5000/api/lessons/progress',
    {
      headers: {
        'Authorization': `Bearer ${localStorage.getItem('token')}`
      }
    }
  );
  return response.json();
}
```

---

## Complete Timeline

| Phase | Task | Duration | Status |
|-------|------|----------|--------|
| 1 | ✅ Create curriculum JSON files | Done | ✅ |
| 2 | 🚀 **Import to MongoDB** | 2 hours | 🚀 **START HERE** |
| 3 | Create API endpoints | 3 hours | ⏳ After import |
| 4 | Create Curriculum Screen | 2-3 days | ⏳ |
| 5 | Create Lesson Screen | 3-4 days | ⏳ |
| 6 | Add Duolingo UI (XP, Streak, Hearts) | 1 week | ⏳ |
| 7 | Test & Polish | 3-5 days | ⏳ |
| **Total** | **Full Learning Platform** | **3 weeks** | |

---

## Your Choice Right Now

You have 3 options:

### 🚀 Option A: I Do Everything (Fastest)
- I create all components
- I set up everything
- You just run it
- **Time**: 2-3 weeks
- **Effort**: Minimal on your part

### 🔄 Option B: I Guide You (Learning)
- I provide code
- You implement it
- I review and adjust
- **Time**: 3-4 weeks
- **Effort**: Moderate
- **Benefit**: You learn the code

### 🤝 Option C: We Build Together
- We pair program
- Share the work
- Quick and collaborative
- **Time**: 2-3 weeks
- **Effort**: Balanced

---

## Immediate Next Action

**1️⃣ Run the import script:**
```bash
node backend/scripts/importCurriculum.js
```

**2️⃣ Verify in MongoDB:**
```bash
mongosh
use edupex
db.lecties.countDocuments()
```

**3️⃣ Let me know when done**, then we proceed with:
- ✅ API endpoints (already written)
- 🚀 Frontend components

---

## Summary

| What | Status | Next |
|------|--------|------|
| Curriculum structure | ✅ Done | Import to DB |
| Backend models | ✅ Ready | Use them |
| API routes | ✅ Ready | Test them |
| Frontend | ⏳ Empty | Build it |
| **Overall** | **Ready to deploy** | **Let's go!** |

---

**Let's make this happen! 🚀**

