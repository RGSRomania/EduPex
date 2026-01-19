# 🔐 Hardcoded Credentials & Testing Guide

## 📝 Overview

For offline/external device testing without network access, EduPex includes hardcoded test credentials directly in the APK. This allows users to:

1. ✅ Download the APK
2. ✅ Install it on any Android device
3. ✅ Login with one-click demo button (no typing needed)
4. ✅ Test the full application without network setup

---

## 🔑 Current Test Credentials

### Primary Test User

| Property | Value |
|----------|-------|
| **Email** | `test@edupex.com` |
| **Password** | `test123` |
| **Username** | `testedupex` |
| **First Name** | `Test` |
| **Last Name** | `User` |
| **Grade Level** | 5 |

This user is created in the backend MongoDB database and has:
- ✅ Valid hashed password
- ✅ Complete profile information
- ✅ Grade level 5 (will see grade 5 lessons)
- ✅ Initial XP: 0
- ✅ Initial Level: 1
- ✅ Initial Streak: 0
- ✅ Initial Hearts: 5

---

## 🎯 How Hardcoded Credentials Work

### 1. Frontend Login Page (`frontend/src/pages/Login.js`)

The login page includes a **"Demo Login" button** with hardcoded credentials:

```javascript
const handleDemoLogin = async () => {
  // Hardcoded demo credentials for APK distribution
  const demoEmail = 'test@edupex.com';
  const demoPassword = 'test123';

  setFormData({
    email: demoEmail,
    password: demoPassword
  });

  // Trigger login with demo credentials
  await performLogin(demoEmail, demoPassword);
};
```

**Button Text**: "🎓 Intră cu Cont Demo" (Romanian for "Enter with Demo Account")

### 2. What Happens When Clicking Demo Button

1. **Form is auto-populated** with email and password
2. **`performLogin()` is called** immediately
3. **POST request sent** to `/api/users/login` with credentials:
   ```json
   {
     "email": "test@edupex.com",
     "password": "test123"
   }
   ```
4. **Backend validates credentials** against MongoDB
5. **JWT token is generated** and returned
6. **Token is stored** in browser's localStorage
7. **User is redirected** to Dashboard

### 3. Backend Login Route (`backend/routes/userRoutes.js`)

The backend login endpoint:

```javascript
router.post('/login', async (req, res) => {
  try {
    const { email, password } = req.body;

    // Find user by email
    const user = await User.findOne({ email });
    if (!user) {
      return res.status(401).json({ message: 'Credențiale invalide' });
    }

    // Verify password (uses bcrypt)
    const isMatch = await user.isValidPassword(password);
    if (!isMatch) {
      return res.status(401).json({ message: 'Credențiale invalide' });
    }

    // Generate JWT token
    const token = jwt.sign({ userId: user._id }, process.env.JWT_SECRET, { expiresIn: '7d' });

    res.json({
      message: 'Login successful',
      token,
      user: {
        id: user._id,
        username: user.username,
        firstName: user.firstName,
        lastName: user.lastName,
        email: user.email,
        gradeLevel: user.gradeLevel,
        xpPoints: user.xpPoints,
        level: user.level,
        // ... more fields
      }
    });
  } catch (error) {
    res.status(500).json({ message: 'Server error' });
  }
});
```

---

## 🛠️ Setting Up Test Credentials

### Step 1: Create Test User in Database

Ensure the test user exists in MongoDB:

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
node checkTestUser.js
```

This script will:
- ✅ Connect to MongoDB
- ✅ Check if `test@edupex.com` exists
- ✅ Create it if it doesn't exist
- ✅ Update password if incorrect
- ✅ Verify everything is working

### Step 2: Verify Test Credentials in Frontend

The credentials are hardcoded in:
- **File**: `frontend/src/pages/Login.js`
- **Function**: `handleDemoLogin()`
- **Lines**: 31-40 (approximately)

To change credentials, edit:

```javascript
const demoEmail = 'test@edupex.com';      // ← Change email here
const demoPassword = 'test123';            // ← Change password here
```

### Step 3: Rebuild APK

After any changes to frontend:

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
```

---

## 🔄 Complete Login Flow (With Demo Credentials)

### Flow Diagram

```
┌─────────────────────────────────────────────────────┐
│  User Installs APK on Device (No Same Network)     │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  App Launches → Login Page Visible                  │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  User Sees "🎓 Intră cu Cont Demo" Button          │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  User Clicks Demo Button                            │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Frontend Auto-fills:                               │
│  - Email: test@edupex.com                          │
│  - Password: test123                               │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Frontend Sends POST to:                            │
│  https://edupex-backend.onrender.com/api/users/login│
│  (Production backend - no network dependency)      │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Backend Validates Credentials:                     │
│  1. Find user with email = "test@edupex.com"       │
│  2. Verify password = "test123" (bcrypt)           │
│  3. Update lastActive timestamp                    │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Backend Generates JWT Token:                       │
│  - Token expires in 7 days                          │
│  - Contains userId and timestamp                    │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Backend Returns:                                   │
│  {                                                  │
│    "token": "eyJhbGc...",                          │
│    "user": {                                        │
│      "id": "...",                                   │
│      "username": "testedupex",                      │
│      "email": "test@edupex.com",                   │
│      "firstName": "Test",                           │
│      "lastName": "User",                            │
│      "gradeLevel": 5,                               │
│      "xpPoints": 0,                                 │
│      "level": 1                                     │
│    }                                                │
│  }                                                  │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Frontend Stores in localStorage:                   │
│  - token: JWT string                                │
│  - user: User object (JSON)                         │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  Frontend Redirects to Dashboard                    │
└────────────────────┬────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────┐
│  ✅ User Is Logged In & Can Access:                │
│  - Dashboard with XP, level, streak, hearts        │
│  - Lessons for their grade level                   │
│  - Quizzes and achievements                        │
│  - AI Assistant help                               │
│  - Progress tracking                               │
└─────────────────────────────────────────────────────┘
```

---

## 📱 Testing Scenarios

### Scenario 1: First Time Installation

1. **User downloads APK** from email/cloud
2. **User installs APK** on Android device
3. **User opens app**
4. **User clicks "🎓 Intră cu Cont Demo"**
5. ✅ **App navigates to Dashboard**

### Scenario 2: Manual Credential Entry

1. **User opens app**
2. **User manually enters**:
   - Email: `test@edupex.com`
   - Password: `test123`
3. **User clicks "Autentificare" button**
4. ✅ **App navigates to Dashboard**

### Scenario 3: Offline-First Test

1. **Device has no internet initially**
2. **APK is installed and app starts**
3. **Device connects to internet**
4. **User clicks demo button**
5. ✅ **Login succeeds with deployed backend**

---

## 🔍 Verifying Credentials Work

### Test 1: Using cURL (From Computer)

```bash
# Test login endpoint
curl -X POST https://edupex-backend.onrender.com/api/users/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@edupex.com",
    "password": "test123"
  }'

# Expected response (success):
# {
#   "message": "Login successful",
#   "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "user": {
#     "id": "...",
#     "username": "testedupex",
#     "firstName": "Test",
#     "lastName": "User",
#     "email": "test@edupex.com",
#     "gradeLevel": 5,
#     "xpPoints": 0,
#     "level": 1,
#     ...
#   }
# }
```

### Test 2: Via Frontend Dev Console

```javascript
// In browser console (when running frontend locally)
const response = await fetch('http://localhost:5000/api/users/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'test@edupex.com',
    password: 'test123'
  })
});

const data = await response.json();
console.log(data);

// Store token
localStorage.setItem('token', data.token);
localStorage.setItem('user', JSON.stringify(data.user));
```

### Test 3: In Installed APK

1. **Install APK** on device
2. **Open app**
3. **Click demo button**
4. **Check browser DevTools** (if connected):
   ```javascript
   localStorage.getItem('token')  // Should show JWT token
   JSON.parse(localStorage.getItem('user'))  // Should show user object
   ```

---

## 🔐 Security Notes

⚠️ **Important Considerations:**

1. **Demo Credentials in APK**
   - Only for testing/demo purposes
   - Not for production Play Store release
   - All users will share same account
   - No user isolation

2. **Password Storage**
   - Password is NOT stored in plain text
   - Backend uses bcrypt (10 salt rounds)
   - Password verified on server, never sent in API responses

3. **JWT Token**
   - Expires in 7 days
   - Stored in localStorage (not httpOnly)
   - Included in Authorization header for API calls
   - Should use httpOnly cookie in production

4. **For Production Release**
   - Remove demo login button
   - Remove hardcoded credentials
   - Implement proper authentication
   - Use secure token storage
   - Add rate limiting on login endpoint
   - Add CAPTCHA for login page

---

## 🔄 Changing Credentials

### To use different test credentials:

#### 1. Edit Frontend (Login Page)

```bash
# File: frontend/src/pages/Login.js
# Lines: ~31-40

const demoEmail = 'your-new-email@example.com';    // Change this
const demoPassword = 'your-new-password';           // Change this
```

#### 2. Create User in Backend

```bash
# Create new user with same credentials
# Option 1: Use registration endpoint
curl -X POST http://localhost:5000/api/users/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "newusername",
    "email": "your-new-email@example.com",
    "password": "your-new-password",
    "firstName": "Your",
    "lastName": "Name",
    "gradeLevel": 6
  }'

# Option 2: Manually create via MongoDB
# Or use checkTestUser.js as template
```

#### 3. Rebuild APK

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
```

---

## 📊 Test User Data Structure

When user logs in, they receive complete profile:

```javascript
{
  "id": "507f1f77bcf86cd799439011",              // MongoDB ObjectId
  "username": "testedupex",
  "firstName": "Test",
  "lastName": "User",
  "email": "test@edupex.com",
  "gradeLevel": 5,                                // Determines visible lessons
  "xpPoints": 0,                                  // Experience points
  "level": 1,                                     // Current level
  "streak": 0,                                    // Days of consecutive learning
  "hearts": 5,                                    // Lives
  "achievements": [],                             // Unlocked badges
  "preferences": {
    "aiTeacherGender": "female",                 // Male/female assistant
    "notificationsEnabled": true,
    "dailyGoal": 50                              // XP daily goal
  },
  "createdAt": "2024-01-15T10:30:00.000Z"
}
```

---

## 📝 Files Containing Hardcoded Credentials

| File | Type | Purpose |
|------|------|---------|
| `frontend/src/pages/Login.js` | Frontend | Hardcoded demo login button and credentials |
| `backend/checkTestUser.js` | Backend Script | Creates/verifies test user in database |
| `backend/models/User.js` | Database Schema | Defines user structure |
| `backend/routes/userRoutes.js` | API Route | Handles login requests |
| `.env` (backend) | Config | JWT_SECRET and MongoDB URI |

---

## ✅ Testing Checklist

Before distributing APK:

- [ ] Test user `test@edupex.com` exists in database
- [ ] Password `test123` works with user
- [ ] Backend login endpoint responds correctly
- [ ] Frontend demo button shows on login page
- [ ] Demo button auto-fills credentials
- [ ] Demo button triggers login successfully
- [ ] JWT token is generated and returned
- [ ] Token is stored in localStorage
- [ ] User is redirected to Dashboard
- [ ] Dashboard loads user's data correctly
- [ ] All API calls include auth token
- [ ] Manual login also works with same credentials
- [ ] APK size is reasonable (~50-70 MB)
- [ ] No console errors in browser
- [ ] No crash reports

---

## 🎯 Summary

**For offline device testing:**
1. ✅ APK is built with production backend URL hardcoded
2. ✅ Frontend includes demo login button
3. ✅ Credentials are hardcoded in frontend
4. ✅ Test user exists in backend database
5. ✅ Device can install and use APK without same-network setup
6. ✅ One-click login for demo testing

**Result:** Users can download APK, install it, and login with a single click without any configuration!


