#!/bin/bash

# ============================================================================
# Quick Local Testing Script - Evaluation Form
# ============================================================================
# Usage: bash quick-local-test.sh
# This script will help you quickly set up and test locally

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     Quick Local Testing - Evaluation Form                     ║"
echo "╚════════════════════════════════════════════════════════════════╝"

# Colors for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Step 1: Check Prerequisites
echo -e "\n${BLUE}Step 1: Checking Prerequisites${NC}"
echo "================================"

if ! command -v node &> /dev/null; then
    echo -e "${RED}❌ Node.js not found${NC}"
    echo "Please install Node.js from https://nodejs.org"
    exit 1
fi
echo -e "${GREEN}✅ Node.js: $(node --version)${NC}"

if ! command -v npm &> /dev/null; then
    echo -e "${RED}❌ npm not found${NC}"
    exit 1
fi
echo -e "${GREEN}✅ npm: $(npm --version)${NC}"

# Step 2: Setup Backend
echo -e "\n${BLUE}Step 2: Setting Up Backend${NC}"
echo "================================"
cd backend || exit

echo "Installing backend dependencies..."
npm install > /dev/null 2>&1
echo -e "${GREEN}✅ Backend dependencies installed${NC}"

# Create .env if it doesn't exist
if [ ! -f .env ]; then
    echo "Creating .env file..."
    cat > .env << 'EOF'
MONGODB_URI=mongodb://localhost:27017/edupex
JWT_SECRET=test_secret_key_change_in_production
PORT=5000
NODE_ENV=development
EOF
    echo -e "${GREEN}✅ .env file created${NC}"
else
    echo -e "${GREEN}✅ .env file already exists${NC}"
fi

# Step 3: Setup Frontend
echo -e "\n${BLUE}Step 3: Setting Up Frontend${NC}"
echo "================================"
cd ../frontend || exit

echo "Installing frontend dependencies..."
npm install > /dev/null 2>&1
echo -e "${GREEN}✅ Frontend dependencies installed${NC}"

# Create .env.local if it doesn't exist
if [ ! -f .env.local ]; then
    echo "Creating .env.local file..."
    cat > .env.local << 'EOF'
REACT_APP_API_BASE_URL=http://localhost:5000/api
REACT_APP_ENVIRONMENT=development
EOF
    echo -e "${GREEN}✅ .env.local file created${NC}"
else
    echo -e "${GREEN}✅ .env.local file already exists${NC}"
fi

# Step 4: Display Instructions
cd ..
echo -e "\n${GREEN}✅ Setup Complete!${NC}"
echo ""
echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              Next Steps - Open 2 Terminal Windows              ║"
echo "╚════════════════════════════════════════════════════════════════╝"

echo -e "\n${BLUE}Terminal 1 - Start Backend:${NC}"
echo "  cd backend"
echo "  npm start"
echo ""
echo -e "${BLUE}Terminal 2 - Start Frontend:${NC}"
echo "  cd frontend"
echo "  npm start"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                      Quick Test Steps                          ║"
echo "╚════════════════════════════════════════════════════════════════╝"

echo -e "\n${BLUE}Once both are running:${NC}"
echo ""
echo "1. Open Browser: http://localhost:3000"
echo ""
echo "2. Click 'Register' and fill form:"
echo "   Username: testuser1"
echo "   Email: test@example.com"
echo "   Password: password123"
echo "   Grade: 7"
echo ""
echo "3. Click 'Register'"
echo "   → Should automatically go to Evaluation Form"
echo ""
echo "4. Complete 8 questions:"
echo "   - Answer all questions"
echo "   - See your score"
echo "   - View knowledge level badge"
echo ""
echo "5. Verify in MongoDB:"
echo "   - Open MongoDB Compass"
echo "   - Check 'edupex' > 'users' collection"
echo "   - Find user with email: test@example.com"
echo "   - Verify 'nivelCunostinte' field is set"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║                     Useful Commands                            ║"
echo "╚════════════════════════════════════════════════════════════════╝"

echo -e "\n${BLUE}Test Backend Endpoints:${NC}"
echo "  curl http://localhost:5000/api/users/evaluation-questions/7"
echo ""

echo -e "${BLUE}View Logs:${NC}"
echo "  Backend: Check terminal window 1"
echo "  Frontend: Check terminal window 2"
echo "  Browser: Press F12 and go to Console tab"
echo ""

echo -e "${BLUE}Clear All Data:${NC}"
echo "  # Delete MongoDB database and start fresh"
echo "  use edupex"
echo "  db.dropDatabase()"
echo ""

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║              For More Details, Read:                           ║"
echo "╚════════════════════════════════════════════════════════════════╝"

echo -e "\n${GREEN}Files to reference:${NC}"
echo "  📖 LOCAL_TESTING_GUIDE_EVALUATION.md - Detailed testing guide"
echo "  📖 EVALUATION_QUICK_START.md - Feature overview"
echo "  📖 EVALUATION_IMPLEMENTATION_GUIDE.md - Technical docs"
echo ""

echo -e "${GREEN}Happy Testing! 🚀${NC}"

