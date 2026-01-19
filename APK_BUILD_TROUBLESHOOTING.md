# 🛠️ APK Build Troubleshooting

## If Build Succeeds ✅

You'll find the APK at:
```
/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

Then follow installation instructions in `APK_BUILD_FIXED.md`

---

## If Build Takes Too Long (>30 min)

The build might be stuck. Kill it and retry:

```bash
# Kill gradle
pkill -f gradle

# Clean and rebuild
cd /Users/mdica/PycharmProjects/EduPex/frontend/android
rm -rf .gradle build
./gradlew clean assembleDebug
```

---

## If Build Fails

Check the log file:
```bash
tail -100 /tmp/apk_build_final.log
```

### Common Error: "Cannot find symbol"
- **Cause**: Capacitor sync issue
- **Fix**: 
  ```bash
  cd /Users/mdica/PycharmProjects/EduPex/frontend
  npx cap sync android
  cd android
  ./gradlew clean assembleDebug
  ```

### Common Error: "Gradle version not supported"
- **Cause**: Gradle 8.13 download failed
- **Fix**:
  ```bash
  cd /Users/mdica/PycharmProjects/EduPex/frontend/android
  rm -rf ~/.gradle/wrapper
  ./gradlew clean assembleDebug
  ```

### Common Error: "Out of memory"
- **Cause**: Gradle needs more heap space
- **Fix**:
  ```bash
  export GRADLE_OPTS="-Xmx2048m"
  cd /Users/mdica/PycharmProjects/EduPex/frontend/android
  ./gradlew clean assembleDebug
  ```

---

## If APK Build Succeeds But Installation Fails

### Error: "app not installed"
1. Check Android version: Android 8.0+
2. Check storage: 50MB free
3. Try: `adb install -r` (replace flag)

### Error: "permission denied"
- Enable "Unknown Sources" in device Settings

### Error: "INSTALL_FAILED_INVALID_APK"
- APK may be corrupted
- Try rebuilding

---

## Quick Commands Reference

### Check prerequisites
```bash
java -version      # Should show Java 24
gradle --version   # Should show 8.13
node --version     # Should show v18+
npm --version      # Should show 9+
```

### Clean build
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend/android
rm -rf .gradle build app/build
./gradlew clean assembleDebug
```

### Monitor build
```bash
tail -f /tmp/apk_build_final.log
```

### When APK is ready
```bash
ls -lah /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk
```

---

## Key Files

| File | Purpose |
|------|---------|
| `gradle-wrapper.properties` | Gradle version config |
| `build.gradle` (app) | Android build settings |
| `capacitor.config.ts` | Capacitor configuration |
| `package.json` (frontend) | React dependencies |

---

## Support Info

- **Gradle 8.13 Java Support**: https://docs.gradle.org/8.13/userguide/java_compatibility.html
- **Capacitor Docs**: https://capacitorjs.com/docs/android
- **Android Build**: https://developer.android.com/build

---

If you encounter an error, check the full log:
```bash
cat /tmp/apk_build_final.log | grep -i "error\|failed\|exception"
```

Share the error message for specific help!

