#!/bin/bash

# Quick Pre-Build Checklist
echo "╔══════════════════════════════════════════════════════════╗"
echo "║     📋 APK BUILD PRE-FLIGHT CHECKLIST 📋                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

cd "$(dirname "$0")"

echo "Checking requirements..."
echo ""

# Check 1: Node.js
if command -v node &> /dev/null; then
    echo "✅ Node.js installed: $(node --version)"
else
    echo "❌ Node.js NOT installed"
    echo "   Install: brew install node"
fi

# Check 2: npm
if command -v npm &> /dev/null; then
    echo "✅ npm installed: $(npm --version)"
else
    echo "❌ npm NOT installed"
fi

# Check 3: Java
if command -v java &> /dev/null; then
    JAVA_VERSION=$(java -version 2>&1 | head -n 1)
    echo "✅ Java installed: $JAVA_VERSION"
else
    echo "❌ Java NOT installed"
    echo "   Install: brew install openjdk@21"
fi

# Check 4: Build scripts exist
if [ -f "build-apk.sh" ]; then
    echo "✅ build-apk.sh exists"
else
    echo "❌ build-apk.sh NOT found"
fi

if [ -f "build-demo-apk.sh" ]; then
    echo "✅ build-demo-apk.sh exists"
else
    echo "❌ build-demo-apk.sh NOT found"
fi

# Check 5: Frontend directory
if [ -d "frontend" ]; then
    echo "✅ frontend directory exists"
else
    echo "❌ frontend directory NOT found"
fi

# Check 6: Android directory
if [ -d "frontend/android" ]; then
    echo "✅ Android project exists"
else
    echo "❌ Android project NOT found"
    echo "   Run: cd frontend && npx cap add android"
fi

# Check 7: Login.js has demo button
if grep -q "handleDemoLogin" frontend/src/pages/Login.js 2>/dev/null; then
    echo "✅ Demo login button implemented"
else
    echo "❌ Demo login button NOT found in Login.js"
fi

# Check 8: Test user in database
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Next Steps:"
echo ""
echo "   To build APK, run:"
echo "      ./build-apk.sh"
echo ""
echo "   Or quick build:"
echo "      ./build-demo-apk.sh"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

