#!/bin/bash

# Fix Java 24 issue by using Java 21

echo "Checking available Java versions..."

# Find Java 21
JAVA_21=$(/usr/libexec/java_home -v 21 2>/dev/null)

if [ -z "$JAVA_21" ]; then
    echo "❌ Java 21 not found. Installing..."
    brew install openjdk@21
    JAVA_21=$(/usr/libexec/java_home -v 21)
fi

echo "✅ Found Java 21 at: $JAVA_21"
echo ""

# Set environment
export JAVA_HOME="$JAVA_21"

echo "Testing Java version:"
java -version

echo ""
echo "Building APK with Java 21..."
echo ""

cd /Users/mdica/PycharmProjects/EduPex/frontend/android

# Clean and build
rm -rf .gradle build
chmod +x gradlew

./gradlew clean assembleDebug

# Check result
if [ -f "app/build/outputs/apk/debug/app-debug.apk" ]; then
    echo ""
    echo "✅ APK BUILD SUCCESSFUL!"
    echo ""
    APK_PATH="app/build/outputs/apk/debug/app-debug.apk"
    APK_SIZE=$(ls -lh "$APK_PATH" | awk '{print $5}')
    echo "📦 APK Created: $APK_PATH"
    echo "📦 Size: $APK_SIZE"
    echo ""
    echo "Ready to install!"
else
    echo "❌ APK build failed"
    exit 1
fi

