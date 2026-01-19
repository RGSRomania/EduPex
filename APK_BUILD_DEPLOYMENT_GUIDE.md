# 🚀 EduPex APK Build & Deployment Guide

## 📋 Prerequisites

Before building the APK, ensure you have:

1. **Node.js & npm** installed
   ```bash
   node --version  # Should be v16+
   npm --version   # Should be v8+
   ```

2. **Android SDK** installed (for building APK)
   - Android SDK Build Tools 34+
   - Android SDK Platform 34+
   - Android Emulator or physical device

3. **Java Development Kit (JDK)**
   ```bash
   java -version   # Should be JDK 11+
   ```

4. **Capacitor CLI** (will be installed with npm)

5. **Gradle** (included in android folder)

---

## ✅ Step 1: Verify Test User Exists

The application uses hardcoded test credentials for easy APK distribution.

### Check if test user exists in database:

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
npm install
node checkTestUser.js
```

Expected output:
```
✅ Connected to MongoDB
✅ Test user exists!
Email: test@edupex.com
Username: testedupex
First Name: Test
Last Name: User
Grade Level: 5
Password "test123" is valid: true

📝 You can now login with:
   Email: test@edupex.com
   Password: test123
```

**If test user doesn't exist**, the script will create it automatically.

---

## ✅ Step 2: Verify Backend is Deployed

The APK needs to connect to a deployed backend (since devices won't be on the same network).

### Check backend status:

```bash
# Test if backend is running
curl https://edupex-backend.onrender.com/api/

# Expected response:
# "EduPex API is running"
```

**Current Backend**: `https://edupex-backend.onrender.com/api`

If the backend is not deployed, you need to deploy it first:

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend

# Deploy to Render.com (if not already deployed)
# Instructions: Follow DEPLOYMENT.md or BACKEND_DEPLOYMENT.md
```

---

## ✅ Step 3: Verify Frontend Configuration

The frontend automatically uses the production backend URL when built for production.

Check `/Users/mdica/PycharmProjects/EduPex/frontend/src/config/apiConfig.js`:

```javascript
export const getApiBaseUrl = () => {
  if (process.env.REACT_APP_API_URL) {
    return process.env.REACT_APP_API_URL;
  }

  if (process.env.NODE_ENV === 'production') {
    return 'https://edupex-backend.onrender.com/api';  // ✅ Production backend
  }
  // ... rest of code
};
```

**The production backend URL is already hardcoded!** ✅

---

## 🔨 Step 4: Build the APK

### Option A: Use the Build Script (Recommended)

```bash
cd /Users/mdica/PycharmProjects/EduPex

# Make the script executable (if not already)
chmod +x build-demo-apk.sh

# Run the build script
./build-demo-apk.sh
```

This script will:
1. ✅ Install frontend dependencies
2. ✅ Build React app for production
3. ✅ Sync with Capacitor
4. ✅ Build debug APK with Gradle
5. ✅ Output APK location

### Option B: Manual Build (Step-by-Step)

```bash
# Step 1: Navigate to frontend
cd /Users/mdica/PycharmProjects/EduPex/frontend

# Step 2: Install dependencies (if not already installed)
npm install

# Step 3: Build React app for production
npm run build

# Step 4: Sync with Capacitor
npx cap sync android

# Step 5: Build the APK
cd android
./gradlew assembleDebug

# The APK will be at:
# /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

**Build time**: 5-15 minutes depending on your machine

---

## 📱 Step 5: Install APK on Device

### Option A: Using ADB (Android Debug Bridge)

1. **Enable USB Debugging** on your Android device:
   - Settings → About Phone → Tap Build Number 7 times
   - Back to Settings → Developer Options → Enable USB Debugging

2. **Connect device via USB**

3. **Install APK**:
   ```bash
   adb install /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
   ```

### Option B: Manual Installation

1. **Transfer APK to device**:
   - Via email, WhatsApp, cloud storage, etc.
   - Or copy to device via USB

2. **On the device**:
   - Open file manager
   - Find the APK file
   - Tap to install
   - Grant permissions if prompted

3. **Launch the app** from home screen

---

## ✅ Step 6: Test the Application

Once installed, test the following:

### 1. Launch App
   - App should start without errors
   - Should see EduPex logo and login page

### 2. Test Demo Login
   - Click "🎓 Intră cu Cont Demo" button
   - Should automatically populate credentials
   - Should navigate to Dashboard

### 3. Test Manual Login
   - Enter: `test@edupex.com`
   - Enter: `test123`
   - Click "Autentificare"
   - Should see Dashboard with XP, level, etc.

### 4. Test Dashboard Features
   - View XP points and level
   - View hearts and streak
   - Access lessons
   - View achievements

### 5. Test Lesson Access
   - Navigate to Lessons section
   - Should see Math and Romanian language courses
   - Should be able to open lessons
   - Should see quiz questions

---

## 🐛 Troubleshooting

### APK Installation Fails
```bash
# Uninstall previous version
adb uninstall com.edupex.app

# Try installing again
adb install /path/to/app-debug.apk

# Or install with reinstall flag
adb install -r /path/to/app-debug.apk
```

### App Crashes on Startup
- Check logcat for errors: `adb logcat`
- Verify backend is running: `curl https://edupex-backend.onrender.com/api/`
- Check app console in browser DevTools

### Login Fails with "Cannot Connect"
```bash
# Verify backend connectivity
curl -X POST https://edupex-backend.onrender.com/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@edupex.com","password":"test123"}'

# Expected response should include token and user data
```

### Demo Button Not Visible
- Rebuild APK: `npm run build && npx cap sync android`
- Clear app cache: `adb shell pm clear com.edupex.app`
- Reinstall APK

### User Can't Complete Lessons
- Verify test user has correct grade level (5-8)
- Check if lessons are in database
- Verify progress endpoint: `curl https://edupex-backend.onrender.com/api/progress/`

---

## 📊 APK Build Output

### Expected File Locations
```
/Users/mdica/PycharmProjects/EduPex/
├── frontend/
│   ├── build/                          # React production build
│   │   ├── index.html
│   │   ├── static/
│   │   └── ...
│   ├── android/
│   │   ├── app/
│   │   │   └── build/
│   │   │       └── outputs/
│   │   │           └── apk/
│   │   │               └── debug/
│   │   │                   └── app-debug.apk  # ✅ FINAL APK FILE
│   │   └── ...
│   └── ...
└── ...
```

### APK File Size
- Debug APK: ~50-70 MB
- Release APK: ~35-50 MB (if built for Play Store)

---

## 🔐 Hardcoded Credentials in APK

### For Testing
These credentials are built into the APK:

| Field | Value |
|-------|-------|
| **Email** | `test@edupex.com` |
| **Password** | `test123` |

### How to Use
1. **Auto-fill**: Click "🎓 Intră cu Cont Demo" button
2. **Manual**: Type credentials in login form

### Important Notes
⚠️ **For production APK submission to Play Store:**
- Remove hardcoded demo login button before release
- Implement proper authentication
- Never hardcode real credentials in production APKs

---

## 📋 Checklist Before Distribution

Before sending APK to the device user:

- [ ] Test user `test@edupex.com` exists in backend database
- [ ] Backend is deployed and accessible (https://edupex-backend.onrender.com/api)
- [ ] Frontend API configuration points to production backend
- [ ] React app is built in production mode (`npm run build`)
- [ ] APK is built with debug or release keystore
- [ ] Login page has demo login button
- [ ] Demo button works correctly
- [ ] APK file exists at expected location
- [ ] APK installs without errors
- [ ] Login works with test credentials
- [ ] Dashboard loads after login
- [ ] Lessons are accessible
- [ ] No console errors in browser DevTools

---

## 🚀 Quick Commands Reference

```bash
# Navigate to project
cd /Users/mdica/PycharmProjects/EduPex

# Check test user
cd backend && node checkTestUser.js

# Check backend status
curl https://edupex-backend.onrender.com/api/

# Build APK (automatic)
./build-demo-apk.sh

# Build APK (manual)
cd frontend && npm run build && npx cap sync android && cd android && ./gradlew assembleDebug

# Install APK
adb install frontend/android/app/build/outputs/apk/debug/app-debug.apk

# Check APK file
ls -lh frontend/android/app/build/outputs/apk/debug/app-debug.apk

# View APK in file explorer
open frontend/android/app/build/outputs/apk/debug/
```

---

## 📚 Additional Resources

- **README.md**: EduPex application overview
- **APPLICATION_USAGE_GUIDE.md**: How to use the app
- **DEPLOYMENT.md**: Deployment instructions
- **BACKEND_DEPLOYMENT.md**: Backend deployment details
- **.env.example** (if exists): Environment configuration

---

## ✨ What's Included in the APK

✅ Complete EduPex application
✅ Math lessons (grades 5-8)
✅ Romanian language lessons
✅ Gamification system (XP, levels, streaks, hearts)
✅ AI assistant integration
✅ Achievement system
✅ Progress tracking
✅ User dashboard
✅ Responsive UI with animations
✅ Offline support (partial - cached content)
✅ Hardcoded test credentials for demo

---

## 🎯 Next Steps After APK Installation

Once the APK is installed on the device:

1. **Launch the app**
2. **Click "🎓 Intră cu Cont Demo"** for instant access
3. **Explore the dashboard**
4. **Try a lesson**
5. **Complete a quiz**
6. **View achievements**
7. **Check progress tracking**

Enjoy learning! 🎓📚


