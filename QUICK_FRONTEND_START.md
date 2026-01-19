# 🚀 START FRONTEND WITH CLOUD BACKEND

## Two Scenarios

### Scenario A: You Have a Cloud Backend URL

If your backend is deployed (e.g., on Render, Railway, Heroku), use:

```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
REACT_APP_API_URL=https://your-backend-url.com npm start
```

**Example with Render:**
```bash
REACT_APP_API_URL=https://edupex-backend.onrender.com npm start
```

### Scenario B: Run Backend Locally + Frontend

If you want to run the backend locally on your laptop first:

**Terminal 1 - Start Backend:**
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
npm start
```

**Terminal 2 - Start Frontend:**
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm start
```

The frontend will automatically use the proxy: `http://localhost:5000`

---

## Which One?

**Option A (Cloud Backend):**
- ✅ Fast testing
- ✅ No local backend needed
- ✅ Uses existing cloud setup
- ❌ Need to know the URL

**Option B (Local Backend):**
- ✅ Full control
- ✅ Easier debugging
- ✅ No external dependencies
- ⚠️ Need to run 2 processes

---

## Tell Me

**Do you have a cloud backend URL** (deployed somewhere)?

If yes: What is it?
If no: Should I start the backend locally first?

Then I'll start your frontend! 🎯


