#!/bin/bash

# ============================================================================
# EduPex - Evaluation Form & Curriculum Import Setup
# ============================================================================
# This script helps set up the evaluation form and database import

echo "╔════════════════════════════════════════════════════════════════╗"
echo "║     EduPex - Evaluation Form & Curriculum Setup              ║"
echo "╚════════════════════════════════════════════════════════════════╝"

# Step 1: Verify Node.js and npm
echo ""
echo "1️⃣  Checking Node.js and npm..."
if ! command -v node &> /dev/null; then
    echo "❌ Node.js is not installed. Please install Node.js first."
    exit 1
fi
echo "✅ Node.js found: $(node --version)"
echo "✅ npm found: $(npm --version)"

# Step 2: Install backend dependencies
echo ""
echo "2️⃣  Installing backend dependencies..."
cd backend || exit 1
npm install 2>&1 | tail -5
echo "✅ Backend dependencies installed"
cd ..

# Step 3: Install frontend dependencies
echo ""
echo "3️⃣  Installing frontend dependencies..."
cd frontend || exit 1
npm install 2>&1 | tail -5
echo "✅ Frontend dependencies installed"
cd ..

# Step 4: Display configuration information
echo ""
echo "4️⃣  Configuration Information"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Backend URL: http://localhost:5000"
echo "Frontend URL: http://localhost:3000"
echo ""
echo "New Endpoints Added:"
echo "  • POST /api/users/evaluate - Submit evaluation results"
echo "  • GET /api/users/evaluation-questions/:gradeLevel - Get evaluation questions"
echo ""
echo "New Database Fields in User Model:"
echo "  • nivelCunostinte (string): 'Incepator', 'Mediu', or 'Avansat'"
echo "  • evaluationScores (object):"
echo "    - matematica: number (0-4)"
echo "    - limba: number (0-4)"
echo "    - total: number (0-8)"
echo "    - completedAt: date"
echo ""

# Step 5: Database Import Information
echo "5️⃣  Database Import Setup"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "To import curriculum_structure.json into MongoDB:"
echo ""
echo "  cd backend"
echo "  node scripts/importCurriculum.js"
echo ""
echo "⚠️  WARNING: This will DELETE all existing curriculum data!"
echo "Make sure to have a backup if needed."
echo ""

# Step 6: Starting the application
echo "6️⃣  Starting the Application"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Option A: Start both frontend and backend"
echo "  npm start"
echo ""
echo "Option B: Start backend only"
echo "  cd backend && npm start"
echo ""
echo "Option C: Start frontend only"
echo "  cd frontend && npm start"
echo ""

# Step 7: Testing the evaluation form
echo "7️⃣  Testing the Evaluation Form"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "1. Register a new user at: http://localhost:3000/register"
echo "2. You will be redirected to evaluation form"
echo "3. Complete the 8-question evaluation"
echo "4. Your knowledge level (Incepator/Mediu/Avansat) will be set"
echo ""

echo ""
echo "✅ Setup complete! Ready to start development."
echo ""

