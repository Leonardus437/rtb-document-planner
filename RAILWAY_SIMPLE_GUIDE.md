# 🎯 RAILWAY DEPLOYMENT - SIMPLE STEPS

## 📋 What You Need
- GitHub account (you have it ✅)
- 10 minutes of time
- Your GitHub repo: https://github.com/Leonardus437/rtb-document-planner

---

## 🚀 STEP-BY-STEP GUIDE

### STEP 1: Create Railway Account
```
🌐 Go to: https://railway.app
👆 Click: "Login"
🔗 Select: "Login with GitHub"
✅ Authorize Railway
```
**Time**: 1 minute

---

### STEP 2: Create New Project
```
👆 Click: "New Project"
📦 Select: "Deploy from GitHub repo"
🔍 Find: "Leonardus437/rtb-document-planner"
✅ Click: "Deploy Now"
⏳ Wait: 2-3 minutes for build
```
**Time**: 3 minutes

---

### STEP 3: Add PostgreSQL Database
```
👆 Click: "+ New" (in your project)
💾 Select: "Database"
🐘 Choose: "PostgreSQL"
⏳ Wait: Green checkmark appears
```
**Time**: 1 minute

---

### STEP 4: Get Your Backend URL
```
👆 Click: Your web service (not database)
⚙️ Go to: "Settings" tab
📍 Scroll to: "Domains" section
🔗 Click: "Generate Domain"
📋 Copy: Your URL (e.g., https://rtb-planner.up.railway.app)
```
**Time**: 30 seconds

---

### STEP 5: Update Frontend
Open `frontend/config.js` and change:

**FROM:**
```javascript
const API_URL = 'https://rtb-document-planner-api.onrender.com';
```

**TO:**
```javascript
const API_URL = 'https://your-railway-url.up.railway.app';
```

Then commit and push:
```bash
git add frontend/config.js
git commit -m "Update API URL to Railway"
git push origin main
```

**Time**: 2 minutes

---

### STEP 6: Initialize Database
Open these URLs in your browser (replace with YOUR Railway URL):

**URL 1:**
```
https://your-app.up.railway.app/migrate-database?secret_key=RTB2024MIGRATE
```
✅ Should see: "Migration completed successfully"

**URL 2:**
```
https://your-app.up.railway.app/init-production-db?secret_key=RTB2024INIT
```
✅ Should see: "Admin user created" + 5 demo teachers

**Time**: 1 minute

---

### STEP 7: Test Your App! 🎉
```
🌐 Go to: https://ikidanago.pages.dev
👆 Click: "Sign In"
📱 Phone: +250789751597
🔒 Password: admin123
✅ Login should work!
```

Try creating a session plan or scheme!

**Time**: 2 minutes

---

## ✅ VERIFICATION

### Check Backend is Running
Visit: `https://your-railway-url.up.railway.app/`

Should see:
```json
{
  "message": "RTB Document Planner API",
  "status": "online"
}
```

### Check Database Has Users
Visit: `https://your-railway-url.up.railway.app/stats`

Should see:
```json
{
  "total_users": 6,
  "total_session_plans": 0,
  "total_schemes": 0
}
```

### Check Frontend Connects
1. Open: https://ikidanago.pages.dev
2. Press F12 (open console)
3. Should see NO red errors
4. Login should work perfectly

---

## 💰 COST: $0/MONTH

Railway gives you **$5 FREE credit every month**.

Your app uses **~$3/month**.

**You pay: $0** ✅

---

## 🎯 WHAT YOU GET

✅ **Persistent Storage** - Users never disappear
✅ **Always Awake** - No sleep delays
✅ **PostgreSQL** - Professional database
✅ **1GB RAM** - Better performance
✅ **100% FREE** - Within $5 credit

---

## 🐛 PROBLEMS?

### Build Failed
- Check Railway logs
- Ensure all files pushed to GitHub
- Try "Redeploy" button

### Can't Connect to Database
- Ensure PostgreSQL is running (green)
- Check DATABASE_URL is set
- Restart web service

### Frontend Shows Errors
- Check config.js has correct URL
- Clear browser cache
- Wait for Cloudflare to redeploy (2 min)

---

## 📞 HELP

**Railway Docs**: https://docs.railway.app
**Railway Discord**: https://discord.gg/railway

**Your Guides**:
- `RAILWAY_QUICKSTART.md` - Quick reference
- `RAILWAY_DEPLOYMENT.md` - Detailed guide
- `RAILWAY_MIGRATION_SUMMARY.md` - Complete info

---

## 🎉 DONE!

Once deployed:
- Teachers can register and login
- Users stay forever (no more disappearing!)
- Backend always responds instantly
- Documents generate perfectly
- Admin dashboard works great

**Enjoy your persistent, always-awake backend!** 🚀

---

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
