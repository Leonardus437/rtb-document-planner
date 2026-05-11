# 🚂 RAILWAY DEPLOYMENT GUIDE - RTB DOCUMENT PLANNER

## 📋 COMPLETE STEP-BY-STEP DEPLOYMENT

---

## STEP 1: PREPARE YOUR PROJECT

### ✅ Files Already Created:
- ✓ `railway.json` - Railway configuration
- ✓ `nixpacks.toml` - Build configuration
- ✓ `Procfile` - Start command
- ✓ `backend/requirements.txt` - Dependencies
- ✓ All backend code ready

### Check Git Status:
```bash
cd /home/leo/Documents/rtb-document-planner-main
git status
```

---

## STEP 2: PUSH TO GITHUB (If Not Already Done)

### Option A: If Repository Exists
```bash
cd /home/leo/Documents/rtb-document-planner-main

# Add all files
git add .

# Commit changes
git commit -m "Prepare for Railway deployment"

# Push to GitHub
git push origin main
```

### Option B: If New Repository
```bash
cd /home/leo/Documents/rtb-document-planner-main

# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - RTB Document Planner"

# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR-USERNAME/rtb-document-planner.git
git branch -M main
git push -u origin main
```

---

## STEP 3: DEPLOY TO RAILWAY

### 3.1 Login to Railway
1. Go to: **https://railway.app**
2. Click **"Login"**
3. Sign in with GitHub account
4. Authorize Railway to access your repositories

### 3.2 Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Choose **"rtb-document-planner"** repository
4. Click **"Deploy Now"**

### 3.3 Add PostgreSQL Database
1. In your project, click **"New"**
2. Select **"Database"**
3. Choose **"Add PostgreSQL"**
4. Wait for database to provision (1-2 minutes)
5. PostgreSQL will automatically create `DATABASE_URL` variable

### 3.4 Configure Environment Variables
1. Click on your **web service** (not database)
2. Go to **"Variables"** tab
3. Verify these variables exist:
   - ✓ `DATABASE_URL` (automatically added by Railway)
   - ✓ `PORT` (automatically added by Railway)

4. **IMPORTANT:** If `DATABASE_URL` starts with `postgres://`, Railway will auto-fix it to `postgresql://`

### 3.5 Configure Build Settings
1. Click on your web service
2. Go to **"Settings"** tab
3. Scroll to **"Build"** section
4. Verify:
   - **Root Directory:** Leave empty (or set to `/`)
   - **Build Command:** `cd backend && pip install -r requirements.txt`
   - **Start Command:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`

### 3.6 Deploy
1. Go to **"Deployments"** tab
2. Railway should auto-deploy
3. If not, click **"Deploy"** button
4. Wait 3-5 minutes for deployment

### 3.7 Get Your Backend URL
1. Go to **"Settings"** tab
2. Scroll to **"Domains"** section
3. Click **"Generate Domain"**
4. Copy the URL (e.g., `https://rtb-planner-production.up.railway.app`)

---

## STEP 4: UPDATE FRONTEND CONFIGURATION

### 4.1 Update config.js
```bash
cd /home/leo/Documents/rtb-document-planner-main/frontend
```

Edit `config.js`:
```javascript
// API Configuration
const CONFIG = {
    // Railway Production Backend
    API_URL: 'https://YOUR-RAILWAY-URL.up.railway.app'
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
```

Replace `YOUR-RAILWAY-URL` with your actual Railway domain.

### 4.2 Commit and Push
```bash
cd /home/leo/Documents/rtb-document-planner-main

git add frontend/config.js
git commit -m "Update backend URL to Railway"
git push origin main
```

---

## STEP 5: DEPLOY FRONTEND TO CLOUDFLARE PAGES

### 5.1 Login to Cloudflare Pages
1. Go to: **https://dash.cloudflare.com**
2. Login to your account
3. Go to **"Workers & Pages"**
4. Click **"Create application"**
5. Select **"Pages"** tab
6. Click **"Connect to Git"**

### 5.2 Connect Repository
1. Select **GitHub**
2. Choose **"rtb-document-planner"** repository
3. Click **"Begin setup"**

### 5.3 Configure Build Settings
- **Project name:** rtb-planner
- **Production branch:** main
- **Build command:** (leave empty)
- **Build output directory:** frontend
- **Root directory:** (leave empty)

### 5.4 Deploy
1. Click **"Save and Deploy"**
2. Wait 2-3 minutes
3. Your site will be live at: `https://rtb-planner.pages.dev`

---

## STEP 6: VERIFY DEPLOYMENT

### 6.1 Test Backend
```bash
# Replace with your Railway URL
curl https://YOUR-RAILWAY-URL.up.railway.app/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "total_users": 1,
  "message": "Database has 1 users - data is persistent"
}
```

### 6.2 Test Frontend
1. Open: `https://rtb-planner.pages.dev`
2. Should see landing page
3. Click **"Register"**
4. Create test account
5. Login
6. Try generating a Session Plan

### 6.3 Test Admin Access
1. Logout
2. Go to login
3. Use admin credentials:
   - **Phone:** +250789751597
   - **Password:** admin123
4. Should see admin dashboard

---

## 🔧 TROUBLESHOOTING

### Issue: "Application failed to respond"
**Solution:**
```bash
# Check Railway logs
# In Railway dashboard:
# 1. Click on your service
# 2. Go to "Deployments" tab
# 3. Click on latest deployment
# 4. View logs
```

### Issue: "Database connection failed"
**Solution:**
1. Check `DATABASE_URL` variable exists
2. Verify PostgreSQL database is running
3. Check logs for connection errors
4. Ensure `DATABASE_URL` uses `postgresql://` (not `postgres://`)

### Issue: "Module not found"
**Solution:**
1. Check `backend/requirements.txt` is complete
2. Verify build command includes `cd backend`
3. Redeploy with correct build command

### Issue: "Port binding failed"
**Solution:**
1. Ensure start command uses `--port $PORT`
2. Don't hardcode port number
3. Railway automatically sets `PORT` variable

### Issue: Frontend can't connect to backend
**Solution:**
1. Verify `frontend/config.js` has correct Railway URL
2. Check CORS settings in `backend/main.py`
3. Ensure Railway domain is generated and active

---

## 📊 DEPLOYMENT CHECKLIST

### Backend (Railway)
- [ ] Repository pushed to GitHub
- [ ] Railway project created
- [ ] PostgreSQL database added
- [ ] Environment variables configured
- [ ] Build settings correct
- [ ] Deployment successful
- [ ] Domain generated
- [ ] Health check returns 200
- [ ] Database has admin user

### Frontend (Cloudflare Pages)
- [ ] Repository connected
- [ ] Build settings configured
- [ ] Deployment successful
- [ ] config.js updated with Railway URL
- [ ] Site loads without errors
- [ ] Can register new user
- [ ] Can login
- [ ] Can generate documents

---

## 🎯 EXPECTED URLS

After successful deployment:

**Backend (Railway):**
- URL: `https://rtb-planner-production.up.railway.app`
- Health: `https://rtb-planner-production.up.railway.app/health`
- API Docs: `https://rtb-planner-production.up.railway.app/docs`

**Frontend (Cloudflare Pages):**
- URL: `https://rtb-planner.pages.dev`
- Alternative: `https://rtb-planner-YOUR-SUBDOMAIN.pages.dev`

---

## 🚀 QUICK COMMANDS

### Check Deployment Status
```bash
# Test backend health
curl https://YOUR-RAILWAY-URL.up.railway.app/health

# Test API endpoint
curl https://YOUR-RAILWAY-URL.up.railway.app/api

# View Railway logs (in dashboard)
# Railway Dashboard → Your Service → Deployments → Latest → Logs
```

### Redeploy
```bash
# Make changes
git add .
git commit -m "Update deployment"
git push origin main

# Railway will auto-deploy
# Cloudflare Pages will auto-deploy
```

### Rollback (if needed)
```bash
# In Railway Dashboard:
# 1. Go to "Deployments" tab
# 2. Find previous working deployment
# 3. Click "..." menu
# 4. Select "Redeploy"
```

---

## 💡 RAILWAY TIPS

### Free Tier Limits
- ✓ 500 hours/month execution time
- ✓ 512 MB RAM
- ✓ 1 GB disk space
- ✓ Shared CPU
- ✓ PostgreSQL database included

### Best Practices
1. **Use environment variables** for sensitive data
2. **Monitor logs** regularly
3. **Set up health checks** for uptime monitoring
4. **Use PostgreSQL** for production (not SQLite)
5. **Enable auto-deploy** from GitHub

### Cost Optimization
- Free tier is sufficient for moderate traffic
- Upgrade to Pro ($5/month) for:
  - More execution hours
  - Better performance
  - Priority support

---

## 📞 SUPPORT

### Railway Support
- Docs: https://docs.railway.app
- Discord: https://discord.gg/railway
- Status: https://status.railway.app

### Cloudflare Pages Support
- Docs: https://developers.cloudflare.com/pages
- Community: https://community.cloudflare.com

### RTB Planner Support
- Admin: +250789751597
- Developer: Trainer Leon

---

## ✅ SUCCESS CRITERIA

Your deployment is successful when:

1. ✅ Backend health check returns `{"status":"healthy"}`
2. ✅ Frontend loads at Cloudflare Pages URL
3. ✅ User can register and login
4. ✅ Session plan generates and downloads
5. ✅ Scheme of work generates and downloads
6. ✅ Assessment plan generates and downloads
7. ✅ Trainer report generates and downloads
8. ✅ Admin can login and see dashboard
9. ✅ All documents are RTB-compliant
10. ✅ System is accessible 24/7

---

## 🎉 NEXT STEPS AFTER DEPLOYMENT

1. **Test all features thoroughly**
2. **Share URLs with users**
3. **Monitor Railway logs for errors**
4. **Set up uptime monitoring** (UptimeRobot)
5. **Create user documentation**
6. **Collect feedback**
7. **Plan future enhancements**

---

**Your system is ready to deploy! Follow these steps carefully and you'll have a fully functional RTB Document Planner in production.** 🚀

*Good luck with your deployment!*
