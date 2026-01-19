# 🌐 FRONTEND + CLOUD BACKEND SETUP

## Your Setup
- **Frontend:** Running on your laptop (localhost:3000)
- **Backend:** Running in the cloud (MongoDB Atlas + Express)
- **No .env changes needed** ✅

## Option 1: Use Cloud Backend URL via Command Line (RECOMMENDED)

Start frontend with cloud backend URL:

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
REACT_APP_API_URL=https://your-backend-url.com npm start
```

Replace `https://your-backend-url.com` with your actual cloud backend URL.

**What is your cloud backend URL?**
- If using Render: `https://your-app-name.onrender.com`
- If using Railway: `https://your-app.railway.app`
- If using Heroku: `https://your-app-name.herokuapp.com`

---

## Option 2: Start Frontend with Local Proxy

If your backend is running locally (port 5000), just run:

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm start
```

The proxy in package.json will automatically forward API calls to `http://localhost:5000`.

---

## Option 3: Override .env.local at Runtime (No File Changes)

Export the API URL before starting:

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
export REACT_APP_API_URL=https://your-cloud-backend-url
npm start
```

---

## How the Frontend Finds Your Backend

The frontend makes API calls like this:

```javascript
const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:5000/api';

// Then makes requests to:
fetch(`${API_URL}/lessons/materii`)
```

So it checks for the environment variable first, then falls back to localhost.

---

## Current Backend Status

✅ **Import successful:** 114 lessons in MongoDB
✅ **Backend code:** Fixed (authenticate middleware)
✅ **Ready to serve:** All API endpoints ready

---

## What You Need

Tell me:

1. **Is your backend running in the cloud?** (Render, Railway, Heroku, etc.)
2. **What's your cloud backend URL?**
3. **Or do you want to run backend locally on port 5000?**

Then I'll tell you the exact command to start your frontend!

---

## Quick Test

To verify your cloud backend is accessible, run:

```bash
curl https://your-cloud-backend-url/api/lessons/materii
```

You should get JSON with your 2 subjects back.

---

**What's your backend URL?** 🚀

