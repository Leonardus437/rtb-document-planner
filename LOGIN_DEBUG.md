# 🔍 LOGIN DEBUG INSTRUCTIONS

## Issue
Login shows "Invalid credentials" even with correct phone/password.

## What I Did
1. ✅ Created test user: +250789751558 / test123
2. ✅ Tested backend directly - **WORKS!**
3. ✅ Added debug logging to login.html
4. ✅ Created test page

## Test Now

### Step 1: Test Backend Directly
```bash
curl -X POST http://localhost:5000/users/login -H "Content-Type: application/json" -d "{\"phone\":\"+250789751558\",\"password\":\"test123\"}"
```
Should return user data ✅

### Step 2: Test Simple Page
1. Go to: http://localhost:5173/test-login-simple.html
2. Click "Test Login" button
3. Check result

### Step 3: Test Real Login with Console
1. Go to: http://localhost:5173/login.html?type=teacher
2. Open browser console (F12)
3. Enter: +250789751558 / test123
4. Click "Sign In"
5. Check console logs

## What to Look For

### In Console:
```
Login attempt: +250789751558
API URL: http://localhost:5000
Fetching: http://localhost:5000/users/login
Response status: 200 or 401
Response body: {...}
```

### Possible Issues:
1. **CORS Error** - Backend not allowing frontend
2. **Wrong API URL** - Check config.js
3. **Cache Issue** - Hard refresh (Ctrl+Shift+R)
4. **Backend not running** - Check port 5000

## Quick Fixes

### Fix 1: Hard Refresh
Press **Ctrl + Shift + R** to clear cache

### Fix 2: Check Backend
```bash
# Should show backend running
netstat -ano | findstr :5000
```

### Fix 3: Restart System
```bash
# Stop everything
taskkill /F /IM python.exe

# Start fresh
start_rtb_system.bat
```

## Test Credentials

### Teacher
- Phone: **+250789751558**
- Password: **test123**

### Admin
- Phone: **+250789751597**
- Password: **admin123**

## Next Steps
1. Run test-login-simple.html
2. Check browser console
3. Report what you see
