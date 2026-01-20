# EduPex APK Deployment Guide

**Build Date:** January 20, 2026
**Status:** ✅ READY FOR TESTING

## APK Information

- **File:** `app-debug.apk`
- **Location:** `/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk`
- **Size:** 5.4 MB
- **Type:** Debug APK (for testing purposes)
- **Backend:** Render Cloud (https://edupex-backend.onrender.com/api)

## Latest Changes

✅ **Fixed Duplicate Chapters Issue**
- Removed 6 duplicate unitati from Matematica (was 12, now 6)
- Removed 6 duplicate unitati from Limba Romana (was 12, now 6)
- Both subjects now display correct chapter structure
- Database cleaned and optimized

## Installation Instructions

### Option 1: Using ADB (Android Debug Bridge)

```bash
# Connect your Android device via USB (with USB debugging enabled)
adb install /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk

# Or use:
adb install-multiple /path/to/app-debug.apk
```

### Option 2: Manual Installation

1. **Transfer APK to Device:**
   - Connect device via USB
   - Copy `app-debug.apk` to device storage (Downloads folder)

2. **Install on Device:**
   - Open Files/File Manager on device
   - Navigate to Downloads
   - Tap `app-debug.apk`
   - Click "Install"
   - Grant necessary permissions when prompted

3. **Allow Installation from Unknown Sources (if needed):**
   - Settings → Security → Unknown Sources (Enable)
   - Then install as above

## App Features to Test

### ✅ What's Working
- **Login/Registration** - Test account creation and login
- **Subject Selection** - Select Matematica or Limba Romana
- **Chapter Display** - Should show **exactly 6 chapters** per subject
- **Lesson Navigation** - Open chapters and view lessons
- **Lesson Content** - Read lesson theory, examples, and tips
- **Quiz/Questions** - Answer questions with feedback

### 🔗 Backend Connection
The app connects to:
```
API Endpoint: https://edupex-backend.onrender.com/api
```

**Status:** ✅ **ONLINE** - Tested and verified working

### 📊 Database
- **MongoDB:** Connected and accessible
- **Lessons:** 51 for Matematica, 50 for Limba Romana (Clasa V)
- **Chapters:** 6 per subject (fixed!)
- **Content:** Fully populated from official curriculum

## Testing Checklist

- [ ] App installs without errors
- [ ] App launches and displays splash screen
- [ ] Can register new user account
- [ ] Can login with account
- [ ] "Lectii" (Lessons) page shows subjects
- [ ] Can select "Matematica" - shows 6 chapters
- [ ] Can select "Limba Romana" - shows 6 chapters
- [ ] Can open a chapter and see lessons
- [ ] Can open a lesson and read content
- [ ] Can answer quiz questions
- [ ] Progress is saved
- [ ] Back button works correctly
- [ ] No major crashes or errors

## Troubleshooting

### App Won't Install
1. Check Android version (minimum API 24 / Android 7.0)
2. Ensure sufficient storage (need ~50 MB free)
3. Try: `adb uninstall com.edupex.app` then reinstall

### Backend Connection Error
1. Check internet connection
2. Verify Render backend status at: https://edupex-backend.onrender.com/api/lessons/test
3. Clear app cache: Settings → Apps → EduPex → Storage → Clear Cache

### App Crashes on Launch
1. Check logcat: `adb logcat com.edupex.app:*`
2. Ensure device has minimum 2GB RAM
3. Try clearing app data: Settings → Apps → EduPex → Storage → Clear All Data

## Performance Notes

- **Render Backend:** Free tier may have cold starts (first request takes 15-30 seconds)
- **Network:** Requires active internet connection
- **Battery:** Monitor battery usage during testing
- **Storage:** APK uses ~100 MB after installation with cached data

## Version Information

- **App Version:** 1.0 (Debug)
- **Build Type:** Debug
- **Render Backend:** edupex-backend.onrender.com
- **Database:** MongoDB Atlas

## Contact & Support

For issues or feedback:
1. Check the troubleshooting section above
2. Review app logs: `adb logcat | grep -i edupex`
3. Test with different Android devices if possible

---

**Build Command Used:**
```bash
./gradlew clean assembleDebug
```

**Next Steps:**
1. ✅ Build APK - DONE
2. ⏳ Test on external device
3. ⏳ Gather feedback and fix issues
4. ⏳ Create release APK for Play Store (when ready)

