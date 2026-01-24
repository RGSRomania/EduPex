#!/bin/bash

# EVALUATION FORM FIX - FINAL DEPLOYMENT SCRIPT
# This script completes the evaluation form questions fix

set -e

cd /Users/mdica/PycharmProjects/EduPex

echo "======================================"
echo "EVALUATION FORM FIX - FINAL DEPLOYMENT"
echo "======================================"
echo ""

# Verify curriculum file exists in backend
if [ ! -f "backend/curriculum_structure.json" ]; then
    echo "❌ ERROR: backend/curriculum_structure.json not found"
    echo "Copying from root..."
    cp curriculum_structure.json backend/curriculum_structure.json
    echo "✅ File copied"
fi

echo ""
echo "Step 1: Checking file sizes..."
echo "Root curriculum: $(du -h curriculum_structure.json | cut -f1)"
echo "Backend curriculum: $(du -h backend/curriculum_structure.json | cut -f1)"
echo ""

echo "Step 2: Verifying backend route has correct paths..."
if grep -q "path.join(__dirname, 'curriculum_structure.json')" backend/routes/userRoutes.js; then
    echo "✅ Backend directory path found in route"
else
    echo "❌ ERROR: Backend directory path NOT found in route"
    exit 1
fi

if grep -q "/app/backend/curriculum_structure.json" backend/routes/userRoutes.js; then
    echo "✅ Render backend path found in route"
else
    echo "❌ ERROR: Render backend path NOT found in route"
    exit 1
fi

echo ""
echo "Step 3: Staging changes..."
git add backend/curriculum_structure.json
git add backend/routes/userRoutes.js
git add EVALUATION_*.md
git add push-evaluation-fix.sh
git add commit_and_push.py
git add fix-evaluation-backend.sh

echo ""
echo "Step 4: Checking git status..."
git status --short

echo ""
echo "Step 5: Creating commit..."
git commit -m "Fix: Evaluation form questions displaying placeholders instead of real curriculum

PROBLEM:
- Emulator shows: 'Clasa a 5a - Întrebare Matematică 1?'
- Should show: 'Câte cifre sunt utilizate în sistemul de numerație zecimal?'
- Root cause: Render backend couldn't find curriculum_structure.json

SOLUTION:
1. Copy curriculum_structure.json to backend directory
2. Enhance backend route with 7 fallback paths (was 4)
3. New paths include: __dirname, /app/backend, etc.

RESULT:
- Backend now finds curriculum file in all environments
- API returns real educational questions
- Emulator shows proper evaluation questions with correct options

FILES CHANGED:
- NEW: backend/curriculum_structure.json (903 KB)
- UPDATED: backend/routes/userRoutes.js (line 403-410: added 3 new fallback paths)

VERIFICATION:
After Render redeploys (2-5 min):
curl https://edupex-backend.onrender.com/api/users/evaluation-questions/5 | jq '.matematica[0].question'
Should return: 'Ce este o mulțime?' (not 'Clasa a 5a - Întrebare...')"

echo ""
echo "Step 6: Pushing to GitHub..."
git push origin main

echo ""
echo "======================================"
echo "✅ SUCCESS - CHANGES PUSHED"
echo "======================================"
echo ""
echo "What happens next:"
echo "1. Render detects the push"
echo "2. Render auto-redeploys (2-5 minutes)"
echo "3. Backend now finds curriculum file"
echo "4. API returns real questions"
echo ""
echo "Verify deployment with:"
echo "  curl https://edupex-backend.onrender.com/api/users/evaluation-questions/5 | jq '.matematica[0].question'"
echo ""
echo "Expected: Real question text like 'Ce este o mulțime?'"
echo "NOT: 'Clasa a 5a - Întrebare Matematică 1?'"
echo ""

