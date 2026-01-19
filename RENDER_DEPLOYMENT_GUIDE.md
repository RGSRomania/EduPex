# 📋 Render.com Deployment Guide for EduPex Backend

## What's Been Prepared

✅ Backend code ready  
✅ .env.production file created  
✅ .gitignore configured  
✅ Git repository initialized  
✅ Code committed  

---

## STEP-BY-STEP DEPLOYMENT

### STEP 1: Push Backend to GitHub

Run these commands in terminal:

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend

# Add GitHub remote (replace YOUR_USERNAME with your actual GitHub username)
git remote add origin https://github.com/RGSRomania/edupex-backend.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Verify it worked**: Go to https://github.com/RGSRomania/edupex-backend and see your code

---

### STEP 2: Deploy to Render.com

#### 2.1 Create Account
- Go to https://render.com
- Click "Sign up"
- Sign in with GitHub (click "GitHub" button)
- Authorize Render to access your GitHub account

#### 2.2 Create Web Service
1. Click "New +" button (top right)
2. Select "Web Service"
3. Click "Connect a repository"
4. Find and select `edupex-backend` (click "Connect")

#### 2.3 Configure Service
Fill in these fields:

| Field | Value |
|-------|-------|
| Name | `edupex-backend` |
| Environment | `Node` |
| Region | `Oregon (US West)` |
| Branch | `main` |
| Build Command | `npm install` |
| Start Command | `npm start` |
| Instance Type | `Free` |

#### 2.4 Add Environment Variables
Click "Add Environment Variable" and add these:

```
MONGODB_URI = mongodb://localhost:27017/edupex
JWT_SECRET = edupex_super_secret_key_2026_change_this_in_production
NODE_ENV = production
PORT = 5000
```

**Note**: If you get MongoDB errors, you'll need to set up MongoDB Atlas (free tier). See section below.

#### 2.5 Click "Create Web Service"

Wait 3-5 minutes for deployment...

---

### STEP 3: Get Your Backend URL

When deployment completes, Render will show a URL like:
```
https://edupex-backend-xxxxx.onrender.com
```

**Copy this URL!** You'll need it in the next step.

---

### STEP 4: Update APK Configuration

Update this file:
`/Users/mdica/PycharmProjects/EduPex/frontend/src/config/apiConfig.js`

Change line 16 from:
```javascript
return 'https://edupex-backend.onrender.com/api';
```

To your actual Render URL:
```javascript
return 'https://edupex-backend-xxxxx.onrender.com/api';
```

---

### STEP 5: Build APK

Once API config is updated:

```bash
cd /Users/mdica/PycharmProjects/EduPex
./build-apk-fixed.sh
```

This builds the APK with your actual backend URL hardcoded in it.

---

## MONGODB SETUP (If Needed)

If you get MongoDB connection errors, set up MongoDB Atlas:

### Free MongoDB Atlas Setup

1. Go to https://www.mongodb.com/cloud/atlas
2. Click "Try Free"
3. Create account with email
4. Create a project (name it "EduPex")
5. Create a cluster (select "Free" tier)
6. Wait 5-10 minutes for cluster to build
7. Click "Connect"
8. Select "Drivers" → "Node.js"
9. Copy the connection string
10. Replace `<username>`, `<password>`, `<database>` in the string
11. Update MongoDB URI in Render environment variables

Connection string template:
```
mongodb+srv://username:password@cluster.mongodb.net/edupex?retryWrites=true&w=majority
```

Then redeploy on Render (click "Manual Deploy" or push new commit).

---

## TROUBLESHOOTING

### Deployment Failed
- Check build logs in Render dashboard
- Common issues:
  - Missing environment variables
  - MongoDB connection error
  - Node version mismatch

### Backend Returns 500 Error
- Check Render logs
- Verify MongoDB is running
- Verify environment variables

### Login Doesn't Work
- Verify test user exists in MongoDB
- Check JWT_SECRET matches everywhere
- Verify CORS is enabled in server.js

---

## COMMANDS QUICK REFERENCE

```bash
# Push to GitHub (one time)
cd backend
git remote add origin https://github.com/RGSRomania/edupex-backend.git
git push -u origin main

# Update APK config with new backend URL
# Edit: frontend/src/config/apiConfig.js line 16

# Build APK
cd /Users/mdica/PycharmProjects/EduPex
./build-apk-fixed.sh
```

---

## Timeline

| Step | Duration | When |
|------|----------|------|
| Push to GitHub | 1 min | Now |
| Deploy to Render | 3-5 min | After push |
| Get Render URL | Instant | When ready |
| Update API config | 1 min | After URL |
| Build APK | 5-10 min | After update |
| **Total** | **~20 min** | |

---

## Status Checklist

After each step, verify:

- [ ] Backend code pushed to GitHub
- [ ] Render deployment started (check dashboard)
- [ ] Render shows "Live" status
- [ ] Got backend URL from Render
- [ ] Updated apiConfig.js with new URL
- [ ] APK build completed
- [ ] APK file exists (~50-70 MB)
- [ ] Ready to install on device!

---

## What's Next After Deployment

1. ✅ Backend deployed to Render
2. ✅ APK built with backend URL
3. ⏭️ Install APK on device: `adb install app-debug.apk`
4. ⏭️ Test demo login
5. ✅ Success!

---

## Still Stuck?

All the files needed are ready. Just:

1. **Push to GitHub** (follow Step 1 above)
2. **Deploy on Render** (follow Step 2 above)  
3. **Get URL and update config** (Step 3-4)
4. **Build APK** (Step 5)

That's it! You're ready to go! 🚀


