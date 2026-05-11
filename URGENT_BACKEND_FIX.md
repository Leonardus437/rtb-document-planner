# 🚨 URGENT FIX - RTB Document Planner Backend

## Problems Identified:
1. ❌ **"Network error: Failed to fetch"** - Missing `/session-plans/` and `/schemes/` endpoints
2. ❌ **"Undefined" profile** - Incomplete user data in login response

## 🔧 Quick Fix Steps:

### Step 1: Update PythonAnywhere Backend
1. **Go to**: https://www.pythonanywhere.com/user/leonardus437/
2. **Login** to your PythonAnywhere account
3. **Open**: Files tab → `/home/leonardus437/mysite/main.py`
4. **Replace ALL content** with: `FIXED_PYTHONANYWHERE_BACKEND.py`
5. **Save** the file
6. **Reload** your web app

### Step 2: Test the Fix
1. **Visit**: https://leonardus437.pythonanywhere.com/
2. **Should show**: `{"message": "RTB Document Planner API", "status": "online", "version": "2.1"}`

### Step 3: Test Document Creation
1. **Go back** to your local app: http://localhost:5173
2. **Login** as a teacher
3. **Try creating** a session plan - should work now!

## 🎯 What the Fix Includes:

### ✅ **Fixed User Profile Data:**
```json
{
  "user_id": "USER_123",
  "name": "Teacher Name",  // ← Now shows correctly
  "phone": "+250...",
  "email": "teacher@school.rw",
  "institution": "School Name",
  "role": "user",
  "is_premium": false
}
```

### ✅ **Added Missing Endpoints:**
- `POST /session-plans/` - Create session plans
- `GET /session-plans/{id}/download` - Download session plans
- `POST /schemes/` - Create schemes of work  
- `GET /schemes/{id}/download` - Download schemes

### ✅ **Fixed Download Tracking:**
- Properly tracks download limits
- Updates user counters
- Handles premium vs free users

## 🚀 After the Fix:
1. **Teachers can login** and see their name (not "undefined")
2. **Document creation works** (no more "Failed to fetch")
3. **Downloads work** with proper file generation
4. **Limits are tracked** correctly

## ⚡ Alternative: Quick Test
If you can't access PythonAnywhere right now, you can test locally:

1. **Copy** `FIXED_PYTHONANYWHERE_BACKEND.py` to `backend/main.py`
2. **Run**: `cd backend && python main.py`
3. **Update** `frontend/config.js` to use `http://localhost:8000`
4. **Test** the system locally

The fix addresses both issues and makes the RTB Document Planner fully functional for TSS Teachers! 🎓