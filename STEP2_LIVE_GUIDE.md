# 📋 STEP 2 - Render Deployment (LIVE WALKTHROUGH)

## What You're Looking At

You're on the Render.com service selection page. You need to click **"Web Services"** because your backend is a Node.js web server.

---

## STEP 2A: Select Web Service

**Click**: "Web Services" → "New Web Service"

---

## STEP 2B: Connect Your GitHub Repository

When the next page loads:

1. Search for: `edupex-backend`
2. Click to select it
3. Click "Connect"

---

## STEP 2C: Configure Your Service

Fill in these exact values:

| Field | Value |
|-------|-------|
| **Name** | `edupex-backend` |
| **Environment** | `Node` |
| **Region** | `Oregon (US West)` |
| **Branch** | `main` |
| **Build Command** | `npm install` |
| **Start Command** | `npm start` |
| **Instance Type** | `Free` |

---

## STEP 2D: Add Environment Variables

You'll see a section "Environment Variables". Click "Add Environment Variable" for each:

### Variable 1:
- **Key**: `MONGODB_URI`
- **Value**: `mongodb://localhost:27017/edupex`

### Variable 2:
- **Key**: `JWT_SECRET`
- **Value**: `edupex_super_secret_key_2026_change_this_in_production`

### Variable 3:
- **Key**: `NODE_ENV`
- **Value**: `production`

### Variable 4:
- **Key**: `PORT`
- **Value**: `5000`

---

## STEP 2E: Create Web Service

Click the blue **"Create Web Service"** button.

---

## STEP 2F: Wait for Deployment

You'll see build logs scrolling. **Wait** for it to show:

```
✓ Build succeeded
Service is live at: https://edupex-backend-xxxxx.onrender.com
```

This takes **3-5 minutes**.

When you see this message, move to **STEP 3**.

---

## STEP 3: Copy Your Backend URL

The URL will look like:
```
https://edupex-backend-xxxxx.onrender.com
```

**Copy the entire URL** (including https://)

---

## STEP 4: Update APK Configuration

Once you have the URL, edit:
`/Users/mdica/PycharmProjects/EduPex/frontend/src/config/apiConfig.js`

Change line 16 from:
```javascript
return 'https://edupex-backend.onrender.com/api';
```

To your actual URL:
```javascript
return 'https://edupex-backend-xxxxx.onrender.com/api';
```

---

## STEP 5: Build APK

```bash
cd /Users/mdica/PycharmProjects/EduPex
./build-apk-fixed.sh
```

---

## You're On It! 🚀

You've already connected GitHub. Now:

1. **Select "Web Services"** on the page you're looking at
2. **Follow the configuration steps above**
3. **Wait for "Live" status** (3-5 minutes)
4. **Tell me the backend URL** when it shows

Then I'll help you with Step 4 & 5.

---

**What to do RIGHT NOW**: Click "Web Services"

