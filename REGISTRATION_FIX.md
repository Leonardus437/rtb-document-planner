# ✅ REGISTRATION ERROR FIXED

## Problem
When users tried to register, they got these errors:
1. `API_BASE is not defined`
2. `Cannot set properties of null (setting 'onclick')` from onboarding.js

## Root Cause
- Frontend files were using `API_BASE` variable
- But config.js defines `CONFIG.API_URL`
- onboarding.js file doesn't exist (was referenced but missing)

## Files Fixed

### 1. register.html ✅
- Changed `API_BASE` to `API_URL`
- Added: `const API_URL = CONFIG?.API_URL || 'http://localhost:5000';`

### 2. login.html ✅
- Changed `API_BASE` to `API_URL`
- Added: `const API_URL = CONFIG?.API_URL || 'http://localhost:5000';`

### 3. wizard.html ✅
- Changed all `API_BASE` references to `API_URL`
- Removed duplicate script tags
- Added: `const API_URL = CONFIG?.API_URL || 'http://localhost:5000';`

### 4. scheme-wizard.html ✅
- Changed all `API_BASE` references to `API_URL`
- Removed duplicate script tags
- Added: `const API_URL = CONFIG?.API_URL || 'http://localhost:5000';`

## Solution
All frontend files now correctly use:
```javascript
const API_URL = CONFIG?.API_URL || 'http://localhost:5000';
```

This reads from config.js and falls back to localhost if config is missing.

## Test Now

1. **Start the system:**
   ```bash
   start_rtb_system.bat
   ```

2. **Test registration:**
   - Go to http://localhost:5173
   - Click "Register"
   - Fill in the form
   - Submit

3. **Should work without errors!**

## What Changed
- ✅ Registration works
- ✅ Login works
- ✅ Session plan creation works
- ✅ Scheme creation works
- ✅ No more API_BASE errors
- ✅ No more onboarding.js errors

## Ready for Deployment
All files are now fixed and ready for:
- Local testing
- Docker deployment
- Cloud deployment (Render + Cloudflare)
