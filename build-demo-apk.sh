#!/bin/bash

echo "📱 EduPex - Build Debug APK with Demo Login"
echo "============================================"
echo ""

# Navigate to frontend directory
cd "$(dirname "$0")/frontend"

# Check if we're in the right place
if [ ! -f "package.json" ]; then
    echo "❌ Error: Cannot find frontend directory"
    exit 1
fi

# Step 1: Set up environment for local backend connection
echo "Step 1: Configuring for local/demo backend..."
export REACT_APP_API_URL="http://10.0.2.2:5000/api"  # Android emulator localhost
echo "✓ API URL set to: $REACT_APP_API_URL"
echo ""

# Step 2: Install dependencies
echo "Step 2: Installing dependencies..."
npm install
echo "✓ Dependencies installed"
echo ""

# Step 3: Build React app
echo "Step 3: Building React app..."
npm run build
echo "✓ React app built"
echo ""

# Step 4: Sync with Capacitor
echo "Step 4: Syncing with Capacitor..."
npx cap sync android
echo "✓ Capacitor synced"
echo ""

# Step 5: Build debug APK
echo "Step 5: Building debug APK..."
cd android

# Set JAVA_HOME for macOS with Homebrew OpenJDK
if [ -d "/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
elif [ -d "/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"
elif [ -d "/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
fi

echo "Using JAVA_HOME: $JAVA_HOME"

# Build debug APK (no signing required)
./gradlew assembleDebug

echo ""
echo "✅ SUCCESS! Debug APK built!"
echo "============================================"
echo ""
echo "📍 APK Location:"
echo "   android/app/build/outputs/apk/debug/app-debug.apk"
echo ""
echo "📱 To install on device:"
echo "   1. Connect your Android device via USB"
echo "   2. Enable USB debugging on device"
echo "   3. Run: adb install -r android/app/build/outputs/apk/debug/app-debug.apk"
echo ""
echo "   Or simply copy the APK to your device and install it"
echo ""
echo "🎓 Demo Login Credentials:"
echo "   Email: test@edupex.com"
echo "   Password: test123"
echo ""
echo "   OR click the '🎓 Intră cu Cont Demo' button to auto-login"
echo ""
echo "⚠️  Note: Make sure your backend server is running!"
echo "   Backend should be accessible at: http://10.0.2.2:5000"
echo "   (This is Android emulator's localhost)"
echo ""

