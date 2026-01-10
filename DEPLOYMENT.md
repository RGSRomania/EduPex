# EduPex Deployment Guide

## Step 1: Deploy Backend to Render (Free)

### 1.1 Create a Render Account
1. Go to https://render.com
2. Sign up with your GitHub account (recommended) or email

### 1.2 Deploy from GitHub
1. Push your code to GitHub if you haven't already:
   ```bash
   cd /Users/mdica/PycharmProjects/EduPex
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. In Render Dashboard:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Select the `EduPex` repository
   - Configure the service:
     - **Name**: edupex-backend
     - **Root Directory**: backend
     - **Environment**: Node
     - **Build Command**: `npm install`
     - **Start Command**: `npm start`
     - **Plan**: Free

3. Add Environment Variables in Render:
   - `NODE_ENV` = `production`
   - `SUPABASE_URL` = `https://your-project.supabase.co`
   - `SUPABASE_SERVICE_KEY` = `your_supabase_service_key_here`
   - `LLM_PROVIDER` = `groq`
   - `GROQ_API_KEY` = `your_groq_api_key_here`
   - `JWT_SECRET` = `your_jwt_secret_here`
   - `MONGODB_URI` = `your_mongodb_connection_string` (optional)

4. Click "Create Web Service"
   - Render will build and deploy your backend
   - You'll get a URL like: `https://edupex-backend.onrender.com`

### 1.3 Alternative: Deploy to Railway (Also Free)
1. Go to https://railway.app
2. Sign up with GitHub
3. Click "New Project" → "Deploy from GitHub repo"
4. Select your repository
5. Add the same environment variables as above
6. Deploy!

---

## Step 2: Update Frontend for Production

### 2.1 Create Environment Files

Create `.env.production` in `/Users/mdica/PycharmProjects/EduPex/frontend/`:
```
REACT_APP_API_URL=https://your-backend-url.onrender.com/api
```

Create `.env.local` for local development:
```
REACT_APP_API_URL=http://localhost:5000/api
```

### 2.2 Build APK with Production Backend

```bash
# Navigate to frontend directory
cd /Users/mdica/PycharmProjects/EduPex/frontend

# Create production environment file
echo "REACT_APP_API_URL=https://edupex-backend.onrender.com/api" > .env.production

# Build React app with production settings
REACT_APP_API_URL=https://edupex-backend.onrender.com/api npm run build

# Sync to Android
npx cap sync android

# Build APK with Java 21
cd android
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
./gradlew assembleRelease
```

The production APK will be at:
`/Users/mdica/PycharmProjects/EduPex/frontend/android/app/build/outputs/apk/release/app-release.apk`

---

## Step 3: Quick Deploy Script

Save this as `deploy.sh` in your project root:

```bash
#!/bin/bash

# Deploy Backend (if using Render CLI)
cd backend
git push

# Build and deploy Android APK
cd ../frontend

# Ask for backend URL
read -p "Enter your backend URL (e.g., https://edupex-backend.onrender.com): " BACKEND_URL

# Build with production URL
REACT_APP_API_URL=$BACKEND_URL/api npm run build
npx cap sync android

# Build APK
cd android
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
./gradlew assembleRelease

echo "✅ APK built successfully!"
echo "📱 Location: android/app/build/outputs/apk/release/app-release.apk"
```

Make it executable:
```bash
chmod +x deploy.sh
```

---

## Step 4: Test Your Deployed Backend

After deployment, test your backend:

```bash
# Replace with your actual Render URL
curl https://edupex-backend.onrender.com/api/assistant/ask \
  -H "Content-Type: application/json" \
  -d '{"question":"Ce este teorema lui Pitagora?","subject":"mate","grade":"5"}'
```

---

## Quick Command Reference

### Build for Local Testing (with local backend)
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm run build
npx cap sync android
cd android
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
./gradlew assembleDebug
```

### Build for Production (with deployed backend)
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
REACT_APP_API_URL=https://YOUR-BACKEND-URL.onrender.com/api npm run build
npx cap sync android
cd android
export JAVA_HOME=/opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home
./gradlew assembleRelease
```

---

## Troubleshooting

### Backend won't start on Render
- Check the logs in Render Dashboard
- Ensure all environment variables are set
- Verify MongoDB connection (if using)

### APK can't connect to backend
- Check the backend URL is correct (include `/api` at the end)
- Ensure backend is running (visit the URL in a browser)
- Check Android app logs: `adb logcat | grep EduPex`

### CORS errors
The backend is already configured with CORS enabled, but if you get errors:
- Ensure your backend URL is correct
- Check Render logs for CORS-related errors

---

## Production Checklist

- [ ] Backend deployed to Render/Railway
- [ ] All environment variables configured
- [ ] Backend URL tested and working
- [ ] Frontend `.env.production` created with backend URL
- [ ] APK built with production backend URL
- [ ] APK tested on a real device
- [ ] Backend stays awake (Render free tier sleeps after 15 min of inactivity)

---

## Notes

**Free Tier Limitations:**
- Render free tier: Backend sleeps after 15 minutes of inactivity (first request takes 30-60 seconds to wake up)
- Railway: 500 hours/month free tier
- Consider upgrading to paid tier for production use

**Backend URL:** Once deployed, your backend will be accessible at:
- Render: `https://edupex-backend.onrender.com`
- Railway: `https://edupex-backend.railway.app`

Update this URL in your frontend `.env.production` file!

