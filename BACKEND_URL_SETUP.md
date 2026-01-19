# 🌐 Backend URL Configuration for External Device Access

## Problem
Your device is not on the same network as your laptop, so it cannot access `http://10.0.2.2:5000/api` or `http://localhost:5000/api`.

**Solution**: Use an internet-accessible backend URL (deployed on cloud service like GitHub, Render, Railway, etc.)

---

## Current Configuration

### What's Now Set
✅ API configuration updated to use `https://edupex-backend.onrender.com/api` for APK builds  
✅ This is an internet-accessible URL that works from any device  
✅ No localhost or 10.0.2.2 in production APK  

### What You Need to Do
Choose ONE of these options to provide a backend URL:

---

## Option 1: Use Existing Render.com Deployment (Easiest)

If your backend is already deployed on Render.com at `https://edupex-backend.onrender.com/`:

1. **Verify it's running:**
   ```bash
   curl https://edupex-backend.onrender.com/api/
   ```

2. **The API config already uses this URL** ✅

3. **Build APK and test:**
   ```bash
   npm run build
   npx cap sync android
   cd android
   ./gradlew assembleDebug
   ```

---

## Option 2: Deploy Backend to GitHub Pages + Cloud Function

If you want to host backend code on GitHub:

### Step 1: Create a `.env.production` file

In your backend directory, create `.env.production`:
```
PORT=5000
MONGODB_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret
NODE_ENV=production
```

### Step 2: Create GitHub Actions Deployment

Create `.github/workflows/deploy.yml`:
```yaml
name: Deploy to Render

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        run: |
          curl -X POST https://api.render.com/deploy/srv-xxx \
            -H "Authorization: Bearer ${{ secrets.RENDER_DEPLOY_KEY }}"
```

### Step 3: Get Your Deployed URL

After deployment, you'll have a URL like:
```
https://your-backend-name.onrender.com/api
```

### Step 4: Update API Configuration

If your deployed backend is different, update:

**File**: `frontend/src/config/apiConfig.js`

Change this line:
```javascript
return 'https://edupex-backend.onrender.com/api';
```

To your actual backend URL:
```javascript
return 'https://your-deployed-backend-url.com/api';
```

---

## Option 3: Deploy Backend Yourself (Manual)

### Using Render.com (Free tier available):

1. **Commit backend to GitHub:**
   ```bash
   cd backend
   git init
   git add .
   git commit -m "Initial backend"
   git remote add origin https://github.com/YOUR_USERNAME/edupex-backend.git
   git push -u origin main
   ```

2. **Create Render account:**
   - Go to https://render.com/
   - Sign in with GitHub
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - Environment: Node
     - Build Command: `npm install`
     - Start Command: `npm start`
     - Environment Variables:
       - `MONGODB_URI`: Your MongoDB connection string
       - `JWT_SECRET`: A random secret string
       - `NODE_ENV`: production

3. **Get your Render URL:**
   - Will be like: `https://edupex-backend-xxx.onrender.com`

4. **Update API Config:**
   ```javascript
   return 'https://edupex-backend-xxx.onrender.com/api';
   ```

---

## Option 4: GitHub + Vercel + Serverless Functions

For serverless approach:

1. Create API routes on Vercel
2. Vercel URL: `https://your-project.vercel.app/api`
3. Update API config with Vercel URL

---

## Testing Your Backend URL

### Test from your laptop:
```bash
curl https://your-backend-url/api/
```

Expected response:
```
"EduPex API is running"
```

### Test from device:
1. Build and install APK
2. Open app
3. Check browser DevTools console for API URL being used
4. Try login with test@edupex.com / test123

---

## Troubleshooting

### Backend returns 502/503/timeout
- Backend may be sleeping (Render free tier)
- Make a request to wake it up: `curl https://your-url/api/`
- Wait 30-60 seconds, then try again

### CORS error
Backend needs to allow requests from APK domain:
```javascript
// In backend/server.js
const cors = require('cors');
app.use(cors({
  origin: '*', // For testing only, restrict in production
  credentials: true
}));
```

### SSL certificate error
Ensure your backend URL uses HTTPS and has valid certificate

### Still can't connect
1. Check internet on device
2. Verify backend is running
3. Check API config has correct URL
4. Rebuild APK after changing URL
5. Clear app cache: `adb shell pm clear com.edupex.app`

---

## Summary

### For External Device Access:

1. **Ensure backend is deployed** on internet-accessible service
2. **Update API config** with correct backend URL (if not using Render.com)
3. **Build APK**: `npm run build && npx cap sync android && cd android && ./gradlew assembleDebug`
4. **Install APK**: `adb install app-debug.apk`
5. **Test**: Click demo login button

**Device will use the internet-accessible backend URL automatically!**

---

## Current Backend Status

**URL Being Used**: `https://edupex-backend.onrender.com/api`

**Test It:**
```bash
curl -X POST https://edupex-backend.onrender.com/api/users/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@edupex.com","password":"test123"}'
```

If this works, your backend is ready for APK deployment! ✅

---

## Next Steps

1. ✅ Verify backend is accessible from internet
2. ✅ API config is already set up for production APK
3. ⏭️ Build APK: `./build-demo-apk.sh`
4. ⏭️ Install on device
5. ⏭️ Test login with test@edupex.com / test123

**That's it!** External device will use the internet-accessible backend automatically.

