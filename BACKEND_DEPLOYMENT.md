# Deploy EduPex Backend to HTTPS (Render)

## 📋 Complete Step-by-Step Deployment Guide

Follow these steps to deploy your backend to Render with HTTPS support for Google Play Store compliance.

---

## 🚀 Quick Start (Automated)

### Run the Deployment Helper Script:

```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
./deploy-to-render.sh
```

This script will:
- Initialize Git repository
- Create .gitignore
- Add and commit files
- Show you the next steps

---

## 📝 Manual Deployment Steps

### Step 1: Prepare Git Repository

```bash
# Navigate to project root
cd /Users/mdica/PycharmProjects/EduPex

# Initialize Git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Prepare backend for Render deployment"
```

### Step 2: Push to GitHub

1. **Create a new GitHub repository:**
   - Go to: https://github.com/new
   - Repository name: `EduPex`
   - Description: "Educational app for Romanian students"
   - Make it **Private** (recommended) or Public
   - Do NOT initialize with README (you already have files)
   - Click "Create repository"

2. **Push your code to GitHub:**
   ```bash
   # Add GitHub as remote (replace YOUR_USERNAME with your GitHub username)
   git remote add origin https://github.com/YOUR_USERNAME/EduPex.git
   
   # Push to GitHub
   git branch -M main
   git push -u origin main
   ```

### Step 3: Deploy to Render

1. **Sign up for Render:**
   - Go to: https://render.com
   - Click "Get Started for Free"
   - Sign up with GitHub (recommended) or email

2. **Create a New Web Service:**
   - Click the "New +" button in the top right
   - Select "Web Service"
   - Click "Connect account" to connect your GitHub
   - Find and select your "EduPex" repository
   - Click "Connect"

3. **Configure the Web Service:**

   Fill in these settings:

   | Setting | Value |
   |---------|-------|
   | **Name** | `edupex-backend` |
   | **Region** | `Oregon (US West)` or closest to your target users |
   | **Branch** | `main` |
   | **Root Directory** | `backend` |
   | **Runtime** | `Node` |
   | **Build Command** | `npm install` |
   | **Start Command** | `npm start` |
   | **Instance Type** | `Free` |

4. **Add Environment Variables:**

   Click "Advanced" → "Add Environment Variable" and add these (copy values from `backend/.env`):

   ```
   NODE_ENV=production
   PORT=10000
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_SERVICE_KEY=your_supabase_service_role_key_here
   LLM_PROVIDER=groq
   GROQ_API_KEY=your_groq_api_key_here
   OPENAI_API_KEY=your_openai_api_key_here
   CHATGPT_MODEL=gpt-4o
   JWT_SECRET=your_secure_jwt_secret_here
   ```

   ⚠️ **Security Note:** Replace all placeholder values with your actual API keys. Never commit real API keys to Git.

5. **Create Web Service:**
   - Click "Create Web Service"
   - Wait 2-5 minutes for deployment
   - Render will show deployment logs

6. **Get Your Backend URL:**
   - Once deployed, you'll see your URL at the top
   - Format: `https://edupex-backend.onrender.com`
   - Copy this URL - you'll need it for the next step

### Step 4: Update Frontend with Production URL

1. **Update `.env.production` file:**
   ```bash
   # Edit the file
   nano /Users/mdica/PycharmProjects/EduPex/frontend/.env.production
   ```

   Replace with your actual Render URL:
   ```
   REACT_APP_API_URL=https://YOUR-ACTUAL-URL.onrender.com/api
   NODE_ENV=production
   ```

2. **Update hardcoded fallback URLs in code:**

   Edit these 3 files and replace `https://edupex-backend.onrender.com/api` with your actual URL:

   - `frontend/src/utils/api.js` (line ~8)
   - `frontend/src/pages/Login.js` (line ~38)  
   - `frontend/src/components/aiAssistant/AIAssistantButton.js` (line ~8)

   Search for this line in each file:
   ```javascript
   ? 'https://edupex-backend.onrender.com/api'  // UPDATE THIS after deploying to Render
   ```

   And replace with:
   ```javascript
   ? 'https://YOUR-ACTUAL-URL.onrender.com/api'
   ```

### Step 5: Test Your Deployment

```bash
# Test the backend is running
curl https://YOUR-ACTUAL-URL.onrender.com/

# Expected response: "EduPex API is running"

# Test a specific endpoint
curl https://YOUR-ACTUAL-URL.onrender.com/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@test.com","password":"test123"}'

# Should return JSON response (even if credentials are invalid)
```

### Step 6: Build Production APK

```bash
# Navigate to frontend
cd /Users/mdica/PycharmProjects/EduPex/frontend

# Build React app with production environment
npm run build

# Sync with Capacitor
npx cap sync android

# Build release APK (after setting up keystore - see PLAY_STORE_REQUIREMENTS.md)
cd android
export JAVA_HOME=$(/usr/libexec/java_home -v 22)
./gradlew assembleRelease
```

---

## 🔄 Alternative Hosting Options

### Railway (Alternative to Render)

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select "EduPex" repository
5. Click on the service → Settings
6. Set **Root Directory**: `backend`
7. Add environment variables (same as Render)
8. Your URL will be: `https://edupex-backend.up.railway.app`

### Heroku (Alternative Option)

```bash
# Install Heroku CLI
brew tap heroku/brew && brew install heroku

# Login
heroku login

# Create app
cd /Users/mdica/PycharmProjects/EduPex/backend
heroku create edupex-backend

# Set environment variables
heroku config:set SUPABASE_URL=https://szbjppcmhshegyewsveu.supabase.co
heroku config:set SUPABASE_SERVICE_KEY=your_key_here
# ... (set all other env vars)

# Deploy
git subtree push --prefix backend heroku main

# Your URL: https://edupex-backend.herokuapp.com
```

---

## ✅ Verification Checklist

After deployment, verify:

- [ ] Backend URL is accessible (returns "EduPex API is running")
- [ ] HTTPS is working (URL starts with `https://`)
- [ ] Frontend `.env.production` is updated
- [ ] Hardcoded URLs in code are updated
- [ ] Production build completes successfully
- [ ] APK connects to production backend

---

## 🐛 Troubleshooting

### Issue: Deployment fails on Render

**Solution:**
- Check deployment logs in Render dashboard
- Ensure `backend/package.json` has correct `start` script
- Verify all environment variables are set

### Issue: Backend returns 404

**Solution:**
- Check Root Directory is set to `backend`
- Verify Start Command is `npm start`
- Check deployment logs for errors

### Issue: Frontend can't connect to backend

**Solution:**
- Verify CORS is enabled in backend (already configured in `server.js`)
- Check `.env.production` has correct URL
- Ensure URL includes `/api` suffix
- Test backend URL directly in browser

### Issue: "Free instance sleeps after 15 minutes"

**Solution:**
- This is normal for Render's free tier
- First request after sleep takes ~30 seconds
- Consider upgrading to paid tier ($7/month) for always-on service
- Or use a service like UptimeRobot to ping your backend every 10 minutes

---

## 🔒 Security Best Practices

### After Deployment:

1. **Regenerate API Keys** (they're exposed in this guide):
   - Generate new Supabase service key
   - Generate new Groq API key
   - Generate new OpenAI API key
   - Generate new JWT secret: `openssl rand -base64 32`

2. **Update Environment Variables:**
   - Go to Render dashboard → your service → Environment
   - Update each key with new values
   - Click "Save Changes"
   - Service will auto-redeploy

3. **Secure Your GitHub Repository:**
   - Make repository private if public
   - Ensure `.env` files are in `.gitignore`
   - Never commit API keys to Git

---

## 📊 Monitoring & Maintenance

### View Logs:
```bash
# In Render dashboard
# Go to your service → Logs tab
# View real-time logs
```

### Update Backend:
```bash
# Make changes to your code
git add .
git commit -m "Update backend"
git push origin main

# Render will auto-deploy the changes
```

### Check Service Health:
- Render Dashboard → your service → Events
- Shows deployment history and status

---

## 📁 File Locations

After deployment, your files are:

```
/Users/mdica/PycharmProjects/EduPex/
├── backend/
│   ├── .env (local only - NOT committed)
│   ├── deploy-to-render.sh (this helper script)
│   ├── package.json
│   └── server.js
├── frontend/
│   ├── .env.local (development)
│   ├── .env.production (production - UPDATE THIS)
│   └── src/
│       ├── utils/api.js (UPDATE URL here)
│       ├── pages/Login.js (UPDATE URL here)
│       └── components/aiAssistant/AIAssistantButton.js (UPDATE URL here)
└── BACKEND_DEPLOYMENT.md (this file)
```

---

## 🎯 Quick Reference

**Your Deployed Backend URL:**
```
https://YOUR-BACKEND-NAME.onrender.com
```

**API Endpoint for Frontend:**
```
https://YOUR-BACKEND-NAME.onrender.com/api
```

**Files to Update After Deployment:**
1. `frontend/.env.production`
2. `frontend/src/utils/api.js`
3. `frontend/src/pages/Login.js`
4. `frontend/src/components/aiAssistant/AIAssistantButton.js`

---

## 💡 Next Steps

After successful deployment:

1. ✅ Backend deployed to HTTPS
2. ✅ Frontend URLs updated
3. ➡️ Create app signing keystore (see `PLAY_STORE_REQUIREMENTS.md`)
4. ➡️ Build release APK
5. ➡️ Test release build
6. ➡️ Submit to Google Play Store

---

## 📞 Support Resources

- **Render Documentation:** https://render.com/docs
- **Render Status:** https://status.render.com
- **Node.js Deployment Guide:** https://render.com/docs/deploy-node-express-app
- **Environment Variables:** https://render.com/docs/environment-variables

---

**Last Updated:** December 9, 2025
**Guide Location:** `/Users/mdica/PycharmProjects/EduPex/BACKEND_DEPLOYMENT.md`

