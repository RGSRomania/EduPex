# 📱 EduPex APK Build & Installation Guide

## Quick Start (2 steps)

### Step 1: Build APK
```bash
cd /Users/mdica/PycharmProjects/EduPex
bash build-apk-release.sh
```

This will:
- Build React app for production
- Sync web assets with Capacitor
- Generate Android APK
- Output APK location

### Step 2: Install on Device

**Option A: Direct Installation (requires Android device connected via USB)**
```bash
adb install -r "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
```

**Option B: Transfer APK and Install Manually**
1. Copy APK from build output:
   ```bash
   cp "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk" ~/Desktop/edupex.apk
   ```
2. Transfer to device via:
   - Email
   - Google Drive
   - USB file transfer
   - Bluetooth
3. On device: Open file manager → Tap APK → Install

---

## Demo Login Credentials

Once installed, use these to log in:

**Email**: `test@edupex.com`  
**Password**: `test123`

---

## Prerequisites

Ensure you have:
- Node.js installed
- Java JDK installed  
- Android SDK (optional - script checks if available)
- Gradle (included in Capacitor project)

Check prerequisites:
```bash
node --version
npm --version
java -version
```

---

## Build Process Details

The build script (`build-apk-release.sh`) does:

1. **Install Dependencies**
   - Installs npm packages if needed
   - Takes ~2-3 minutes first time

2. **Build React Production Bundle**
   - Minifies and optimizes React code
   - Targets production API: `https://edupex-backend.onrender.com/api`
   - Takes ~1-2 minutes

3. **Sync Capacitor Assets**
   - Copies web assets to Android project
   - Prepares for native compilation
   - Takes ~30 seconds

4. **Compile Android APK**
   - Gradle compiles Java/Kotlin code
   - Packages everything into APK
   - Takes ~3-5 minutes

**Total build time: 5-10 minutes** (first time is slower)

---

## APK Details

### File Location
```
/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

### APK Type
- **Debug APK**: Unsigned, for testing and development
- Installable on any device
- Can be sideloaded (manually installed)

### Why Debug vs Release?
- **Debug**: No signing key needed, easier to build
- **Release**: Requires signing key, for Play Store distribution
- For external device testing, debug APK is perfect

---

## Installation Methods

### Method 1: ADB (Android Debug Bridge)
Best if you have USB connection and adb installed.

```bash
# Check if device is connected
adb devices

# Install APK
adb install -r "/path/to/app-debug.apk"

# Uninstall (if needed)
adb uninstall com.edupex.app
```

### Method 2: Direct File Transfer
1. Copy APK to Desktop
2. Send via email/cloud
3. Download on device
4. Tap to install

### Method 3: USB File Transfer
1. Connect device via USB
2. Drag APK to device storage
3. Use device file manager to tap and install

---

## Troubleshooting

### Build Fails with "npm not found"
```bash
# Check Node installation
node --version
npm --version

# If not installed, install from https://nodejs.org
```

### Build Fails with "Java not found"
```bash
# Check Java installation
java -version

# If not installed, install JDK from https://www.oracle.com/java/
```

### APK Installation Fails on Device
- Check "Unknown Sources" is enabled in device settings
- Try `adb install -r` (replace flag forces reinstall)
- Ensure Android version 8.0+ on device

### "Cannot connect to API" after installation
- Check device has internet connection
- Verify backend is running: `curl https://edupex-backend.onrender.com/api/`
- Check device can access external HTTPS URLs

### App Crashes on Startup
- Check Android version (Android 8.0 minimum)
- Check API connectivity
- Check demo credentials are correct: `test@edupex.com` / `test123`

---

## Verification

### Verify Build Success
```bash
ls -lah "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
```

Should show file size and recent modification time.

### Verify Device Installation
```bash
adb shell pm list packages | grep edupex
```

Should show: `package:com.edupex.app`

### Verify App Functionality
1. Install APK
2. Open app
3. See "EduPex" splash screen
4. Tap "Demo Login" button
5. App should auto-fill demo credentials and log in
6. Should see dashboard with lessons

---

## API Configuration

The APK is configured to use:
- **Production API**: `https://edupex-backend.onrender.com/api`
- **Database**: Supabase (configured via backend)
- **LLM**: Groq API for AI Assistant

---

## File Structure

```
EduPex/
├── frontend/
│   ├── src/
│   │   ├── config/
│   │   │   └── apiConfig.js (points to production API)
│   │   ├── pages/
│   │   │   └── Login.js (has demo credentials)
│   │   └── ...
│   ├── android/
│   │   ├── app/
│   │   │   ├── build/ (generated)
│   │   │   │   └── outputs/
│   │   │   │       └── apk/
│   │   │   │           └── debug/
│   │   │   │               └── app-debug.apk ← THIS FILE
│   │   │   └── build.gradle
│   │   └── gradlew
│   ├── package.json
│   ├── capacitor.config.ts
│   └── build/ (generated)
└── build-apk-release.sh ← RUN THIS SCRIPT
```

---

## Next Steps

1. **Run build script**: `bash /Users/mdica/PycharmProjects/EduPex/build-apk-release.sh`
2. **Wait for completion**: Takes 5-10 minutes
3. **Install on device**: Use one of the methods above
4. **Test with demo login**: `test@edupex.com` / `test123`
5. **Share APK**: Can send to others for testing

---

## Support

If you encounter issues:
1. Check prerequisites are installed
2. Review "Troubleshooting" section above
3. Check that backend API is responsive
4. Verify demo user exists in database

---

**You're ready to build! 🚀**

Run: `bash /Users/mdica/PycharmProjects/EduPex/build-apk-release.sh`

