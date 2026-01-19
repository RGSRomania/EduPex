#!/bin/bash

# Direct Gradle Build with explicit steps

cd /Users/mdica/PycharmProjects/EduPex/frontend/android

echo "Step 1: Making gradlew executable..."
chmod +x gradlew

echo "Step 2: Checking Gradle..."
./gradlew --version > /tmp/gradle_version.txt 2>&1
echo "Gradle check completed"

echo "Step 3: Cleaning..."
./gradlew clean > /tmp/gradle_clean.txt 2>&1
echo "Clean completed"

echo "Step 4: Building APK..."
./gradlew assembleDebug > /tmp/gradle_build.txt 2>&1

APK_PATH="/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"

echo "Step 5: Checking result..."
if [ -f "$APK_PATH" ]; then
    echo "✅ APK CREATED SUCCESSFULLY"
    ls -lh "$APK_PATH"
else
    echo "❌ APK NOT FOUND"
    echo ""
    echo "Build logs:"
    echo "--- Version ---"
    cat /tmp/gradle_version.txt
    echo ""
    echo "--- Clean ---"
    cat /tmp/gradle_clean.txt
    echo ""
    echo "--- Build ---"
    tail -50 /tmp/gradle_build.txt
fi

