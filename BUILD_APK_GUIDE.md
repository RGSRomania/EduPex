# 📱 Building EduPex APK with Demo Login

## ✅ What's Been Done

### 1. Added Demo Login Feature
- ✅ Added "🎓 Intră cu Cont Demo" button to login page
- ✅ Hardcoded credentials: `test@edupex.com` / `test123`
- ✅ One-click demo login - no typing required!

### 2. Created Build Script
- ✅ Created `build-demo-apk.sh` for easy APK generation
- ✅ Automatically configures for Android emulator backend
- ✅ Builds debug APK (no signing required)

---

## 🚀 Quick Start - Build APK

### Option 1: Use the Build Script (Recommended)

```bash
cd /Users/mdica/PycharmProjects/EduPex
./build-demo-apk.sh
```

This will:
1. Install dependencies
2. Build React app
3. Sync with Capacitor
4. Generate debug APK

**Output:** `frontend/android/app/build/outputs/apk/debug/app-debug.apk`

### Option 2: Manual Build

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend

# Build React app
npm run build

# Sync with Capacitor
npx cap sync android

# Build APK
cd android
./gradlew assembleDebug
```

---

## 📦 Installing the APK

### Method 1: USB Installation
```bash
# Connect Android device via USB
# Enable USB debugging on device
adb install -r frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

### Method 2: File Transfer
1. Copy `app-debug.apk` to your phone
2. Open file and tap "Install"
3. Allow installation from unknown sources if prompted

### Method 3: Share via Cloud
1. Upload APK to Google Drive / Dropbox / WeTransfer
2. Share link with recipient
3. Download on Android device and install

---

## 🎓 Using Demo Login

### For Users Receiving the APK:

**Option A: Demo Button (Easiest)**
1. Open the app
2. Click **"🎓 Intră cu Cont Demo"** button
3. ✅ Automatically logged in!

**Option B: Manual Entry**
1. Open the app
2. Enter:
   - Email: `test@edupex.com`
   - Password: `test123`
3. Click "Autentificare"

---

## ⚠️ Important Notes

### Backend Requirement
The app needs to connect to a backend server. You have two options:

#### Option 1: Local Backend (Current Setup)
- The APK is configured to connect to `http://10.0.2.2:5000/api`
- This works **only on Android emulators**
- ❌ Won't work on real devices unless backend is accessible

#### Option 2: Deploy Backend First (Recommended for Distribution)
If sending APK to others, deploy backend first:

```bash
# Deploy to Render.com (free tier available)
cd backend
./deploy-to-render.sh
```

Then rebuild APK with production backend:
```bash
cd frontend
REACT_APP_API_URL=https://your-backend.onrender.com/api npm run build
npx cap sync android
cd android && ./gradlew assembleDebug
```

---

## 🔧 Troubleshooting

### "App won't connect to backend"
**Solution:** Deploy backend to cloud service first, then rebuild APK with production URL

### "Installation blocked"
**Solution:** Enable "Install unknown apps" in Android settings

### "Gradle build failed"
**Solution:** Ensure you have Java 11 or later installed
```bash
java -version
# If needed: brew install openjdk@21
```

### "Demo login doesn't work"
**Solution:** Verify test user exists in database:
```bash
cd backend
node checkTestUser.js
```

---

## 📋 Checklist Before Sending APK

- ✅ Demo login feature added
- ⚠️ Backend deployed and accessible (or running locally)
- ✅ APK built successfully
- ⚠️ Test APK on a real Android device
- ✅ Verify demo login works
- ✅ Test AI assistant works
- ✅ Test lessons load correctly

---

## 🎯 For Recipients

When you receive the APK:

1. **Download** the APK file to your Android device
2. **Allow** installation from unknown sources (in Settings)
3. **Install** by tapping the APK file
4. **Open** the EduPex app
5. **Click** "🎓 Intră cu Cont Demo" for instant access

That's it! No registration needed.

---

## 🔐 Demo Account Details

**Email:** test@edupex.com  
**Password:** test123

**User Info:**
- Name: Test User
- Grade Level: 5
- XP: 0 (fresh account)
- Subjects: Mathematics & Romanian

---

## 📱 APK Details

**Package Name:** com.edupex.app  
**Version:** Check `frontend/package.json`  
**Build Type:** Debug (development)  
**Signed:** No (debug builds don't require signing)

For **production/Play Store release**, you need to:
1. Create a signing key
2. Use `./gradlew assembleRelease`
3. Configure `keystore.properties`

---

## 🚀 Next Steps

### To share the APK now:
```bash
# Find the APK
ls -lh frontend/android/app/build/outputs/apk/debug/app-debug.apk

# Share via any method (USB, email, cloud storage)
```

### To prepare for production:
1. Deploy backend to Render/Railway/Heroku
2. Update API URL in build script
3. Create signing key for release build
4. Follow Play Store submission guidelines

---

## 💡 Tips

- **Demo button** is styled with a gradient purple color for easy identification
- **Auto-fill** happens when clicking demo button - no typing needed
- **Test user** has full access to all features
- **Backend** can be local (for testing) or deployed (for distribution)

---

**Ready to build?** Run: `./build-demo-apk.sh`

**Questions?** Check troubleshooting section above or the `AI_ASSISTANT_FIX.md` document.

