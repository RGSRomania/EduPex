#!/bin/bash

# EduPex APK Build Script (Fixed Version)
# This script builds the APK with all fixes applied

echo "=========================================="
echo "EduPex APK Build Script (Fixed)"
echo "=========================================="
echo ""

# Step 1: Build React App
echo "Step 1: Building React app..."
cd /Users/mdica/PycharmProjects/EduPex/frontend
if npm run build > /dev/null 2>&1; then
    echo "✅ React app built successfully"
else
    echo "❌ React build failed"
    exit 1
fi

# Step 2: Check if build directory exists
if [ ! -d "build" ]; then
    echo "❌ Build directory not found"
    exit 1
fi
echo "✅ Build directory confirmed"

# Step 3: Fix permissions
echo ""
echo "Step 2: Fixing permissions..."
sudo chown -R $USER /Users/mdica/PycharmProjects/EduPex/frontend/android 2>/dev/null || true

# Step 4: Build APK
echo ""
echo "Step 3: Building Android APK..."
echo "This may take 5-10 minutes..."
cd /Users/mdica/PycharmProjects/EduPex/frontend/android

# Run gradle build
./gradlew clean assembleDebug

# Check if APK was created
echo ""
if [ -f "app/build/outputs/apk/debug/app-debug.apk" ]; then
    APK_SIZE=$(ls -lh app/build/outputs/apk/debug/app-debug.apk | awk '{print $5}')
    echo "=========================================="
    echo "✅ APK BUILD SUCCESSFUL!"
    echo "=========================================="
    echo ""
    echo "APK Location:"
    echo "  /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "APK Size: $APK_SIZE"
    echo ""
    echo "Next Steps:"
    echo "  1. Install on device:"
    echo "     adb install app/build/outputs/apk/debug/app-debug.apk"
    echo ""
    echo "  2. Open app on device"
    echo "  3. Click '🎓 Intră cu Cont Demo' button"
    echo "  4. Should auto-login with test@edupex.com"
    echo ""
    echo "API URL (in APK): https://edupex-backend.onrender.com/api"
    echo "Test Credentials: test@edupex.com / test123"
    echo ""
else
    echo "❌ APK build failed - app-debug.apk not found"
    exit 1
fi


