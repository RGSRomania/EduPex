# Backend Server Connection - RESOLVED ✅

## Problem
The frontend was receiving `ERR_CONNECTION_REFUSED` errors when trying to connect to the login API:
```
POST http://localhost:5000/api/users/login net::ERR_CONNECTION_REFUSED
Login error: TypeError: Failed to fetch
```

## Root Cause
The backend server on port 5000 was not running.

## Solution Applied

### 1. **Started Backend Server**
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
npm start
```
- Backend is now running on **http://localhost:5000**
- Server successfully connected to MongoDB
- API health check endpoint is responding correctly

### 2. **Started Frontend Development Server**
```bash
cd /Users/mdica/PycharmProjects/EduPex/frontend
npm start
```
- Frontend is now running on **http://localhost:3000**
- Can access the app in your browser at http://localhost:3000

### 3. **Created Demo User Credentials**
```bash
cd /Users/mdica/PycharmProjects/EduPex/backend
node createDemoUser.js
```
Demo login credentials:
- **Email:** test@edupex.com
- **Password:** test123
- **Grade Level:** 5

### 4. **Verified API Connection**
Login API endpoint test successful:
```
POST http://localhost:5000/api/users/login
Response: Login successful with JWT token ✅
```

## Current Status

### Running Services
- ✅ **Backend API** - Port 5000 (Node.js/Express)
- ✅ **Frontend** - Port 3000 (React Development Server)
- ✅ **MongoDB** - Atlas connection active

### Testing
- ✅ Health check endpoint: `http://localhost:5000/api/health`
- ✅ Login endpoint working with demo credentials
- ✅ JWT token generation functioning correctly

## What To Do Next

### 1. **Open the Application**
Go to: **http://localhost:3000** in your browser

### 2. **Login with Demo Account**
- Email: `test@edupex.com`
- Password: `test123`

### 3. **Development Workflow**
- Keep both servers running in terminal windows
- Frontend changes auto-reload (React hot module reloading)
- Backend changes require manual restart (restart `npm start` in backend folder)

### 4. **To Stop the Servers**
- Press **Ctrl+C** in each terminal window running the servers

## Important Notes

1. **Environment Files**
   - Backend: `/backend/.env` - Contains API keys, MongoDB URI, JWT secret
   - Frontend: `/frontend/.env.local` - Contains configuration for API URL detection

2. **Database**
   - Using MongoDB Atlas (cloud hosted)
   - IP whitelisting must be configured in MongoDB Atlas settings

3. **API Configuration**
   - Frontend automatically detects correct API URL based on platform:
     - Web browser: `http://localhost:5000/api`
     - Android emulator: `http://10.0.2.2:5000/api`
     - iOS simulator: `http://localhost:5000/api`

## Troubleshooting

If you encounter issues:

1. **Port Already in Use**
   ```bash
   # Find what's using port 5000
   lsof -i :5000
   # Find what's using port 3000
   lsof -i :3000
   ```

2. **Dependencies Not Installed**
   ```bash
   # For backend
   cd backend && npm install
   # For frontend
   cd frontend && npm install
   ```

3. **MongoDB Connection Error**
   - Check `.env` file has valid MONGODB_URI
   - Verify your IP is whitelisted in MongoDB Atlas

4. **Clear Browser Cache**
   - Open DevTools (F12) → Right-click refresh button → "Empty cache and hard refresh"

---

**Status:** All systems operational ✅
**Last Updated:** January 19, 2026

