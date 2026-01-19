#!/bin/bash

# Check APK build status and wait for completion

APK_PATH="/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
MAX_WAIT=600  # 10 minutes in seconds
ELAPSED=0
CHECK_INTERVAL=10

echo "🔍 Checking APK build status..."
echo ""

while [ $ELAPSED -lt $MAX_WAIT ]; do
    if [ -f "$APK_PATH" ]; then
        echo "✅ APK BUILD COMPLETE!"
        echo ""
        APK_SIZE=$(ls -lh "$APK_PATH" | awk '{print $5}')
        echo "📦 APK Details:"
        echo "   Location: $APK_PATH"
        echo "   Size: $APK_SIZE"
        echo ""
        echo "📱 Demo Login Credentials:"
        echo "   Email: test@edupex.com"
        echo "   Password: test123"
        echo ""
        echo "🚀 Installation Options:"
        echo ""
        echo "   Option 1 (USB with adb):"
        echo "   adb install -r \"$APK_PATH\""
        echo ""
        echo "   Option 2 (Copy to Desktop):"
        echo "   cp \"$APK_PATH\" ~/Desktop/edupex.apk"
        echo ""
        echo "   Option 3 (Email/Cloud):"
        echo "   Send $APK_PATH to another device"
        echo ""
        exit 0
    fi

    # Show progress
    PERCENT=$((ELAPSED * 100 / MAX_WAIT))
    echo -ne "⏳ Building... ${PERCENT}% (${ELAPSED}s / ${MAX_WAIT}s)\r"

    sleep $CHECK_INTERVAL
    ELAPSED=$((ELAPSED + CHECK_INTERVAL))
done

echo ""
echo "⏰ Build timeout after 10 minutes"
echo ""
echo "❌ APK not found at: $APK_PATH"
echo ""
echo "Possible issues:"
echo "  1. Build is still running (Gradle can be slow)"
echo "  2. Build failed - check for errors"
echo "  3. Gradle compilation had issues"
echo ""
echo "Try running the build script again:"
echo "  bash /Users/mdica/PycharmProjects/EduPex/simple-build-apk.sh"
echo ""

exit 1

