#!/bin/bash

# EduPex APK Build Script - For Render Backend
# This script builds a debug APK for testing on external devices
# The app will connect to the Render backend at: https://edupex-backend.onrender.com/api

echo "🚀 Starting EduPex APK Build Process"
echo "========================================"
echo ""

# Change to frontend directory
cd "$(dirname "$0")/frontend" || exit 1

echo "✅ Step 1: Cleaning dependencies and build artifacts"
echo "-------------------------------------------"
# Clean node modules and build folder
rm -rf node_modules build dist android/app/build android/app/.gradle || true

echo "✅ Step 2: Installing dependencies"
echo "-------------------------------------------"
npm install

echo "✅ Step 3: Building React web app"
echo "-------------------------------------------"
npm run build

echo "✅ Step 4: Setting up Capacitor Android"
echo "-------------------------------------------"
npx cap sync android

echo "✅ Step 5: Building APK with Gradle"
echo "-------------------------------------------"
cd android || exit 1

# Build debug APK
./gradlew clean assembleDebug

APK_PATH="app/build/outputs/apk/debug/app-debug.apk"

if [ -f "$APK_PATH" ]; then
    echo ""
    echo "✅ APK BUILD SUCCESSFUL!"
    echo "========================================"
    echo ""
    echo "📱 APK Location: $(pwd)/$APK_PATH"
    echo ""
    echo "📋 Next Steps:"
    echo "1. Transfer the APK to your external device:"
    echo "   adb install $(pwd)/$APK_PATH"
    echo ""
    echo "2. Or transfer manually via USB:"
    echo "   - Copy APK to device storage"
    echo "   - Install using file manager or adb"
    echo ""
    echo "3. The app will connect to Render backend:"
    echo "   https://edupex-backend.onrender.com/api"
    echo ""
else
    echo ""
    echo "❌ APK BUILD FAILED"
    echo "Please check the build errors above"
    exit 1
fi

