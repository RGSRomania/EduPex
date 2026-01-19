# EduPex Application - Usage Guide

## 📚 Application Overview

**EduPex** is an educational mobile application designed for learning Math and Romanian language, following the Romanian school curriculum (grades 5-8). It uses gamification strategies similar to Duolingo to make learning engaging and fun.

### Target Users
- Students in grades 5-8 in Romania
- Focus on curriculum-aligned content for Mathematics and Romanian Language

---

## 🎮 Core Features

### 1. **Gamification System**
- **XP & Levels**: Earn experience points and level up
- **Streak System**: Track consecutive days of learning
- **Hearts/Lives**: Limited attempts with wrong answers
- **Daily Quests**: Missions with XP rewards
- **Achievements**: Unlockable badges and trophies
- **Leaderboards**: Compete with other learners

### 2. **Educational Content**
- **Interactive Lessons**: Multiple choice, fill-in-the-blank, true/false questions
- **Immediate Feedback**: Answer validation with explanations
- **Video Lessons**: Organized by subjects and grades
- **AI Assistant**: Virtual teacher providing contextual help
- **Skill Trees**: Visual learning paths with unlockable lessons

### 3. **User Experience**
- **Home Dashboard**: Personal stats, course overview, daily goals
- **Course Navigation**: Mathematics and Romanian Language skill trees
- **Progress Visualization**: Visual tracking of advancement
- **Responsive Design**: Works on all devices
- **Smooth Animations**: Modern transitions and effects

---

## 🏗️ Application Architecture

### **Backend (Node.js + Express)**
- **Database**: MongoDB for user data, lessons, progress, achievements
- **Authentication**: JWT token-based authentication
- **API Routes**:
  - `/api/users` - User authentication, registration, profile
  - `/api/lessons` - Course content and lesson data
  - `/api/progress` - User progress tracking
  - `/api/assistant` - AI assistant interactions
- **AI Integration**: GPT-4.0 powered assistant via OpenAI API
- **External Services**: Supabase integration for some features

### **Frontend (React + Capacitor)**
- **UI Framework**: React with React Router for navigation
- **State Management**: Redux with Redux Thunk for async actions
- **Styling**: Styled Components for CSS-in-JS
- **Animations**: Framer Motion for smooth transitions
- **Mobile Build**: Capacitor for converting React web app to APK
- **API Communication**: Axios for HTTP requests
- **Charts**: Chart.js for progress visualization

### **Database Schema**
- **Users**: email, username, password (hashed), firstName, lastName, gradeLevel, xp, level, hearts, streak
- **Lessons**: title, description, subject, gradeLevel, questions, content, video links
- **Progress**: userId, lessonId, completed, score, attemptCount, completedAt
- **Achievements**: userId, badgeId, unlockedAt, type (streak, level, quiz)

---

## 🔐 Authentication & Credentials

### Current Test User
**For APK distribution and testing without network access:**

| Field | Value |
|-------|-------|
| Email | `test@edupex.com` |
| Password | `test123` |
| Username | `testedupex` |
| First Name | `Test` |
| Last Name | `User` |
| Grade Level | 5 |

This user is hardcoded in the Login page for quick demo access.

### Creating Additional Test Users
You can create new test users either:

1. **Via Backend Script** (if MongoDB is running):
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
node checkTestUser.js
```

2. **Via Registration Page**: Use the frontend registration form to create new accounts

---

## 📱 Building APK for Offline Device Access

### Key Configuration

Since your device is not on the same network, you need to use a **publicly deployed backend**:

#### Current Configuration (in `frontend/src/config/apiConfig.js`):
```javascript
// Production environment - use deployed backend
if (process.env.NODE_ENV === 'production') {
  return 'https://edupex-backend.onrender.com/api';  // Deployed backend
}

// Android emulator (if testing locally)
if (platform === 'android') {
  return 'http://10.0.2.2:5000/api';
}
```

### Option 1: Build APK with Hardcoded Backend URL

**For production/offline devices**, the APK will use the deployed backend: `https://edupex-backend.onrender.com/api`

#### Build Steps:

1. **Ensure Backend is Deployed**
   - Backend is already deployed on Render.com
   - Verify it's running at: `https://edupex-backend.onrender.com/api`

2. **Build the APK**
   ```bash
   cd /Users/mdica/PycharmProjects/EduPex
   ./build-demo-apk.sh
   ```
   
   Or manually:
   ```bash
   cd frontend
   npm install
   npm run build
   npx cap sync android
   cd android
   ./gradlew assembleDebug
   ```

3. **Install on Device**
   ```bash
   # Via ADB (Android Debug Bridge)
   adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk
   
   # Or transfer the APK file and install manually on the device
   ```

### Option 2: Change Backend URL Before Building

If you want to use a different backend URL, edit `frontend/src/config/apiConfig.js`:

```javascript
export const getApiBaseUrl = () => {
  // Change this to your deployed backend URL
  if (process.env.NODE_ENV === 'production') {
    return 'https://your-deployed-backend.com/api';  // Your backend URL
  }
  // ... rest of code
};
```

---

## 🔄 API Flow for Login

1. **User enters credentials** on Login page
2. **Frontend sends POST request** to `/api/users/login` with email and password
3. **Backend verifies credentials** against MongoDB
4. **Backend returns JWT token** and user data
5. **Frontend stores token** in localStorage
6. **Token is included** in all subsequent API requests via Authorization header

### Demo Login Flow (Hardcoded)
- Click "🎓 Intră cu Cont Demo" button
- Automatically fills form with `test@edupex.com` / `test123`
- Performs login without typing

---

## 📋 APK Deployment Checklist

Before distributing the APK:

- ✅ Test user `test@edupex.com` is created in backend database
- ✅ Demo login button is present on Login page
- ✅ Backend is deployed and accessible (Render.com)
- ✅ APK hardcodes production backend URL (no local network needed)
- ✅ API configuration automatically detects production environment
- ✅ All hardcoded credentials are in place
- ✅ APK is built in release/production mode for smaller size

---

## 🚀 Quick Commands

### Development
```bash
# Start backend
cd backend
npm install
npm start  # Runs on http://localhost:5000

# Start frontend (in another terminal)
cd frontend
npm install
npm start  # Runs on http://localhost:3000
```

### Testing
```bash
# Check test user exists
cd backend
node checkTestUser.js

# Check backend connectivity
curl https://edupex-backend.onrender.com/api/
```

### Building APK
```bash
# Automatic build script
./build-demo-apk.sh

# Manual build
cd frontend
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
```

### Installing APK
```bash
# Via ADB
adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk

# Manual installation
# Transfer APK to device and tap to install
```

---

## 📁 Key File Locations

| Purpose | Location |
|---------|----------|
| Login Page | `frontend/src/pages/Login.js` |
| API Config | `frontend/src/config/apiConfig.js` |
| API Utilities | `frontend/src/utils/api.js` |
| Backend Server | `backend/server.js` |
| User Model | `backend/models/User.js` |
| User Routes | `backend/routes/userRoutes.js` |
| Test User Script | `backend/checkTestUser.js` |
| Build Script | `build-demo-apk.sh` |

---

## 🔗 Important URLs

| Purpose | URL |
|---------|-----|
| Deployed Backend API | `https://edupex-backend.onrender.com/api` |
| Local Backend (dev) | `http://localhost:5000/api` |
| Frontend (dev) | `http://localhost:3000` |
| Android Emulator Localhost | `http://10.0.2.2:5000/api` |

---

## 📝 Notes for APK Distribution

1. **Hardcoded Credentials**: The test user credentials are hardcoded in the Login page component. Users can:
   - Click "🎓 Intră cu Cont Demo" for instant access
   - Manually enter credentials: `test@edupex.com` / `test123`

2. **No Network Required**: The APK connects to the deployed backend on Render.com, so it works on any device with internet connection (doesn't need to be on same network).

3. **APK Size**: Debug APK is ~50-70MB. For production distribution, consider building a release APK.

4. **Offline Features**: Currently, most features require backend connection. To add offline support:
   - Implement local SQLite database with React Native SQLite
   - Sync data when connection is available
   - Cache lessons and content locally

---

## 🐛 Troubleshooting

### APK Won't Connect to Backend
- Verify backend is running: `curl https://edupex-backend.onrender.com/api/`
- Check internet connection on device
- Rebuild APK if URLs were changed

### Login Fails
- Verify test user exists: `node backend/checkTestUser.js`
- Check user database in MongoDB
- Verify backend error logs

### Demo Login Button Not Working
- Ensure frontend is rebuilt: `npm run build`
- Check browser console for errors
- Verify API configuration in `apiConfig.js`

---

## 📚 For Future Development

Consider implementing:
1. **Offline Sync**: Local storage with cloud sync
2. **Push Notifications**: Daily learning reminders
3. **Social Features**: Friend connections and challenges
4. **Analytics**: Track user learning patterns
5. **Performance Optimization**: Lazy loading, code splitting
6. **Release Build**: Signed APK for Play Store submission


