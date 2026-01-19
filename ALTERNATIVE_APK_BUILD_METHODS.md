# 🛠️ Alternative: Manual APK Build Instructions

Since Gradle builds are having Java compatibility issues, here's an alternative approach:

## Option 1: Build APK Using Android Studio (Recommended)

1. Open Android Studio
2. File → Open → `/Users/mdica/PycharmProjects/EduPex/frontend/android`
3. Click "Build" → "Build Bundle(s) / APK(s)" → "Build APK(s)"
4. Wait for build to complete
5. APK will be in: `frontend/android/app/build/outputs/apk/debug/`

## Option 2: Use EAS Build (Expo)

1. Install EAS CLI: `npm install -g eas-cli`
2. Go to frontend: `cd /Users/mdica/PycharmProjects/EduPex/frontend`
3. Login to Expo: `eas login`
4. Build APK: `eas build --platform android`
5. Download APK when ready

## Option 3: Troubleshoot Gradle

If you want to try Gradle again:

```bash
# Check Java version
java -version

# If Java 24, downgrade to Java 21:
# 1. Install Java 21: brew install openjdk@21
# 2. Set JAVA_HOME: export JAVA_HOME=$(/usr/libexec/java_home -v 21)
# 3. Verify: java -version
# 4. Build: cd /Users/mdica/PycharmProjects/EduPex/frontend/android && ./gradlew assembleDebug
```

## Option 4: Check Build Status

```bash
# Check if build is running
ps aux | grep gradle

# Kill stuck build
pkill -9 gradle

# Check build output directory
ls -la /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/
```

## When APK is Ready

```bash
# Copy to desktop
cp "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk" ~/Desktop/edupex.apk

# Or install directly
adb install -r "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
```

## Demo Login
```
Email: test@edupex.com
Password: test123
```

---

**Recommended**: Use Android Studio for the most reliable build process.

