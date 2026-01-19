# 🚀 EduPex - Quick Start Guide (30 Minutes)

## What is EduPex?

**EduPex** = Educational app for learning Math & Romanian (grades 5-8) with gamification like Duolingo

**Goal** = Create APK to send to device not on same network, with hardcoded test login

---

## ⚡ 5-Minute Overview

### Problem You Had
❌ Device not on same network as laptop  
❌ Can't hardcode localhost backend URL  
❌ Need test credentials pre-configured  
❌ Want one-click demo login  

### Solution Implemented
✅ Backend deployed on Render.com (works from anywhere)  
✅ Production URL hardcoded in APK  
✅ Test user created in database  
✅ Demo login button on login page (one-click)  

---

## 📊 Architecture (Simple)

```
┌─────────────────────────────────────────────┐
│  Device (Anywhere in World)                 │
│  ┌───────────────────────────────────────┐  │
│  │ EduPex APK                            │  │
│  │ - Login page with demo button         │  │
│  │ - Dashboard with lessons              │  │
│  │ - Quizzes and achievements            │  │
│  └───────────────────┬───────────────────┘  │
│                      │                      │
│                      │ (Internet)           │
└──────────────────────┼──────────────────────┘
                       │
                       ↓
┌──────────────────────────────────────────────┐
│  Render.com Server (Deployed Backend)        │
│  https://edupex-backend.onrender.com/api     │
│                                              │
│  - User authentication                       │
│  - Lesson data                               │
│  - Progress tracking                         │
│  - AI assistant                              │
└────────────────┬─────────────────────────────┘
                 │
                 ↓
        ┌────────────────┐
        │  MongoDB       │
        │  - Users       │
        │  - Lessons     │
        │  - Progress    │
        └────────────────┘
```

---

## 🎯 Test Credentials (Already Set Up)

```
Email:    test@edupex.com
Password: test123

How to use: Click "🎓 Intră cu Cont Demo" button
Result:    Instant login, no typing needed!
```

---

## 🚀 Build APK in 3 Steps (15 Minutes)

### Step 1: Verify Test User (2 min)

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
npm install
node checkTestUser.js
```

Expected: ✅ Test user exists!

### Step 2: Build APK (10 min)

```bash
cd /Users/mdica/PycharmProjects/EduPex
./build-demo-apk.sh
```

Expected: APK created at `frontend/android/app/build/outputs/apk/debug/app-debug.apk`

### Step 3: Install on Device (3 min)

**Option A: Via ADB (Fastest)**
```bash
adb install /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

**Option B: Manual**
1. Email APK to device
2. Tap to install
3. Done!

---

## ✅ Test on Device (5 Minutes)

1. **Open app** → See login page
2. **Click "🎓 Intră cu Cont Demo"** → Auto-login
3. **See dashboard** with XP, level, streak
4. **Click lessons** → See Math & Romanian courses
5. **Try a quiz** → Answer questions and get XP
6. **View achievements** → See unlocked badges

---

## 📁 What's Included in APK

| Feature | Status |
|---------|--------|
| Math Lessons | ✅ Yes |
| Romanian Lessons | ✅ Yes |
| Gamification (XP, Levels) | ✅ Yes |
| Achievements & Badges | ✅ Yes |
| Progress Tracking | ✅ Yes |
| AI Assistant | ✅ Yes |
| Quiz System | ✅ Yes |
| Beautiful UI/Animations | ✅ Yes |
| Works Offline | ❌ No (needs internet) |
| User Registration | ✅ Yes (but demo works too) |

---

## 🔑 How Demo Login Works

```javascript
User clicks demo button
         ↓
Frontend auto-fills:
  Email: test@edupex.com
  Password: test123
         ↓
POST request to backend
         ↓
Backend verifies in MongoDB
         ↓
Backend generates JWT token
         ↓
Token stored in browser
         ↓
User logged in ✅
         ↓
Can access all lessons, quizzes, etc.
```

---

## 📋 Before Distributing APK - Checklist

- [x] Backend deployed ✅
- [x] Test user created ✅
- [x] Demo button on login page ✅
- [x] Credentials hardcoded ✅
- [x] APK builds successfully ✅
- [ ] Test on actual device
- [ ] Verify demo login works
- [ ] Verify lessons load
- [ ] Verify no errors

---

## 🎓 Features Once Logged In

### Dashboard
- XP points and level
- Streak counter (consecutive days)
- Hearts/lives system
- Daily goal progress

### Lessons
- Math (Natural numbers, Fractions, Geometry)
- Romanian Language (Grammar, Literature)
- Each lesson has interactive questions
- Immediate feedback on answers

### Quizzes
- Complete quiz = earn XP
- Multiple choice questions
- Progress tracking per lesson

### Achievements
- Unlock badges
- Streak milestones
- Level milestones
- Leaderboards (future)

### AI Assistant
- Contextual help
- Curriculum-aligned answers
- Virtual teacher

---

## 🐛 Troubleshooting

### APK won't install
```bash
# Uninstall first
adb uninstall com.edupex.app
# Then reinstall
adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

### Demo button not working
1. Verify backend is running: `curl https://edupex-backend.onrender.com/api/`
2. Check browser console for errors (F12)
3. Rebuild APK: `./build-demo-apk.sh`

### Login fails
1. Verify test user: `node backend/checkTestUser.js`
2. Check internet connection on device
3. Check backend logs on Render.com

### Lessons don't show
1. Verify user has correct grade level (5-8)
2. Check that lessons exist in database
3. Check browser console for API errors

---

## 📱 Sharing APK

### Method 1: Direct Installation
```bash
# Send via adb to connected device
adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

### Method 2: Email/Cloud
1. Zip the APK file
2. Send via email or cloud storage (Google Drive, OneDrive, etc.)
3. Recipient downloads and installs

### Method 3: USB Transfer
1. Connect device to laptop
2. Copy APK to device
3. Open file manager on device
4. Tap APK to install

---

## 🔄 API Endpoints (For Reference)

Backend automatically handles:

```
POST   /api/users/login              Register login
POST   /api/users/register           Register new user
GET    /api/users/profile            Get user data
GET    /api/lessons                  List all lessons
GET    /api/lessons/:id              Get lesson details
POST   /api/progress/:lessonId       Save progress
GET    /api/progress                 Get user progress
GET    /api/assistant/help           Get AI help
```

All requests automatically include JWT token.

---

## ⏱️ Timeline

| Task | Time | Status |
|------|------|--------|
| Learn app purpose | 2 min | ✅ Done |
| Understand architecture | 3 min | ✅ Done |
| Verify test user | 2 min | ✅ Ready |
| Build APK | 10 min | 🔄 Next |
| Install on device | 3 min | 🔄 Next |
| Test features | 5 min | 🔄 Next |
| **Total** | **25 min** | |

---

## 📞 Files for Reference

If you need details:

1. **DEPLOYMENT_SUMMARY.md** - Complete overview
2. **APK_BUILD_DEPLOYMENT_GUIDE.md** - Step-by-step instructions
3. **HARDCODED_CREDENTIALS_GUIDE.md** - Technical deep dive
4. **APPLICATION_USAGE_GUIDE.md** - Features and usage

---

## 🎉 You're Ready!

### What's Already Done
✅ Backend is deployed  
✅ Test user is created  
✅ Frontend has demo button  
✅ Credentials are hardcoded  
✅ Build script is ready  

### What You Do
1. Run `./build-demo-apk.sh`
2. Wait 10-15 minutes
3. Install APK on device
4. Click demo button
5. Start learning!

---

## ❓ Quick FAQ

**Q: Do I need Android Studio?**  
A: No, the build script handles everything

**Q: How big is the APK?**  
A: ~50-70 MB (debug), ~35-50 MB (release)

**Q: Can users make accounts?**  
A: Yes, registration works, but demo button makes it easier

**Q: Will it work offline?**  
A: No, needs internet connection to backend

**Q: What if backend crashes?**  
A: App won't work until backend is back up

**Q: How long do users stay logged in?**  
A: Token expires in 7 days

---

## 🚀 Start Building Now!

```bash
# Everything you need to run:
cd /Users/mdica/PycharmProjects/EduPex
./build-demo-apk.sh
```

That's it! 🎓📱


