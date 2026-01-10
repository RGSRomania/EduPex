# Google Play Store Requirements Checklist for EduPex

## ✅ COMPLETED (Fixed by automation)

### Security & Configuration
- [x] **Disabled cleartext HTTP traffic** - App now requires HTTPS
- [x] **Updated network security config** - Production-ready security settings
- [x] **Configured release build** - Code minification and optimization enabled
- [x] **Added ProGuard rules** - Proper obfuscation for Capacitor/WebView apps

## 🔴 CRITICAL - MUST DO BEFORE PUBLISHING

### 1. Backend HTTPS Migration
**Status:** ❌ BLOCKING
**Current:** App uses `http://10.0.2.2:5000/api` (development only)
**Required:** Deploy backend to HTTPS server

**Actions needed:**
- Deploy backend to a cloud service with HTTPS (Render, Railway, Heroku, AWS, etc.)
- Update API_BASE_URL in production build to use HTTPS endpoint
- Example: `https://your-backend.onrender.com/api`

### 2. Create App Signing Key
**Status:** ❌ BLOCKING
**Required:** Sign release APK with your keystore

**Commands to create keystore:**
```bash
cd frontend/android/app
keytool -genkey -v -keystore edupex-release-key.keystore \
  -alias edupex-key -keyalg RSA -keysize 2048 -validity 10000

# Create keystore.properties file
cat > ../keystore.properties << EOF
RELEASE_STORE_FILE=app/edupex-release-key.keystore
RELEASE_STORE_PASSWORD=YOUR_STRONG_PASSWORD
RELEASE_KEY_ALIAS=edupex-key
RELEASE_KEY_PASSWORD=YOUR_STRONG_PASSWORD
EOF
```

⚠️ **IMPORTANT:** 
- Keep keystore file safe - if lost, you can NEVER update your app
- Add `keystore.properties` to `.gitignore`
- Store backup of keystore in secure location

### 3. Update API URLs for Production
**Status:** ❌ BLOCKING

**Files to update:**
- `frontend/src/utils/api.js` - Change default API URL
- `frontend/src/pages/Login.js` - Update API endpoint
- `frontend/src/components/aiAssistant/AIAssistantButton.js` - Update API endpoint

**Example change:**
```javascript
const API_BASE_URL = process.env.REACT_APP_API_URL || 'https://your-backend.onrender.com/api';
```

### 4. Create Privacy Policy
**Status:** ❌ REQUIRED
**Why:** Your app collects user data (email, progress, etc.)

**What to include:**
- What data you collect (email, name, progress, quiz results)
- How you use the data (educational purposes, progress tracking)
- Data storage and security measures
- User rights (deletion, access)
- Contact information

**Where to host:**
- Create a simple webpage or use Google Sites
- URL will be required during Play Console submission

### 5. Create App Icons
**Status:** ⚠️ USING DEFAULT ICONS
**Current:** Using Capacitor default icons

**Actions needed:**
```bash
# Create icons in these sizes:
# 512x512 - Play Store listing
# 1024x1024 - Feature graphic
# Various sizes for adaptive icons

# Use Capacitor's asset generator:
npx @capacitor/assets generate --iconBackgroundColor '#your-color'
```

### 6. Create Screenshots & Store Listing
**Status:** ❌ REQUIRED

**Required assets:**
- Screenshots (at least 2, max 8) for phone and tablet
- Feature graphic (1024 x 500)
- App icon (512 x 512)
- Short description (80 chars max)
- Full description (4000 chars max)

### 7. Set Up Google Play Console
**Status:** ❌ REQUIRED

**Steps:**
1. Create Google Play Developer account ($25 one-time fee)
2. Set up app in Play Console
3. Complete content rating questionnaire
4. Add privacy policy URL
5. Set up pricing & distribution

## ⚠️ IMPORTANT - RECOMMENDED

### 8. Version Code Management
**Current:** versionCode = 1, versionName = "1.0"
**Status:** ✅ OK for initial release

**For future updates:**
- Increment versionCode for each release (2, 3, 4...)
- Update versionName semantically (1.1, 1.2, 2.0)

### 9. Test Release Build
**Status:** ⚠️ NOT TESTED

**Commands to build and test:**
```bash
cd frontend
npm run build
npx cap sync android
cd android

# Build release APK (after keystore is set up)
./gradlew assembleRelease

# Test the release build
adb install app/build/outputs/apk/release/app-release.apk
```

### 10. Content Rating
**Status:** ❌ REQUIRED

**During Play Console setup:**
- Complete content rating questionnaire
- Your app is educational for children
- May receive PEGI 3, ESRB Everyone rating

### 11. Target Audience
**Status:** ⚠️ NEEDS DECISION

**Questions to answer:**
- Age range: Elementary school (6-12 years)?
- Are you complying with COPPA (Children's Online Privacy Protection Act)?
- Do you have parental controls?

### 12. Add Data Safety Form
**Status:** ❌ REQUIRED (New Google Play requirement)

**Data you collect:**
- Account info (email, name)
- App activity (progress, quiz results)
- You likely DON'T collect location, contacts, etc.

**Purpose:**
- App functionality
- Personalization
- Analytics (if you add Firebase/Analytics)

## 📋 PRE-LAUNCH CHECKLIST

Before submitting to Play Store:

- [ ] Backend deployed to HTTPS production server
- [ ] All API URLs updated to production HTTPS endpoints
- [ ] Keystore created and secured
- [ ] Release APK built and signed
- [ ] Release build tested on physical device
- [ ] Privacy policy created and hosted
- [ ] App icons created (all sizes)
- [ ] Screenshots captured (phone & tablet)
- [ ] Store listing prepared (descriptions, graphics)
- [ ] Google Play Developer account created
- [ ] Content rating completed
- [ ] Data safety form completed
- [ ] Target audience defined
- [ ] Pricing set (free or paid)
- [ ] Distribution countries selected
- [ ] App tested for crashes and critical bugs

## 🚀 BUILD COMMANDS

### Development Build (with HTTP for local testing)
```bash
# Revert to HTTP for development
# Update capacitor.config.ts: androidScheme: 'http', cleartext: true
cd frontend
npm run build
npx cap sync android
cd android
./gradlew assembleDebug
```

### Production Build (HTTPS only)
```bash
# Ensure all configs are set for HTTPS
cd frontend
REACT_APP_API_URL=https://your-backend.com/api npm run build
npx cap sync android
cd android
./gradlew assembleRelease  # Requires keystore setup

# Output: android/app/build/outputs/apk/release/app-release.apk
```

## 📞 SUPPORT

If you need help:
1. Google Play Console Help: https://support.google.com/googleplay/android-developer
2. Capacitor Docs: https://capacitorjs.com/docs
3. Android Publishing: https://developer.android.com/studio/publish

## 🔒 SECURITY REMINDERS

1. **Never commit:**
   - keystore.properties
   - *.keystore files
   - API keys or secrets

2. **Always use:**
   - Environment variables for production URLs
   - HTTPS for all network traffic
   - Secure password storage
   - Latest security patches

3. **Backup:**
   - Your keystore file (critical!)
   - Database credentials
   - App signing keys

## 📊 ESTIMATED TIMELINE

- Backend deployment: 1-2 days
- Create signing keys & icons: 1 day
- Privacy policy & store listing: 2-3 days
- Testing release build: 1-2 days
- Play Console setup: 1 day
- Google review process: 3-7 days

**Total: ~2 weeks** (first submission)

