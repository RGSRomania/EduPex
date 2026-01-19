# 📚 EduPex Documentation Index

## Welcome! 👋

This document guides you through all the documentation created for the EduPex project.

---

## 🎯 Quick Navigation

### ⚡ For the Impatient (5 minutes)
1. **Start here**: `QUICK_START.md` - Overview and 30-minute build guide
2. **Build command**: `./build-demo-apk.sh`
3. **Done!**

### 📖 For Complete Understanding (30 minutes)
1. `APPLICATION_USAGE_GUIDE.md` - Learn what EduPex is and how it works
2. `DEPLOYMENT_SUMMARY.md` - Overview of deployment architecture
3. `TECHNICAL_DIAGRAMS.md` - Visual diagrams of system architecture
4. `APK_BUILD_DEPLOYMENT_GUIDE.md` - Step-by-step build instructions

### 🔬 For Technical Deep Dive (1 hour)
1. `HARDCODED_CREDENTIALS_GUIDE.md` - Technical details on authentication
2. `TECHNICAL_DIAGRAMS.md` - Complete system architecture
3. Source code in `frontend/src/` and `backend/`

---

## 📋 Document Guide

### 1. **QUICK_START.md** ⭐ START HERE
**Purpose**: Fast overview for people who just want to build the APK  
**Length**: 5-10 minutes to read  
**Contains**:
- What is EduPex (simple explanation)
- 3-step APK build process
- Test credentials
- Basic troubleshooting

**Read this if**: You want to build and deploy quickly

---

### 2. **APPLICATION_USAGE_GUIDE.md**
**Purpose**: Comprehensive guide to the EduPex application  
**Length**: 20 minutes to read  
**Contains**:
- Complete application overview
- Feature descriptions (gamification, lessons, AI, etc.)
- Architecture explanation (backend, frontend, database)
- Authentication flow
- APK checklist
- File locations
- Troubleshooting
- Future development ideas

**Read this if**: You want to understand what the app does

---

### 3. **DEPLOYMENT_SUMMARY.md**
**Purpose**: Executive summary of the entire project  
**Length**: 15 minutes to read  
**Contains**:
- What has been configured (backend, test user, demo button)
- How users will use it
- Architecture overview (diagram)
- Complete build & deploy instructions
- Credentials summary
- Quick reference commands
- Security notes
- FAQ

**Read this if**: You want complete overview before deployment

---

### 4. **APK_BUILD_DEPLOYMENT_GUIDE.md**
**Purpose**: Detailed step-by-step build and deployment instructions  
**Length**: 30 minutes to read  
**Contains**:
- Prerequisites (Node, Android SDK, Java, etc.)
- Step 1: Verify test user in database
- Step 2: Verify backend is deployed
- Step 3: Verify frontend configuration
- Step 4: Build APK (automatic or manual)
- Step 5: Install on device (ADB or manual)
- Step 6: Test the application
- APK output locations
- File size information
- Pre-distribution checklist
- Quick command reference
- Troubleshooting guide

**Read this if**: You want detailed instructions for each step

---

### 5. **HARDCODED_CREDENTIALS_GUIDE.md**
**Purpose**: Technical deep dive on authentication and hardcoded credentials  
**Length**: 25 minutes to read  
**Contains**:
- How hardcoded credentials work
- Test user details (test@edupex.com / test123)
- Frontend demo button implementation
- Backend login route
- Complete login flow (step-by-step)
- API endpoints
- Setting up credentials
- Verification methods (cURL, console, APK)
- Security considerations
- How to change credentials
- Test user data structure
- Testing checklist

**Read this if**: You want to understand authentication in detail

---

### 6. **TECHNICAL_DIAGRAMS.md**
**Purpose**: Visual diagrams of system architecture  
**Length**: 15 minutes to read  
**Contains**:
- System architecture overview (ASCII art)
- User login flow (complete sequence)
- File structure and hardcoded elements
- API call sequence with tokens
- Gamification system architecture
- Build & deployment pipeline
- Database schema overview

**Read this if**: You prefer visual representations of architecture

---

## 🎯 Recommended Reading Path

### Path A: Just Build It (Quick)
1. ✅ This file (overview)
2. ✅ QUICK_START.md (5 min)
3. ✅ Run `./build-demo-apk.sh` (15 min)
4. ✅ Install APK on device (5 min)
5. ✅ Done! (25 minutes total)

### Path B: Understand & Build (Standard)
1. ✅ This file (overview)
2. ✅ APPLICATION_USAGE_GUIDE.md (10 min)
3. ✅ DEPLOYMENT_SUMMARY.md (10 min)
4. ✅ APK_BUILD_DEPLOYMENT_GUIDE.md (10 min)
5. ✅ Run build script (15 min)
6. ✅ Install & test (10 min)
7. ✅ Done! (55 minutes total)

### Path C: Complete Mastery (Thorough)
1. ✅ This file (overview)
2. ✅ APPLICATION_USAGE_GUIDE.md (10 min)
3. ✅ DEPLOYMENT_SUMMARY.md (10 min)
4. ✅ TECHNICAL_DIAGRAMS.md (10 min)
5. ✅ APK_BUILD_DEPLOYMENT_GUIDE.md (10 min)
6. ✅ HARDCODED_CREDENTIALS_GUIDE.md (15 min)
7. ✅ Explore source code (30 min)
8. ✅ Run build script (15 min)
9. ✅ Install & test (10 min)
10. ✅ Done! (2 hours total)

---

## 🚀 What the Docs Cover

### Architecture
- ✅ Frontend (React + Capacitor)
- ✅ Backend (Node.js/Express)
- ✅ Database (MongoDB)
- ✅ API Communication
- ✅ Authentication (JWT)

### Features
- ✅ Math & Romanian lessons
- ✅ Gamification system
- ✅ Achievement tracking
- ✅ Progress visualization
- ✅ AI assistant
- ✅ Quiz system

### Deployment
- ✅ APK building process
- ✅ Device installation
- ✅ Backend deployment (Render.com)
- ✅ Test credentials setup
- ✅ Hardcoded configuration

### Testing & Troubleshooting
- ✅ Verification steps
- ✅ Common issues & solutions
- ✅ Debug procedures
- ✅ Test checklists

---

## 📁 Quick File Reference

| Document | Purpose | Read Time |
|----------|---------|-----------|
| QUICK_START.md | Get started fast | 5 min |
| APPLICATION_USAGE_GUIDE.md | Understand the app | 20 min |
| DEPLOYMENT_SUMMARY.md | Executive overview | 15 min |
| APK_BUILD_DEPLOYMENT_GUIDE.md | Build instructions | 30 min |
| HARDCODED_CREDENTIALS_GUIDE.md | Auth details | 25 min |
| TECHNICAL_DIAGRAMS.md | Visual architecture | 15 min |

---

## 🎓 Key Concepts Explained Across Docs

### Hardcoded Credentials
- **What**: Test user `test@edupex.com` / `test123`
- **Where**: Docs 2, 3, 4, 5
- **Why**: One-click demo login without typing
- **Files**: `frontend/src/pages/Login.js`, `backend/models/User.js`

### API Configuration
- **What**: Production backend URL hardcoded in APK
- **Where**: Docs 3, 4, 6
- **Why**: Device works from anywhere (not same network)
- **Files**: `frontend/src/config/apiConfig.js`

### APK Building
- **What**: Converting React web app to Android APK
- **Where**: Docs 1, 4
- **Why**: Can install on any Android device
- **Files**: `build-demo-apk.sh`, Gradle config

### Authentication Flow
- **What**: Login → Backend → JWT → localStorage
- **Where**: Docs 5, 6
- **Why**: Secure API communication
- **Files**: `frontend/src/utils/api.js`, `backend/routes/userRoutes.js`

---

## ✅ Pre-Deployment Checklist

Before distributing APK, verify:

- [ ] Backend deployed at https://edupex-backend.onrender.com/api
- [ ] Test user `test@edupex.com` created in MongoDB
- [ ] Frontend has demo login button
- [ ] Hardcoded credentials in `Login.js` are correct
- [ ] API configuration points to production backend
- [ ] APK builds successfully
- [ ] Demo login works on test device
- [ ] Lessons load and quizzes work
- [ ] No console errors

---

## 🔗 Related Files in Project

### Frontend Code
```
frontend/
├── src/
│   ├── pages/
│   │   └── Login.js                    ← Demo button & credentials
│   ├── config/
│   │   └── apiConfig.js                ← Backend URL
│   ├── utils/
│   │   └── api.js                      ← API client
│   └── components/
│       └── Dashboard/...               ← Main UI
├── build/                              ← React production build
└── android/
    ├── app/
    │   └── build/outputs/apk/
    │       └── debug/app-debug.apk    ← Final APK
    └── gradle configs
```

### Backend Code
```
backend/
├── server.js                           ← Express server
├── checkTestUser.js                    ← Create test user
├── models/
│   └── User.js                         ← User schema
├── routes/
│   ├── userRoutes.js                   ← Login/Auth
│   ├── lessonRoutes.js
│   ├── progressRoutes.js
│   └── aiAssistantRoutes.js
└── .env                                ← Config (MongoDB, JWT secret)
```

### Build & Config
```
/
├── build-demo-apk.sh                   ← Automatic build script
├── QUICK_START.md                      ← This documentation
├── APPLICATION_USAGE_GUIDE.md
├── DEPLOYMENT_SUMMARY.md
├── APK_BUILD_DEPLOYMENT_GUIDE.md
├── HARDCODED_CREDENTIALS_GUIDE.md
├── TECHNICAL_DIAGRAMS.md
└── .env files                          ← Configuration
```

---

## 🎯 Success Criteria

After following the docs, you should be able to:

✅ Explain what EduPex is  
✅ Understand the architecture  
✅ Build an APK with one command  
✅ Install APK on a device  
✅ Login with demo credentials  
✅ Access all features (lessons, quizzes, etc.)  
✅ Understand how hardcoded credentials work  
✅ Troubleshoot common issues  

---

## 📞 Key Commands Reference

```bash
# Check test user
cd backend && node checkTestUser.js

# Build APK (automatic)
cd /Users/mdica/PycharmProjects/EduPex && ./build-demo-apk.sh

# Build APK (manual steps)
cd frontend && npm install && npm run build && npx cap sync android && cd android && ./gradlew assembleDebug

# Install on device
adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk

# Check backend
curl https://edupex-backend.onrender.com/api/

# Open APK folder
open frontend/android/app/build/outputs/apk/debug/
```

---

## 🎉 Final Notes

The documentation is structured to accommodate different learning styles:

- **Readers who prefer quick overviews**: Start with QUICK_START.md
- **Visual learners**: Check TECHNICAL_DIAGRAMS.md
- **Step-by-step followers**: Use APK_BUILD_DEPLOYMENT_GUIDE.md
- **Technical deep-divers**: Read HARDCODED_CREDENTIALS_GUIDE.md

All documents cross-reference each other, so you can jump between them as needed.

**Start with QUICK_START.md** - it's the fastest path to getting the APK built and deployed! 🚀

---

## 📝 Document Version Info

Created: January 10, 2026  
For: EduPex Educational Platform  
Purpose: APK deployment with hardcoded test credentials  
Audience: Developers, QA, and deployment teams  

All documents are consistent and work together as a complete guide.

---

Happy deploying! 🎓📱

