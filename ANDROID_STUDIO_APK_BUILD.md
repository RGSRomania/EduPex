# Android Studio - Build APK Steps

## Current Screen Analysis
You can see the Build menu is open with several options:
- Assemble 'app' Run Configuration
- Compile 'android.app'
- Compile All Sources
- Assemble Module 'android.app'
- Assemble Project
- Assemble Project with Tests
- **Generate App Bundles or APKs** ← CLICK THIS ONE (has arrow →)
- Analyze APK...
- Clean Project
- Clean and Assemble Project with Tests
- Select Build Variant...

## What To Do Now:

### CLICK: Build → Generate App Bundles or APKs →

This will open a submenu with:
- Build APK(s) ← Select this
- Build App Bundle(s)

### Then Select: Build APK(s)

A dialog will appear asking:
- "Build APK(s)"
- Shows different build variants (debug, release)
- Select "debug"
- Click "Create"

### Build Process Starts
- Progress bar appears at bottom
- Takes 3-5 minutes
- Shows "Build Finished Successfully"

### APK Location
When done, APK is at:
```
/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

### Install on Device
```bash
adb install -r "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
```

### Demo Login
```
Email: test@edupex.com
Password: test123
```

---

**Next Step: Click on "Generate App Bundles or APKs" →**

