#!/bin/bash

# EduPex APK Build Script
# Builds a production APK for external device deployment

set -e

echo "================================================"
echo "  EduPex APK Build Script"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

PROJECT_DIR="/Users/mdica/PycharmProjects/EduPex"
FRONTEND_DIR="$PROJECT_DIR/frontend"
ANDROID_DIR="$FRONTEND_DIR/android"

# Check for required tools
echo -e "${BLUE}Checking prerequisites...${NC}"

if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js not found. Please install Node.js${NC}"
    exit 1
fi

if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm not found. Please install npm${NC}"
    exit 1
fi

if ! command -v java &> /dev/null; then
    echo -e "${RED}❌ Java not found. Please install Java JDK${NC}"
    exit 1
fi

echo -e "${GREEN}✓ All prerequisites found${NC}"
echo ""

# Step 1: Build React app for production
echo -e "${BLUE}Step 1: Building React app for production...${NC}"
cd "$FRONTEND_DIR"

# Install dependencies if needed
if [ ! -d "node_modules" ]; then
  echo "Installing dependencies..."
  npm install
fi

# Build for production
echo "Building production bundle..."
npm run build

echo -e "${GREEN}✓ React app built successfully${NC}"
echo ""

# Step 2: Copy web assets to Capacitor
echo -e "${BLUE}Step 2: Copying web assets to Capacitor...${NC}"
cd "$FRONTEND_DIR"
npx cap sync android

echo -e "${GREEN}✓ Web assets synced${NC}"
echo ""

# Step 3: Build APK
echo -e "${BLUE}Step 3: Building APK...${NC}"
cd "$ANDROID_DIR"

# Make gradlew executable
chmod +x gradlew

# Build using Gradle - assembleDebug for testing (unsigned)
# For production, use assembleRelease (requires signing)
echo "Running Gradle build (debug APK for testing)..."
./gradlew clean assembleDebug

echo -e "${GREEN}✓ APK built successfully${NC}"
echo ""

# Step 4: Show APK location
echo -e "${BLUE}Step 4: APK Details${NC}"
APK_PATH="$ANDROID_DIR/app/build/outputs/apk/debug/app-debug.apk"

if [ -f "$APK_PATH" ]; then
  APK_SIZE=$(du -h "$APK_PATH" | cut -f1)
  echo -e "${GREEN}✓ APK Generated Successfully!${NC}"
  echo ""
  echo "📦 APK Details:"
  echo "   Location: $APK_PATH"
  echo "   Size: $APK_SIZE"
  echo "   Type: Debug APK (for testing on external devices)"
  echo ""
  echo "📱 Demo Login Credentials:"
  echo "   Email: test@edupex.com"
  echo "   Password: test123"
  echo ""
  echo "🌐 API Endpoint:"
  echo "   https://edupex-backend.onrender.com/api"
  echo ""
  echo "✅ Ready to install on external device!"
  echo ""
  echo "To install on device (with adb):"
  echo "   adb install -r \"$APK_PATH\""
  echo ""
  echo "To transfer APK to device:"
  echo "   cp \"$APK_PATH\" ~/Desktop/edupex.apk"
  echo "   (Then transfer via email, USB, or file sharing)"
else
  echo -e "${RED}❌ APK not found at expected location${NC}"
  echo "   Expected: $APK_PATH"
  echo "   Please check build logs above for errors"
  exit 1
fi

echo -e "${BLUE}================================================${NC}"
echo -e "${GREEN}Build Complete! APK is ready for distribution.${NC}"
echo -e "${BLUE}================================================${NC}"


