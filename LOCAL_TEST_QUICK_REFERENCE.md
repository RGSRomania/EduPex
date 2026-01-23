# 🚀 Local Testing - Quick Reference Card
**Print this or bookmark it! Quick copy-paste commands.**
---
## ⚡ Super Quick Start (5 minutes)
### Terminal 1 - Backend
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
npm install
npm start
```
### Terminal 2 - Frontend
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm install
npm start
```
### Browser
```
http://localhost:3000/register
```
---
## 📝 Quick Test Checklist
```
Quick Test (5 min):
  [ ] Register → Grade 7
  [ ] Complete 8 questions
  [ ] See results page
  [ ] Knowledge level shows
Full Test (30 min):
  [ ] Test all 3 knowledge levels (0-3, 4-6, 7-8)
  [ ] Test all grade levels (5, 6, 7, 8)
  [ ] Mobile responsive (F12 → Toggle Device)
  [ ] No console errors (F12 → Console tab)
  [ ] Database saved data (MongoDB Compass)
```
---
## 🧪 Test API Endpoints (Copy-Paste)
### Get Questions for Grade 7
```bash
curl http://localhost:5000/api/users/evaluation-questions/7
```
### Get Questions for Other Grades
```bash
# Grade 5
curl http://localhost:5000/api/users/evaluation-questions/5
# Grade 6
curl http://localhost:5000/api/users/evaluation-questions/6
# Grade 8
curl http://localhost:5000/api/users/evaluation-questions/8
```
---
## 🔧 Common Issues & Quick Fixes
### Backend won't start
```bash
# Kill process on port 5000
lsof -i :5000
kill -9 <PID>
# Try again
npm start
```
### Frontend won't start
```bash
# Kill process on port 3000
lsof -i :3000
kill -9 <PID>
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
npm start
```
### MongoDB connection error
```bash
# Start MongoDB locally
brew services start mongodb-community
# Or use MongoDB Atlas connection string in .env
MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/edupex
```
### Port already in use
```bash
# Change port in backend .env
PORT=5001
# Or kill process using port
lsof -i :5000
kill -9 <PID>
```
---
## 📊 Quick Test Scenarios
### Scenario 1: Incepator (0-3 correct)
```
Register with Grade 7
Answer 2 questions → See "Incepator" badge
```
### Scenario 2: Mediu (4-6 correct)
```
Register with Grade 6
Answer 5 questions → See "Mediu" badge
```
### Scenario 3: Avansat (7-8 correct)
```
Register with Grade 5
Answer 8 questions → See "Avansat" badge
```
---
## 🔐 Test Security
### Cannot access without login
```bash
curl http://localhost:5000/api/users/evaluate
# Should get 401 Unauthorized
```
### Password validation
```
Try register with "123" → Should fail
Try register with "password123" → Should work
```
---
## 📱 Test Mobile
In Chrome DevTools:
```
F12 → Ctrl+Shift+M → Select iPhone 12
```
---
## 💾 Check Database
### Using MongoDB Compass
```
1. Connect to localhost:27017
2. Go to: edupex > users
3. Find your test user
4. Check: nivelCunostinte field
```
### Using MongoDB Shell
```bash
mongo
use edupex
db.users.findOne({ email: "test@example.com" })
```
---
## 📝 Test Data Examples
### Test Account 1
```
Email: test1@example.com
Password: password123
Grade: 5
Expected: Various scores
```
### Test Account 2
```
Email: test2@example.com
Password: password123
Grade: 7
Expected: Various scores
```
### Test Account 3
```
Email: test3@example.com
Password: password123
Grade: 8
Expected: Various scores
```
---
## 🎯 Expected Results
| Correct | Level | Color |
|---------|-------|-------|
| 0-3 | Incepator | Blue |
| 4-6 | Mediu | Orange |
| 7-8 | Avansat | Green |
---
## 📊 Performance Targets
✅ Page Load: < 2 seconds
✅ API Response: < 1 second
✅ No Console Errors
✅ Mobile Responsive
---
## 🛠️ Useful DevTools Tips
### View Console Logs
```
F12 → Console tab
Look for: ✅ messages (success) or ❌ (errors)
```
### View Network Requests
```
F12 → Network tab
Filter by: XHR (API calls)
Check: Response times and payloads
```
### Test Mobile
```
F12 → Toggle Device Toolbar (Ctrl+Shift+M)
Test on: iPhone 12, iPad, Android
```
### Check Performance
```
F12 → Performance tab
Record interaction
Check: Frame rate (should be ~60fps)
```
---
## 📋 Full Test Checklist
```
BACKEND SETUP
  [ ] cd backend
  [ ] npm install
  [ ] npm start (should say "Server running on :5000")
FRONTEND SETUP  
  [ ] cd frontend
  [ ] npm install
  [ ] npm start (should open http://localhost:3000)
REGISTRATION
  [ ] Can fill all fields
  [ ] Submit works
  [ ] Redirects to /evaluation
EVALUATION FORM
  [ ] Loads with 8 questions
  [ ] Questions display properly
  [ ] Can select answers
  [ ] Can navigate back/forward
  [ ] Progress bar updates
  [ ] Cannot skip questions
SCORING (Test all 3 levels)
  [ ] 0-3 correct → Incepator
  [ ] 4-6 correct → Mediu
  [ ] 7-8 correct → Avansat
RESULTS
  [ ] Score breakdown shows
  [ ] Knowledge badge displays
  [ ] Button to dashboard works
DATABASE
  [ ] User saved in MongoDB
  [ ] evaluationScores exists
  [ ] nivelCunostinte exists
BROWSER & MOBILE
  [ ] Desktop works (Chrome, Firefox, Safari)
  [ ] Mobile responsive (F12 toggle)
  [ ] No console errors
  [ ] No network errors
```
---
## 🎉 Success Indicators
If you see:
✅ Registration → Evaluation redirect
✅ 8 questions displaying
✅ Score calculation working
✅ Knowledge level badge showing
✅ Data saved in MongoDB
✅ No console errors
**Then everything is working! 🚀**
---
## 📞 Need Help?
1. Check: `LOCAL_TESTING_GUIDE_EVALUATION.md` (detailed guide)
2. Check: `EVALUATION_IMPLEMENTATION_GUIDE.md` (technical docs)
3. Check: Console (F12) for error messages
4. Check: Backend terminal for API errors
---
**Happy Testing! 🧪**
Quick Start: bash quick-local-test.sh  
Full Guide: Open LOCAL_TESTING_GUIDE_EVALUATION.md
