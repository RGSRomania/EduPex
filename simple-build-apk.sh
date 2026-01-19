#!/bin/bash

# Simple APK Build Script - Direct approach

set -e

echo "🔨 Starting APK Build..."
echo ""

cd /Users/mdica/PycharmProjects/EduPex/frontend

# Step 1: Build React
echo "Step 1: Building React..."
npm run build --production

if [ ! -d "build" ]; then
    echo "❌ React build failed"
    exit 1
fi

echo "✅ React build complete"
echo ""

# Step 2: Sync to Capacitor
echo "Step 2: Syncing to Capacitor..."
cd /Users/mdica/PycharmProjects/EduPex/frontend
npx cap sync android

echo "✅ Capacitor sync complete"
echo ""

# Step 3: Build APK with Gradle
echo "Step 3: Building APK with Gradle..."
cd /Users/mdica/PycharmProjects/EduPex/frontend/android

# Make gradle executable
chmod +x gradlew

# Clean and build
echo "Cleaning old builds..."
./gradlew clean --quiet

echo "Building APK (this may take a few minutes)..."
./gradlew assembleDebug --quiet

echo "✅ Gradle build complete"
echo ""

# Step 4: Verify APK
echo "Step 4: Verifying APK..."
APK_PATH="/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"

if [ -f "$APK_PATH" ]; then
    APK_SIZE=$(ls -lh "$APK_PATH" | awk '{print $5}')
    echo "✅ APK BUILD SUCCESSFUL!"
    echo ""
    echo "📦 APK Details:"
    echo "   Path: $APK_PATH"
    echo "   Size: $APK_SIZE"
    echo ""
    echo "📱 To install on device:"
    echo "   adb install -r \"$APK_PATH\""
    echo ""
    echo "📊 To copy to Desktop:"
    echo "   cp \"$APK_PATH\" ~/Desktop/edupex.apk"
    echo ""
    echo "🔑 Demo Login:"
    echo "   Email: test@edupex.com"
    echo "   Password: test123"
    echo ""
else
    echo "❌ APK not found at expected location"
    echo "   Expected: $APK_PATH"
    echo ""
    echo "Checking build directory..."
    ls -la /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/ 2>/dev/null || echo "Build outputs directory doesn't exist"
    exit 1
fi

