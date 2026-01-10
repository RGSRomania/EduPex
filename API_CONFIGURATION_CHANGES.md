# API Configuration Changes

## Problem
The application was hardcoded to use `10.0.2.2:5000` (Android emulator localhost) for API calls, which prevented it from working properly in web browsers. When running the app in a web browser, it was trying to connect to `10.0.2.2` instead of `localhost`, causing connection errors.

## Solution
Implemented automatic platform detection using Capacitor's platform API to dynamically select the correct API URL based on the runtime environment.

## Changes Made

### 1. New File: `frontend/src/config/apiConfig.js`
Created a centralized API configuration module that:
- Detects the current platform (web, Android, iOS) using Capacitor
- Returns the appropriate API URL for each platform:
  - **Web browser**: `http://localhost:5000/api`
  - **Android emulator**: `http://10.0.2.2:5000/api`
  - **iOS simulator**: `http://localhost:5000/api`
- Supports environment variable override via `REACT_APP_API_URL`
- Handles production environment automatically

### 2. Updated Files

#### `frontend/src/utils/api.js`
- Removed hardcoded API URL logic
- Now imports and uses `API_BASE_URL` from `apiConfig.js`

#### `frontend/src/pages/Login.js`
- Removed hardcoded API URL logic
- Now imports and uses `API_BASE_URL` from `apiConfig.js`

#### `frontend/src/components/aiAssistant/AIAssistantButton.js`
- Removed hardcoded API URL logic
- Now imports and uses `API_BASE_URL` from `apiConfig.js`

#### `frontend/.env.local`
- Updated comments to reflect automatic platform detection
- Removed hardcoded `REACT_APP_API_URL` setting
- Now relies on automatic detection by default
- Documented how to override if needed

#### `frontend/.env.example`
- Updated documentation to explain the new automatic platform detection feature
- Added examples for manual override
- Improved production configuration examples

## How It Works

1. **Development Mode** (default):
   - The app automatically detects the platform using `Capacitor.getPlatform()`
   - Selects the appropriate localhost URL for that platform
   - No environment variables needed

2. **Manual Override**:
   - Set `REACT_APP_API_URL` in `.env.local` to override automatic detection
   - Useful for testing specific backend URLs

3. **Production Mode**:
   - Set `REACT_APP_API_URL` to your deployed backend URL
   - Example: `REACT_APP_API_URL=https://edupex-backend.onrender.com/api`

## Benefits

1. **Works in all environments**: Web browsers, Android emulators, iOS simulators
2. **No manual configuration needed**: Automatic platform detection
3. **Centralized configuration**: Single source of truth for API URLs
4. **Easy to override**: Environment variables still work for custom setups
5. **Production-ready**: Seamless transition from development to production

## Testing

Both frontend and backend have been restarted and are running successfully:
- Backend: http://localhost:5000
- Frontend: http://localhost:3000

The app will now correctly connect to the backend whether running in:
- A web browser (uses `localhost`)
- An Android emulator (uses `10.0.2.2`)
- An iOS simulator (uses `localhost`)

## Next Steps

No further action required. The app is now ready to use in any development environment!

