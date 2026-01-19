#!/bin/bash

# EduPex Status Check Script
# Use this to verify all fixes and build status

echo "════════════════════════════════════════════════════════"
echo "  EduPex APK Build - Status Check"
echo "════════════════════════════════════════════════════════"
echo ""

# Color codes
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Counter
CHECKS_PASSED=0
CHECKS_FAILED=0

# Function to check
check() {
    local name=$1
    local command=$2

    if eval "$command" > /dev/null 2>&1; then
        echo -e "${GREEN}✅${NC} $name"
        ((CHECKS_PASSED++))
    else
        echo -e "${RED}❌${NC} $name"
        ((CHECKS_FAILED++))
    fi
}

echo "--- Files & Configuration ---"
check "React build exists" "[ -d /Users/mdica/PycharmProjects/EduPex/frontend/build ]"
check "API config updated" "grep -q 'https://edupex-backend.onrender.com/api' /Users/mdica/PycharmProjects/EduPex/frontend/src/config/apiConfig.js"
check "Gradle config fixed" "grep -q 'if (signingConfigs.hasProperty' /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build.gradle"

echo ""
echo "--- Backend Accessibility ---"
check "Backend is online" "curl -s -o /dev/null -w '%{http_code}' https://edupex-backend.onrender.com/api/ | grep -q 200"

echo ""
echo "--- APK Build Status ---"
if [ -f "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk" ]; then
    APK_SIZE=$(ls -lh /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk | awk '{print $5}')
    echo -e "${GREEN}✅${NC} APK BUILD COMPLETE!"
    echo "   Location: /frontend/android/app/build/outputs/apk/debug/app-debug.apk"
    echo "   Size: $APK_SIZE"
    ((CHECKS_PASSED++))
else
    if [ -d "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build" ]; then
        echo -e "${YELLOW}⏳${NC} APK still building..."
        echo "   Directory exists - compilation in progress"
    else
        echo -e "${YELLOW}⏳${NC} APK build starting (takes 5-10 minutes)..."
    fi
fi

echo ""
echo "--- Device Setup (Optional Check) ---"
check "ADB available" "which adb"
check "Android SDK available" "which android"

echo ""
echo "════════════════════════════════════════════════════════"
echo "  Summary"
echo "════════════════════════════════════════════════════════"
echo ""

TOTAL=$((CHECKS_PASSED + CHECKS_FAILED))

if [ $CHECKS_FAILED -eq 0 ]; then
    echo -e "${GREEN}✅ All checks passed!${NC}"
else
    echo -e "${YELLOW}⚠️  Some checks incomplete (may be expected)${NC}"
fi

echo ""
echo "Checks Passed: $CHECKS_PASSED"
echo "Checks Failed: $CHECKS_FAILED"
echo ""

if [ -f "/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk" ]; then
    echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
    echo -e "${GREEN}  🎉 READY TO INSTALL AND TEST!${NC}"
    echo -e "${GREEN}════════════════════════════════════════════════════════${NC}"
    echo ""
    echo "Next command:"
    echo "  adb install /Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/debug/app-debug.apk"
    echo ""
else
    echo "════════════════════════════════════════════════════════"
    echo "  ⏳ Waiting for APK build to complete (5-10 minutes)..."
    echo "════════════════════════════════════════════════════════"
    echo ""
    echo "Run this script again to check progress:"
    echo "  $0"
    echo ""
fi

echo "For more details, see:"
echo "  - FINAL_STATUS.md (detailed info)"
echo "  - ACTION_PLAN.md (next steps)"
echo "  - ISSUES_RESOLVED.md (what was fixed)"
echo ""


