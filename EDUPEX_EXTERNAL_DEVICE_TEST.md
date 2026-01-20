# 🚀 EduPex External Device Testing Guide

**Build Date:** January 20, 2026  
**Status:** ✅ **READY FOR TESTING**  
**Backend:** Render Cloud (https://edupex-backend.onrender.com/api)

---

## 📋 Quick Summary

You now have everything needed to test the EduPex app on an external Android device:

| Item | Status | Details |
|------|--------|---------|
| **Database Fix** | ✅ DONE | Removed 12 duplicate chapters → Now 6 per subject |
| **APK Build** | ✅ DONE | 5.4 MB debug APK ready |
| **Backend** | ✅ ONLINE | Render server verified and working |
| **Documentation** | ✅ COMPLETE | Full guides and checklists included |
| **Scripts** | ✅ READY | Installation and build scripts provided |

---

## 🎯 What Was Fixed

### Before ❌
- **Matematica:** 12 chapters shown (duplicates with mixed naming)
- **Limba Romana:** 12 chapters shown (duplicates with mixed naming)

### After ✅
- **Matematica:** 6 chapters displayed correctly
- **Limba Romana:** 6 chapters displayed correctly
- All duplicate unitati removed from MongoDB
- Database optimized and cleaned

---

## 📱 Installation Steps (Choose One)

### Option A: Using the Automated Script (Recommended)

```bash
# Make the script executable
chmod +x /Users/mdica/PycharmProjects/EduPex/adb-install.sh

# Run the installation script
/Users/mdica/PycharmProjects/EduPex/adb-install.sh
```

The script will:
- Check for ADB installation
- List connected devices
- Guide you through enabling USB debugging
- Install the APK automatically
- Provide useful ADB commands for testing

### Option B: Manual ADB Installation

```bash
# 1. Enable USB Debugging on device
Settings → About Phone → Build Number (tap 7 times)
Settings → Developer Options → USB Debugging → ON

# 2. Connect device via USB

# 3. Check device connection
adb devices

# 4. Install APK
adb install /Users/mdica/PycharmProjects/EduPex/EduPex-debug.apk
```

### Option C: Manual File Transfer

1. Connect device via USB
2. Copy `EduPex-debug.apk` to device (via Android File Transfer or USB)
3. Open Files/File Manager on device
4. Navigate to file location
5. Tap APK → Install
6. Grant permissions when prompted

---

## ✅ Testing Checklist

### Installation
- [ ] APK installs without errors
- [ ] Installation completes in < 30 seconds
- [ ] App icon appears on home screen

### Launch & UI
- [ ] App launches without crashing
- [ ] Splash screen displays
- [ ] UI is responsive (no freezing)
- [ ] Text is readable and properly formatted

### Authentication
- [ ] Can create new account
- [ ] Can login with email/password
- [ ] Can logout successfully
- [ ] Remember me feature works (if available)

### Main Feature: Chapter Selection
- [ ] "Lectii" (Lessons) page loads
- [ ] Can see subject options
- [ ] **Can select "Matematica" → Shows 6 chapters** ✅
- [ ] **Can select "Limba Romana" → Shows 6 chapters** ✅

### Chapter Details
- [ ] Can open a chapter
- [ ] Chapter displays correct lessons
- [ ] Lessons list is scrollable
- [ ] Can click on a lesson

### Lesson Content
- [ ] Lesson theory displays with proper formatting
- [ ] Examples are visible and readable
- [ ] Tips section shows helpful advice
- [ ] Content is complete (not cut off)

### Quiz/Questions
- [ ] Can answer multiple choice questions
- [ ] Correct answers are indicated
- [ ] Explanations display for each answer
- [ ] Can proceed to next question
- [ ] Quiz progress is tracked

### Navigation
- [ ] Back button returns to previous screen
- [ ] Home button takes to main menu
- [ ] Menu navigation works smoothly
- [ ] No navigation crashes or freezes

### Performance
- [ ] App loads lessons in < 3 seconds
- [ ] Quiz answers respond within 1 second
- [ ] No excessive battery drain during testing
- [ ] No memory/RAM issues

### Data Persistence
- [ ] Progress is saved
- [ ] User can logout and login again
- [ ] Previous progress is still there
- [ ] Quiz answers are remembered

### Error Handling
- [ ] No unexpected crashes
- [ ] Error messages are clear
- [ ] App recovers gracefully from errors
- [ ] Network errors are handled properly

---

## 🔧 Useful Testing Commands

### View App Logs (Troubleshooting)
```bash
# Real-time app logs
adb logcat com.edupex.app:*

# Filter for errors
adb logcat com.edupex.app:E

# Save logs to file
adb logcat com.edupex.app:* > edupex-logs.txt
```

### Clear App Data
```bash
# Clear cache only (keeps login)
adb shell pm clear --cache-only com.edupex.app

# Clear all app data (remove login)
adb shell pm clear com.edupex.app
```

### Screenshots & Video Recording
```bash
# Take screenshot
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png ~/Desktop/

# Record video (30 seconds)
adb shell screenrecord --time-limit=30 /sdcard/video.mp4
adb pull /sdcard/video.mp4 ~/Desktop/
```

### Device Information
```bash
# Device specs
adb shell getprop | grep -i "model\|version\|product"

# Check available storage
adb shell df -h | grep -E "^/data|^/storage"

# Check RAM usage
adb shell "cat /proc/meminfo | grep -i memtotal"
```

### App Management
```bash
# Uninstall app
adb uninstall com.edupex.app

# Get app info
adb shell dumpsys package com.edupex.app

# Force stop app
adb shell am force-stop com.edupex.app
```

---

## 🌐 Backend API Status

### Endpoint Health Check
```bash
# Test backend is running
curl https://edupex-backend.onrender.com/api/lessons/test

# Expected response:
# {"message":"Lesson routes are accessible!","timestamp":"2026-01-20T..."}
```

### Database Status
```bash
# Get available subjects
curl https://edupex-backend.onrender.com/api/lessons/materii

# Get lessons for Matematica
curl https://edupex-backend.onrender.com/api/lessons/materii/<materieId>/clase
```

---

## 🐛 Common Issues & Solutions

### Issue: "Installation unsuccessful"
```
❌ Error message when running: adb install app-debug.apk

Solutions:
1. Uninstall previous version:
   adb uninstall com.edupex.app
2. Clear cache:
   adb cache --clear
3. Check storage:
   Device must have at least 50 MB free
4. Try again:
   adb install /Users/mdica/PycharmProjects/EduPex/EduPex-debug.apk
```

### Issue: "No devices found" with adb
```
❌ adb devices returns empty list

Solutions:
1. Enable USB Debugging on device
2. Accept authorization dialog on device
3. Restart adb server:
   adb kill-server
   adb start-server
4. Try different USB cable
5. Update Android SDK Tools
```

### Issue: "Backend connection error"
```
❌ App shows connection timeout or "Cannot reach server"

Solutions:
1. Check internet connection on device
2. Verify Render backend is online:
   https://edupex-backend.onrender.com/api/lessons/test
3. Clear app cache:
   adb shell pm clear com.edupex.app
4. Check device DNS:
   adb shell getprop net.dns1
5. Restart app and device
```

### Issue: "App crashes immediately"
```
❌ App closes/crashes right after opening

Solutions:
1. Check device minimum requirements:
   - Android 7.0 or higher
   - 2GB RAM minimum
   - 50MB free storage
2. View crash logs:
   adb logcat com.edupex.app:E
3. Clear all app data:
   adb shell pm clear com.edupex.app
4. Reinstall APK:
   adb uninstall com.edupex.app
   adb install /path/to/EduPex-debug.apk
5. Test on different device (if available)
```

### Issue: "Wrong number of chapters"
```
❌ Still seeing 12 chapters instead of 6

This shouldn't happen as database has been fixed!

Solutions:
1. Clear app cache:
   adb shell pm clear com.edupex.app
2. Restart app
3. Force refresh data (kill and restart app)
4. Check backend:
   https://edupex-backend.onrender.com/api/lessons/materii
5. If still broken, backend may not have updated
   Contact support with device logs (adb logcat)
```

---

## 📊 Testing Report Template

When you've tested the app, please document:

```
EDUPEX TEST REPORT
==================
Date Tested: _______________
Tester Name: _______________
Device: _______________
Android Version: _______________
Network Type: WiFi / Mobile Data

PASS/FAIL SUMMARY:
✅ Installation: PASS / FAIL
✅ Login: PASS / FAIL
✅ Subject Selection: PASS / FAIL
✅ Chapter Display (6 chapters): PASS / FAIL
✅ Lesson Navigation: PASS / FAIL
✅ Content Display: PASS / FAIL
✅ Quiz/Questions: PASS / FAIL
✅ Progress Saving: PASS / FAIL
✅ Performance: PASS / FAIL
✅ Error Handling: PASS / FAIL

OVERALL: PASS / FAIL

Issues Found:
1. _______________
2. _______________
3. _______________

Suggestions for Improvement:
1. _______________
2. _______________

Notes:
_______________
```

---

## 📁 File Locations

```
Project Root: /Users/mdica/PycharmProjects/EduPex

Key Files:
├── EduPex-debug.apk (5.4 MB)         ← Install this on your device
├── adb-install.sh                     ← Run this for automatic installation
├── build-apk-render.sh                ← Use to rebuild APK if needed
├── APK_DEPLOYMENT_GUIDE_RENDER.md     ← Detailed deployment guide
├── APK_BUILD_COMPLETE_SUMMARY.md      ← Complete build summary
└── EDUPEX_EXTERNAL_DEVICE_TEST.md     ← This file

Backend:
└── Render: https://edupex-backend.onrender.com/api
```

---

## 🔐 Security & Privacy Notes

- **Debug APK:** This is a development build, not optimized for security
- **Network:** Uses HTTPS for all API calls
- **Database:** MongoDB Atlas with proper authentication
- **Test Data:** Use a test account for testing
- **Privacy:** App requires internet for full functionality

---

## ⚡ Performance Expectations

### First Load (Cold Start)
- Expected: 15-30 seconds (Render free tier cold start)
- Subsequent loads: < 3 seconds

### Quiz Response
- Expected: < 1 second for each answer

### Data Sync
- Expected: Automatic, happens in background
- No manual refresh needed

### Battery Usage
- Expected: Normal (similar to other educational apps)
- Monitor during 1-2 hour test sessions

---

## 🎓 Content Notes

### Matematica (Mathematics)
- **Grade:** Clasa V (Grade 5, ages 10-11)
- **Chapters:** 6 units covering:
  1. Natural number operations
  2. Arithmetic problem-solving methods
  3. Number divisibility
  4. Common fractions
  5. Decimal fractions
  6. Geometry and measurements

### Limba Romana (Romanian Language)
- **Grade:** Clasa V (Grade 5, ages 10-11)
- **Chapters:** 6 units covering:
  1. Communication and language
  2. Spelling and punctuation
  3. Morphology
  4. Syntax
  5. Text and discourse
  6. Literature

---

## 📞 Support

If you encounter issues:

1. **Check the troubleshooting section** above
2. **Review logs:** `adb logcat com.edupex.app:E`
3. **Verify backend:** https://edupex-backend.onrender.com/api/lessons/test
4. **Try a different device** (if available)
5. **Document your issue** with steps to reproduce

---

## ✅ Final Checklist Before Testing

- [ ] Android device with USB debugging enabled
- [ ] USB cable connected to Mac
- [ ] APK file downloaded: `EduPex-debug.apk`
- [ ] Internet connection on device (WiFi or mobile)
- [ ] Minimum Android 7.0 on device
- [ ] At least 50 MB free storage
- [ ] Read installation instructions above
- [ ] Have testing checklist ready
- [ ] Ready to document findings

---

## 🎉 Ready to Test!

Everything is prepared and documented. 

**Next step:** Follow the installation instructions above to get the app on your external device.

**Remember:** The main fix you're testing is that both Matematica and Limba Romana now show **exactly 6 chapters** instead of 12. Please verify this works correctly on your device!

---

**Questions?** Refer to the detailed guides:
- `APK_DEPLOYMENT_GUIDE_RENDER.md` - Installation details
- `APK_BUILD_COMPLETE_SUMMARY.md` - Build process details

**Good luck testing! 🚀**

