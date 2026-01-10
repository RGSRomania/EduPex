#!/bin/bash

echo "🚀 EduPex Deployment Script"
echo "============================"

# Get backend URL from user
read -p "Enter your deployed backend URL (e.g., https://edupex-backend.onrender.com): " BACKEND_URL

if [ -z "$BACKEND_URL" ]; then
    echo "❌ Backend URL is required!"
    exit 1
fi

echo "📦 Building React app with production backend..."
cd /Users/mdica/PycharmProjects/EduPex/frontend

# Build with production URL
REACT_APP_API_URL=$BACKEND_URL/api npm run build

echo "🔄 Syncing with Android..."
npx cap sync android

echo "📱 Building production APK..."
cd android
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
./gradlew assembleRelease

echo ""
echo "✅ Production APK built successfully!"
echo "📍 Location: android/app/build/outputs/apk/release/app-release.apk"
echo ""
echo "📋 Next steps:"
echo "1. Install APK on your Android device"
echo "2. The app will connect to: $BACKEND_URL"
echo ""

