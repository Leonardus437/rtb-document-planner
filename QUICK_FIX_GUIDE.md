# 🚨 QUICK FIX GUIDE - RTB DOCUMENT PLANNER

## PROBLEM: System Not Working in Production

**Backend Status:** ❌ DOWN (Railway deployment not responding)
**Impact:** Users cannot create documents

---

## ⚡ IMMEDIATE FIX (Choose One Option)

### OPTION 1: Fix Railway Deployment (Recommended if you have access)

1. **Login to Railway**
   ```
   Visit: https://railway.app
   Login with your account
   ```

2. **Check Project Status**
   - Find "RTB Document Planner" project
   - Check if service is running
   - Look for deployment errors

3. **Verify Environment Variables**
   - Click on your service
   - Go to "Variables" tab
   - Ensure `DATABASE_URL` is set (PostgreSQL connection string)
   - Add `PORT=8000` if missing

4. **Redeploy**
   - Go to "Deployments" tab
   - Click "Deploy" or "Redeploy"
   - Wait for deployment to complete
   - Copy the new deployment URL

5. **Update Frontend**
   - Edit `frontend/config.js`
   - Update `API_URL` with new Railway URL
   - Commit and push to trigger Cloudflare Pages rebuild

---

### OPTION 2: Deploy to Render (Alternative Platform)

1. **Create Render Account**
   ```
   Visit: https://render.com
   Sign up for free account
   ```

2. **Create PostgreSQL Database**
   - Click "New +" → "PostgreSQL"
   - Name: rtb-planner-db
   - Plan: Free
   - Click "Create Database"
   - Copy "Internal Database URL"

3. **Create Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     * Name: rtb-planner-backend
     * Root Directory: backend
     * Build Command: `pip install -r requirements.txt`
     * Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Environment Variables:
     * `DATABASE_URL` = (paste Internal Database URL)
     * `PYTHON_VERSION` = 3.12.3
   - Click "Create Web Service"

4. **Get Backend URL**
   - Wait for deployment to complete
   - Copy the URL (e.g., https://rtb-planner-backend.onrender.com)

5. **Update Frontend**
   - Edit `frontend/config.js`:
   ```javascript
   const CONFIG = {
       API_URL: 'https://rtb-planner-backend.onrender.com'
   };
   ```
   - Commit and push changes

---

### OPTION 3: Run Locally (For Testing)

1. **Install Dependencies**
   ```bash
   cd /home/leo/Documents/rtb-document-planner-main/backend
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   ```bash
   python init_database.py
   ```

3. **Start Backend**
   ```bash
   uvicorn main:app --reload --port 5000
   ```

4. **Update Frontend Config (Temporary)**
   - Edit `frontend/config.js`:
   ```javascript
   const CONFIG = {
       API_URL: 'http://localhost:5000'
   };
   ```

5. **Start Frontend**
   ```bash
   cd ../frontend
   python -m http.server 5173
   ```

6. **Access System**
   ```
   Open browser: http://localhost:5173
   ```

---

## 🔍 VERIFICATION STEPS

After fixing, verify these work:

1. **Backend Health Check**
   ```bash
   curl https://YOUR-BACKEND-URL/health
   ```
   Should return: `{"status":"healthy","database":"connected",...}`

2. **User Registration**
   - Go to frontend
   - Click "Register"
   - Create test account
   - Should succeed

3. **User Login**
   - Login with test account
   - Should redirect to dashboard

4. **Document Generation**
   - Click "Session Plan"
   - Fill form
   - Click "Generate"
   - Should download DOCX file

5. **Admin Access**
   - Logout
   - Login as admin:
     * Phone: +250789751597
     * Password: admin123
   - Should see admin dashboard

---

## 📝 CURRENT CONFIGURATION

**Frontend (Cloudflare Pages):**
- URL: https://rtb-planner.pages.dev
- Config: `frontend/config.js`
- Current Backend: https://web-production-df3e5.up.railway.app (NOT WORKING)

**Backend (Railway - DOWN):**
- URL: https://web-production-df3e5.up.railway.app
- Status: 404 Application not found
- Database: PostgreSQL (should be configured in Railway)

---

## 🆘 TROUBLESHOOTING

### Issue: "Cannot connect to backend"
**Solution:** 
- Check backend URL in `frontend/config.js`
- Verify backend is running (curl health endpoint)
- Check CORS settings in `backend/main.py`

### Issue: "Database connection failed"
**Solution:**
- Verify DATABASE_URL environment variable
- Check PostgreSQL database is running
- For local: ensure SQLite is being used (no DATABASE_URL set)

### Issue: "Dependencies not found"
**Solution:**
```bash
cd backend
pip install --upgrade pip
pip install -r requirements.txt
```

### Issue: "Port already in use"
**Solution:**
```bash
# Find process using port
lsof -i :5000
# Kill process
kill -9 <PID>
# Or use different port
uvicorn main:app --reload --port 5001
```

---

## 📞 NEED HELP?

**System Developer:** Trainer Leon
**Admin Phone:** +250789751597

**Quick Commands:**
```bash
# Check if backend is running
curl https://YOUR-BACKEND-URL/health

# Check Python version
python3 --version

# Check installed packages
pip list | grep -E "fastapi|sqlalchemy|uvicorn"

# View backend logs (if running locally)
tail -f backend/logs/*.log
```

---

## ✅ SUCCESS CHECKLIST

- [ ] Backend is accessible (health check returns 200)
- [ ] Frontend loads without errors
- [ ] User can register
- [ ] User can login
- [ ] Session plan generates successfully
- [ ] Scheme of work generates successfully
- [ ] Assessment plan generates successfully
- [ ] Trainer report generates successfully
- [ ] Admin can login
- [ ] Admin dashboard shows statistics
- [ ] Documents are RTB-compliant (check formatting)

---

**Once fixed, the system should work perfectly - the code is excellent!**

*Last Updated: $(date)*
