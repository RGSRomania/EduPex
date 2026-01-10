#!/bin/bash

# EduPex - Complete Build and Test Script
# This script builds the APK and provides testing instructions

set -e

echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║       📱 EduPex APK Builder with Demo Login 📱          ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# Check prerequisites
echo "🔍 Checking prerequisites..."
echo ""

# Check Node.js
if ! command -v node &> /dev/null; then
    echo "❌ Node.js not found. Please install Node.js first."
    exit 1
fi
echo "✓ Node.js: $(node --version)"

# Check npm
if ! command -v npm &> /dev/null; then
    echo "❌ npm not found. Please install npm first."
    exit 1
fi
echo "✓ npm: $(npm --version)"

# Check Java
if ! command -v java &> /dev/null; then
    echo "❌ Java not found. Please install Java 11 or later."
    exit 1
fi
echo "✓ Java: $(java -version 2>&1 | head -n 1)"

echo ""
echo "✅ All prerequisites met!"
echo ""
echo "════════════════════════════════════════════════════════════"
echo ""

# Navigate to project root
cd "$(dirname "$0")"
PROJECT_ROOT=$(pwd)

echo "📁 Project root: $PROJECT_ROOT"
echo ""

# Option to choose backend URL
echo "🌐 Backend Configuration"
echo "─────────────────────────"
echo ""
echo "Choose backend option:"
echo "  1) Local backend (http://10.0.2.2:5000/api) - for emulator testing"
echo "  2) Custom backend URL - for production/sharing"
echo ""
read -p "Enter choice (1 or 2): " BACKEND_CHOICE
echo ""

if [ "$BACKEND_CHOICE" = "2" ]; then
    read -p "Enter backend URL (e.g., https://your-backend.onrender.com/api): " CUSTOM_BACKEND_URL
    if [ -z "$CUSTOM_BACKEND_URL" ]; then
        echo "❌ Backend URL cannot be empty!"
        exit 1
    fi
    export REACT_APP_API_URL="$CUSTOM_BACKEND_URL"
    echo "✓ Backend URL set to: $CUSTOM_BACKEND_URL"
else
    export REACT_APP_API_URL="http://10.0.2.2:5000/api"
    echo "✓ Backend URL set to: http://10.0.2.2:5000/api (local)"
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo ""

# Navigate to frontend
cd "$PROJECT_ROOT/frontend"

# Step 1: Install dependencies
echo "📦 Step 1/5: Installing dependencies..."
npm install --legacy-peer-deps
echo "✓ Dependencies installed"
echo ""

# Step 2: Build React app
echo "🔨 Step 2/5: Building React application..."
npm run build
echo "✓ React app built"
echo ""

# Step 3: Sync with Capacitor
echo "🔄 Step 3/5: Syncing with Capacitor..."
npx cap sync android
echo "✓ Capacitor synced"
echo ""

# Step 4: Build APK
echo "📱 Step 4/5: Building Android APK..."
cd android

# Set JAVA_HOME
if [ -d "/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
elif [ -d "/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/opt/homebrew/opt/openjdk@17/libexec/openjdk.jdk/Contents/Home"
elif [ -d "/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home" ]; then
    export JAVA_HOME="/usr/local/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home"
fi

echo "   Using JAVA_HOME: $JAVA_HOME"

# Clean previous builds
./gradlew clean

# Build debug APK
./gradlew assembleDebug

echo "✓ APK built successfully"
echo ""

# Step 5: Locate APK
APK_PATH="$PROJECT_ROOT/frontend/android/app/build/outputs/apk/debug/app-debug.apk"

echo "📍 Step 5/5: Locating APK..."
if [ -f "$APK_PATH" ]; then
    APK_SIZE=$(ls -lh "$APK_PATH" | awk '{print $5}')
    echo "✓ APK found: $APK_SIZE"
else
    echo "❌ APK not found at expected location"
    exit 1
fi

echo ""
echo "════════════════════════════════════════════════════════════"
echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║                                                          ║"
echo "║              ✅ BUILD SUCCESSFUL! ✅                     ║"
echo "║                                                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "📱 APK Details:"
echo "───────────────"
echo "   Location: android/app/build/outputs/apk/debug/app-debug.apk"
echo "   Size: $APK_SIZE"
echo "   Package: com.edupex.app"
echo "   Backend: $REACT_APP_API_URL"
echo ""
echo "🎓 Demo Login Credentials:"
echo "───────────────────────────"
echo "   Email: test@edupex.com"
echo "   Password: test123"
echo "   OR: Click '🎓 Intră cu Cont Demo' button"
echo ""
echo "📦 Installation Options:"
echo "────────────────────────"
echo "   Option 1 - USB Install (device connected):"
echo "      adb install -r android/app/build/outputs/apk/debug/app-debug.apk"
echo ""
echo "   Option 2 - Manual Install:"
echo "      1. Copy APK to phone"
echo "      2. Open and install"
echo "      3. Allow 'Unknown Sources' if prompted"
echo ""
echo "   Option 3 - Share:"
echo "      Upload to Google Drive/Dropbox and share link"
echo ""
echo "⚠️  Important Notes:"
echo "────────────────────"
if [ "$BACKEND_CHOICE" = "1" ]; then
    echo "   • Backend set to LOCAL (10.0.2.2:5000)"
    echo "   • Make sure backend is running: cd backend && node server.js"
    echo "   • Only works on emulator or device on same network"
    echo "   • For sharing with others, rebuild with production backend URL"
else
    echo "   • Backend set to: $REACT_APP_API_URL"
    echo "   • Make sure backend is deployed and accessible"
    echo "   • Test backend URL in browser first"
fi
echo ""
echo "🧪 Testing the APK:"
echo "────────────────────"
echo "   1. Install APK on Android device/emulator"
echo "   2. Open the app"
echo "   3. Click '🎓 Intră cu Cont Demo' button"
echo "   4. Verify login works"
echo "   5. Test AI assistant"
echo "   6. Test lessons"
echo ""
echo "📚 Documentation:"
echo "──────────────────"
echo "   Full guide: BUILD_APK_GUIDE.md"
echo "   AI setup: AI_ASSISTANT_FIX.md"
echo ""
echo "✅ Ready to share! Copy the APK and send it!"
echo ""

