#!/bin/bash

echo "================================"
echo "  APK Build Status Check"
echo "================================"
echo ""

APK_PATH="/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"

# Check if APK exists
if [ -f "$APK_PATH" ]; then
    APK_SIZE=$(du -h "$APK_PATH" | cut -f1)
    MOD_TIME=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M:%S" "$APK_PATH")

    echo "✅ APK BUILD COMPLETE!"
    echo ""
    echo "📦 File Details:"
    echo "   Location: $APK_PATH"
    echo "   Size: $APK_SIZE"
    echo "   Last Modified: $MOD_TIME"
    echo ""
    echo "📱 Ready to Install:"
    echo ""
    echo "   Option 1: USB Installation"
    echo "   adb install -r \"$APK_PATH\""
    echo ""
    echo "   Option 2: Manual Transfer"
    echo "   cp \"$APK_PATH\" ~/Desktop/edupex.apk"
    echo "   (Then transfer file to device)"
    echo ""
    echo "🔑 Demo Login Credentials:"
    echo "   Email: test@edupex.com"
    echo "   Password: test123"
    echo ""
    echo "🌐 Backend API:"
    echo "   https://edupex-backend.onrender.com/api"
    echo ""
    echo "================================"
else
    echo "⏳ Build Still in Progress..."
    echo ""
    echo "Checking intermediate build stages..."
    echo ""

    # Check React build
    if [ -d "/Users/mdica/PycharmProjects/EduPex/frontend/build" ]; then
        echo "✓ React build directory created"
    else
        echo "⏳ React build in progress (or not started)"
    fi

    # Check Gradle cache
    if [ -d "/Users/mdica/PycharmProjects/EduPex/frontend/android/.gradle" ]; then
        echo "✓ Gradle is running"
    else
        echo "⏳ Gradle preparing..."
    fi

    # Check intermediate APK build
    if [ -d "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build" ]; then
        echo "✓ APK build directory exists"
    else
        echo "⏳ APK build hasn't started yet"
    fi

    echo ""
    echo "Please wait... Build typically takes 5-10 minutes"
    echo "Run this script again in a moment to check status"
    echo ""
    echo "Or check logs:"
    echo "   tail -f /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build.log 2>/dev/null || echo 'No build log yet'"
fi

