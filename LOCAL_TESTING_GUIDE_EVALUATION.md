# 🧪 Local Testing Guide - Evaluation Form

**Date:** January 23, 2026  
**Purpose:** Step-by-step guide to test evaluation form locally

---

## ✅ Prerequisites

Before starting, make sure you have:
- [x] Node.js installed (v14+)
- [x] npm installed (v6+)
- [x] MongoDB running locally OR MongoDB Atlas connection string
- [x] Git (optional, but recommended)

**Verify Installation:**
```bash
node --version  # Should be v14 or higher
npm --version   # Should be v6 or higher
```

---

## 🚀 Step 1: Backend Setup & Testing

### 1.1 Navigate to Backend Directory
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
```

### 1.2 Install Dependencies
```bash
npm install
```

### 1.3 Configure Environment

Create/update `.env` file with:
```env
MONGODB_URI=mongodb://localhost:27017/edupex
# OR use MongoDB Atlas:
# MONGODB_URI=mongodb+srv://username:password@cluster.mongodb.net/edupex

JWT_SECRET=your_secret_key_here_change_in_production
PORT=5000
NODE_ENV=development
```

### 1.4 Start Backend Server
```bash
npm start
```

**Expected Output:**
```
✅ Connected to MongoDB
✅ Server running on http://localhost:5000
```

### 1.5 Test Backend Endpoints

**Test 1: Get Evaluation Questions**
```bash
curl http://localhost:5000/api/users/evaluation-questions/7
```

**Expected Response:**
```json
{
  "matematica": [
    {
      "id": "math1",
      "subject": "Matematica",
      "question": "Clasa a 7a - Întrebare Matematică 1?",
      "options": ["A", "B", "C", "D"],
      "correctAnswer": 0
    },
    ...
  ],
  "limba": [...]
}
```

---

## 🎨 Step 2: Frontend Setup & Testing

### 2.1 Open New Terminal & Navigate to Frontend
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
```

### 2.2 Install Dependencies
```bash
npm install
```

### 2.3 Configure Environment

Create/update `.env.local` file with:
```env
REACT_APP_API_BASE_URL=http://localhost:5000/api
REACT_APP_ENVIRONMENT=development
```

### 2.4 Start Frontend Server
```bash
npm start
```

**Expected Output:**
```
✅ Compiled successfully!
✅ To create a production build, run: npm run build
✅ Open http://localhost:3000 to view in browser
```

---

## 🧪 Step 3: Test Registration → Evaluation Flow

### 3.1 Open Browser
Navigate to: **http://localhost:3000**

### 3.2 Go to Registration Page
Click: **Register** (or navigate to `/register`)

### 3.3 Fill Registration Form
```
Username: testuser1
Email: test@example.com
Password: password123
First Name: John
Last Name: Doe
Grade Level: 7 (select dropdown)
```

### 3.4 Click Register
✅ **Expected:** Automatic redirect to evaluation form

---

## 📋 Step 4: Test Evaluation Form

### 4.1 Verify Evaluation Form Loads
✅ Should see:
- Title: "Evaluare de Plasament"
- Progress bar showing "Question 1 of 8"
- First evaluation question displayed
- 4 answer options (A, B, C, D)

### 4.2 Test Question Navigation

**Test Navigation Forward:**
```
1. Select an answer option
2. Click "Următoare" (Next) button
3. Verify: Question 2 appears
4. Verify: Progress bar updates to "Question 2 of 8"
```

**Test Navigation Backward:**
```
1. Click "Înapoi" (Back) button
2. Verify: Question 1 appears again
3. Verify: Previous answer is remembered
```

### 4.3 Test Answer Selection
```
1. Click different answer options
2. Verify: Selected option is highlighted in blue
3. Verify: Can change answer before moving next
```

### 4.4 Test Button Validation
```
1. Don't select any answer
2. Verify: "Următoare" button is disabled (grayed out)
3. Select an answer
4. Verify: "Următoare" button becomes enabled
```

### 4.5 Complete Full Evaluation
```
Answer all 8 questions (navigate through all):
- Questions 1-4: Math questions
- Questions 5-8: Romanian language questions
```

---

## 📊 Step 5: Test Scoring

### 5.1 Test Score Calculation (Scenario 1: Incepator)
```
Answer 2 questions correctly (out of 8)
Expected Result:
  - Matematica: X/4
  - Limba: X/4
  - Total: 2/8
  - Knowledge Level: INCEPATOR (0-3 correct)
```

### 5.2 Test Score Calculation (Scenario 2: Mediu)
```
Answer 5 questions correctly
Expected Result:
  - Matematica: X/4
  - Limba: X/4
  - Total: 5/8
  - Knowledge Level: MEDIU (4-6 correct)
```

### 5.3 Test Score Calculation (Scenario 3: Avansat)
```
Answer 7 questions correctly
Expected Result:
  - Matematica: X/4
  - Limba: X/4
  - Total: 7/8
  - Knowledge Level: AVANSAT (7-8 correct)
```

---

## ✅ Step 6: Verify Results Page

After completing all 8 questions:

✅ **Should See:**
- Results heading: "Evaluare Completă!"
- Emoji: 🎓
- Score breakdown:
  - 📐 Matematica: X/4
  - 📚 Limba: X/4
  - Total: X/8
- Knowledge level badge with color
- Personalized message based on level
- Button: "Continuă către Dashboard"

### 6.1 Click Dashboard Button
✅ **Expected:** Redirected to `/dashboard`

---

## 💾 Step 7: Verify Database Persistence

### 7.1 Check User Record in MongoDB

**Option A: Using MongoDB Compass**
1. Open MongoDB Compass
2. Connect to: `mongodb://localhost:27017`
3. Go to: `edupex` database → `users` collection
4. Find user with email `test@example.com`
5. Verify fields:
   - `nivelCunostinte`: Should be "Incepator", "Mediu", or "Avansat"
   - `evaluationScores.matematica`: Number (0-4)
   - `evaluationScores.limba`: Number (0-4)
   - `evaluationScores.total`: Number (0-8)
   - `evaluationScores.completedAt`: Timestamp

**Option B: Using MongoDB Shell**
```bash
# Open MongoDB shell
mongo

# Switch to database
use edupex

# Find user
db.users.findOne({ email: "test@example.com" })

# Verify evaluationScores and nivelCunostinte fields exist
```

---

## 🔄 Step 8: Test Different Scenarios

### Scenario A: Test All Grade Levels
```
Register 4 users with different grade levels:
1. Grade 5 user
2. Grade 6 user
3. Grade 7 user
4. Grade 8 user

Verify: Questions appear for correct grade level
```

### Scenario B: Test Error Handling
```
1. Close browser during evaluation
   Expected: Session preserved, can login again
   
2. Disable internet/backend
   Expected: Clear error message shown
   
3. Refresh page during evaluation
   Expected: Can continue evaluation with saved answers
```

### Scenario C: Test Mobile Experience
```
1. Open Chrome DevTools (F12)
2. Toggle Device Toolbar (Ctrl+Shift+M)
3. Select: iPhone 12 (390x844)
4. Verify:
   - Form is readable on mobile
   - Buttons are clickable
   - Text is sized appropriately
   - No horizontal scrolling
```

### Scenario D: Test Different Browsers
```
Test on:
- Chrome (recommended for development)
- Firefox
- Safari (if on Mac)
- Edge

Verify: Same experience across browsers
```

---

## 🐛 Step 9: Check Console for Errors

### 9.1 Frontend Console
```
1. Open Browser DevTools (F12)
2. Go to "Console" tab
3. Verify: No red errors or warnings
4. Look for: Request/response logs from API
```

### 9.2 Backend Console
```
Terminal where backend is running should show:
✅ GET /api/users/evaluation-questions/7
✅ POST /api/users/evaluate
✅ No error messages
```

---

## 📊 Step 10: Performance Testing

### 10.1 Measure Page Load Time
```
1. Open DevTools (F12)
2. Go to "Network" tab
3. Reload evaluation page
4. Check: "DOMContentLoaded" and "Load" times
5. Target: < 2 seconds total load
```

### 10.2 Measure API Response Time
```
1. In Network tab, look for:
   - /api/users/evaluation-questions/7
   - /api/users/evaluate
2. Check Response time
3. Target: < 500ms for questions, < 1s for evaluation
```

### 10.3 Check Memory Usage
```
1. Open DevTools (F12)
2. Go to "Memory" tab
3. Take Heap snapshot
4. Interact with evaluation form
5. Take another snapshot
6. Verify: Memory increase is reasonable (< 10MB)
```

---

## 🔐 Step 11: Security Testing

### 11.1 Test Authentication
```
1. Go to /evaluation without logging in
2. Expected: Redirected to login page
```

### 11.2 Test Password Validation
```
Register with passwords:
1. "123" (too short)
   Expected: Error message "Password too short"
   
2. "password123" (valid)
   Expected: Registration succeeds
```

### 11.3 Test Duplicate Email
```
1. Register user with email1
2. Try to register another user with same email
3. Expected: Error "Email already exists"
```

---

## 📝 Testing Checklist

Use this checklist to track your local testing:

### Registration & Redirect
- [ ] Registration form loads
- [ ] Can fill all fields
- [ ] Submit button works
- [ ] Automatic redirect to /evaluation occurs

### Evaluation Form
- [ ] Form loads with 8 questions
- [ ] Questions display correctly
- [ ] Answer options are clickable
- [ ] Can select answers
- [ ] Can navigate forward
- [ ] Can navigate backward
- [ ] Progress bar updates
- [ ] Submit button enabled only when all answered

### Scoring & Results
- [ ] Correct score calculation (test 0-3, 4-6, 7-8)
- [ ] Knowledge level correct (Incepator/Mediu/Avansat)
- [ ] Results page displays
- [ ] Dashboard button works
- [ ] User can access dashboard

### Database
- [ ] User record created
- [ ] evaluationScores saved
- [ ] nivelCunostinte saved
- [ ] completedAt timestamp recorded

### Performance
- [ ] Page loads in < 2s
- [ ] API responses < 1s
- [ ] No console errors
- [ ] Mobile responsive

### Security
- [ ] Cannot access /evaluation without login
- [ ] Password validation works
- [ ] Duplicate email blocked

---

## 🛠️ Troubleshooting

### Issue: Backend won't start
**Solution:**
```bash
# Check MongoDB is running
mongod --version

# Check port 5000 is available
lsof -i :5000

# Kill process on port 5000 if needed
kill -9 <PID>

# Restart backend
npm start
```

### Issue: Frontend won't start
**Solution:**
```bash
# Check port 3000 is available
lsof -i :3000

# Clear npm cache
npm cache clean --force

# Reinstall dependencies
rm -rf node_modules package-lock.json
npm install

# Start frontend
npm start
```

### Issue: Cannot connect to MongoDB
**Solution:**
```bash
# Check .env file has correct MONGODB_URI
cat .env

# If using local MongoDB:
# Ensure MongoDB is running: brew services start mongodb-community

# If using MongoDB Atlas:
# Verify connection string has correct username/password/cluster
```

### Issue: Evaluation form not loading
**Solution:**
```
1. Check backend is running (http://localhost:5000)
2. Open browser console (F12)
3. Look for error messages
4. Check Network tab for failed requests
5. Verify .env has correct API URL
```

### Issue: Answers not saving
**Solution:**
1. Check backend console for POST errors
2. Verify token is being sent with request
3. Check MongoDB is connected
4. Verify user record exists in database

---

## 📋 Testing Report Template

After testing locally, fill out:

```
Testing Report - Evaluation Form
================================
Date: ___________
Tester: _________

Backend Status: ✅ / ❌
Frontend Status: ✅ / ❌
Database Status: ✅ / ❌

Features Tested:
- Registration: ✅ / ❌
- Evaluation: ✅ / ❌
- Scoring: ✅ / ❌
- Results: ✅ / ❌
- Dashboard: ✅ / ❌

Issues Found:
1. _____________
2. _____________
3. _____________

Overall Status: ✅ READY / ⚠️ NEEDS FIXES
```

---

## 🎉 Next Steps

After successful local testing:

1. ✅ All features working locally
2. ✅ No console errors
3. ✅ Database saving data correctly
4. ✅ All scenarios passing

**Then You Can:**
- Deploy to staging/production
- Share with team for testing
- Plan Phase 2 enhancements

---

## 📞 Support

If you encounter issues during local testing:

1. Check **EVALUATION_IMPLEMENTATION_GUIDE.md** for technical details
2. Check **DEPLOYMENT_CHECKLIST.md** for pre-deployment verification
3. Review code comments in:
   - `backend/routes/userRoutes.js`
   - `frontend/src/components/EvaluationForm.js`

---

**Happy Testing! 🚀**

Version: 1.0.0  
Date: January 23, 2026  
Status: ✅ READY FOR LOCAL TESTING

