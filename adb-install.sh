#!/bin/bash
# Quick Reference: ADB Commands for EduPex Testing
# Save as: adb-install-guide.sh

echo "═══════════════════════════════════════════════════════════"
echo "  EduPex APK Installation Guide - ADB Quick Reference"
echo "═══════════════════════════════════════════════════════════"
echo ""

# Check if ADB is installed
if ! command -v adb &> /dev/null; then
    echo "❌ ADB not found. Install Android SDK Platform Tools:"
    echo "   https://developer.android.com/studio/command-line/adb"
    exit 1
fi

echo "✅ ADB is installed: $(adb --version | head -1)"
echo ""

# Get APK path
APK_PATH="/Users/mdica/PycharmProjects/EduPex/EduPex-debug.apk"

if [ ! -f "$APK_PATH" ]; then
    echo "❌ APK file not found at: $APK_PATH"
    exit 1
fi

APK_SIZE=$(du -h "$APK_PATH" | cut -f1)
echo "📱 APK Details:"
echo "   File: $(basename $APK_PATH)"
echo "   Size: $APK_SIZE"
echo "   Path: $APK_PATH"
echo ""

echo "═══════════════════════════════════════════════════════════"
echo "  Step 1: Enable USB Debugging on Your Device"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "1. Open Settings on your Android device"
echo "2. Go to: About Phone"
echo "3. Tap 'Build Number' 7 times (until you see 'Developer Mode Enabled')"
echo "4. Go back to Settings → Developer Options"
echo "5. Enable 'USB Debugging'"
echo "6. Connect device to Mac via USB cable"
echo ""

echo "═══════════════════════════════════════════════════════════"
echo "  Step 2: Check Device Connection"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Running: adb devices"
echo ""
adb devices
echo ""
echo "💡 You should see your device listed. If it shows 'unauthorized',"
echo "   check the dialog on your device and tap 'Allow USB debugging'"
echo ""

echo "═══════════════════════════════════════════════════════════"
echo "  Step 3: Install APK"
echo "═══════════════════════════════════════════════════════════"
echo ""
read -p "Press Enter to install the APK on your device..."
echo ""
echo "Installing: $APK_PATH"
echo ""

if adb install "$APK_PATH"; then
    echo ""
    echo "✅ APK INSTALLED SUCCESSFULLY!"
    echo ""
    echo "The EduPex app has been installed on your device."
    echo "You should see the app icon on your home screen."
    echo ""
    echo "═══════════════════════════════════════════════════════════"
    echo "  Next Steps"
    echo "═══════════════════════════════════════════════════════════"
    echo ""
    echo "1. Tap the EduPex icon to launch the app"
    echo "2. Create an account or login"
    echo "3. Select subject: Matematica or Limba Romana"
    echo "4. Verify you see EXACTLY 6 chapters ✅"
    echo "5. Test lesson navigation and quiz features"
    echo ""
    echo "═══════════════════════════════════════════════════════════"
    echo "  Useful ADB Commands for Testing"
    echo "═══════════════════════════════════════════════════════════"
    echo ""
    echo "View logs:"
    echo "  adb logcat com.edupex.app:* | grep -v 'Choreographer'"
    echo ""
    echo "Clear app cache:"
    echo "  adb shell pm clear com.edupex.app"
    echo ""
    echo "Uninstall app:"
    echo "  adb uninstall com.edupex.app"
    echo ""
    echo "Reinstall (uninstall + install):"
    echo "  adb uninstall com.edupex.app && adb install $APK_PATH"
    echo ""
    echo "Take device screenshot:"
    echo "  adb shell screencap -p /sdcard/screenshot.png"
    echo "  adb pull /sdcard/screenshot.png ~/screenshot.png"
    echo ""
    echo "═══════════════════════════════════════════════════════════"
else
    echo ""
    echo "❌ Installation failed. Check the error message above."
    echo ""
    echo "Possible solutions:"
    echo "1. Check USB connection"
    echo "2. Enable USB Debugging on device"
    echo "3. Uninstall previous version: adb uninstall com.edupex.app"
    echo "4. Check available storage on device (need ~50MB)"
    echo ""
    exit 1
fi

