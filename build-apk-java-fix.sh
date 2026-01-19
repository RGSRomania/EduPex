#!/bin/bash

# Build APK with Java 21 (compatible with Gradle 8.12)

cd /Users/mdica/PycharmProjects/EduPex/frontend/android

echo "Attempting to find compatible Java version..."

# Try common Java paths
JAVA_HOMES=(
    "/usr/libexec/java_home -v 21"
    "/usr/libexec/java_home -v 17"
    "/usr/libexec/java_home -v 11"
)

JAVA_HOME=""
for java_cmd in "${JAVA_HOMES[@]}"; do
    if eval "$java_cmd" &>/dev/null; then
        JAVA_HOME=$(eval "$java_cmd")
        JAVA_VERSION=$(echo $JAVA_HOME | grep -oE "[0-9]+")
        echo "Found Java $JAVA_VERSION at: $JAVA_HOME"
        break
    fi
done

if [ -z "$JAVA_HOME" ]; then
    echo "No compatible Java version found"
    echo "Trying with current Java anyway..."
    JAVA_HOME="/Library/Java/JavaVirtualMachines/openjdk-24.0.1/Contents/Home"
fi

echo ""
echo "Setting JAVA_HOME to: $JAVA_HOME"
export JAVA_HOME

# Now build
echo ""
echo "Building APK with Java $(basename $JAVA_HOME)..."
echo ""

chmod +x gradlew

./gradlew clean assembleDebug

APK_PATH="/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"

if [ -f "$APK_PATH" ]; then
    echo ""
    echo "✅ APK BUILD SUCCESSFUL!"
    echo ""
    APK_SIZE=$(ls -lh "$APK_PATH" | awk '{print $5}')
    echo "📦 Location: $APK_PATH"
    echo "📦 Size: $APK_SIZE"
    echo ""
    echo "Ready for installation!"
else
    echo ""
    echo "❌ APK build still failed"
    exit 1
fi

