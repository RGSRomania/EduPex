#!/bin/bash
set -e

cd /Users/mdica/PycharmProjects/EduPex

echo "=== Evaluation Form Fix - Git Commit and Push ==="
echo ""
echo "Step 1: Adding all changes..."
git add backend/curriculum_structure.json
git add backend/routes/userRoutes.js
git add fix-evaluation-backend.sh
git add commit_and_push.py
git add EVALUATION_FORM_FIX_IMPLEMENTATION.md
git add EVALUATION_FIX_ACTION_ITEMS.md

echo "Step 2: Checking status..."
git status --short

echo ""
echo "Step 3: Creating commit..."
git commit -m "Fix: Evaluation form questions not displaying - Add curriculum to backend

Changes:
- Copy curriculum_structure.json to backend directory for Render deployment
- Enhance backend evaluation route with 7 fallback paths to find curriculum file
- Fix ensures real questions display instead of placeholder 'Clasa a Xa - Întrebare...' text
- Backend will now properly extract and return educational questions for all grade levels

Expected result:
- Emulator now shows: 'Câte cifre sunt utilizate în sistemul de numerație zecimal?'
- Instead of: 'Clasa a 5a - Întrebare Matematică 1?'
- All 8 evaluation questions (4 math + 4 language) will display real curriculum content

This fix resolves the issue where Render deployment couldn't find curriculum file."

echo "Step 4: Pushing to GitHub..."
git push origin main

echo ""
echo "=== SUCCESS ==="
echo "✅ All changes committed and pushed"
echo "✅ Render will automatically redeploy (2-5 minutes)"
echo "✅ Monitor: https://dashboard.render.com"
echo ""
echo "Next: Test API at https://edupex-backend.onrender.com/api/users/evaluation-questions/5"

