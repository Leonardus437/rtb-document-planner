# 🚀 QUICK START - Railway Deployment

## ⚡ 5-Minute Setup

### Step 1: Sign Up (1 minute)
1. Go to: https://railway.app
2. Click "Login" → "Login with GitHub"
3. Authorize Railway

### Step 2: Deploy Backend (2 minutes)
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose: `Leonardus437/rtb-document-planner`
4. Click "Deploy Now"
5. Wait for build to complete

### Step 3: Add Database (1 minute)
1. In your project, click "+ New"
2. Select "Database" → "PostgreSQL"
3. Wait for green status (ready)

### Step 4: Get Your URL (30 seconds)
1. Click on your web service
2. Click "Settings" tab
3. Scroll to "Domains"
4. Click "Generate Domain"
5. Copy your URL: `https://rtb-document-planner-production.up.railway.app`

### Step 5: Update Frontend (30 seconds)
1. Open: `frontend/config.js`
2. Replace API_URL with your Railway URL
3. Save, commit, push to GitHub
4. Cloudflare Pages auto-deploys

### Step 6: Initialize Database (30 seconds)
Visit these URLs once (replace with your Railway URL):
```
https://your-app.up.railway.app/migrate-database?secret_key=RTB2024MIGRATE
https://your-app.up.railway.app/init-production-db?secret_key=RTB2024INIT
```

## ✅ Done!

Test your app:
- Frontend: https://ikidanago.pages.dev
- Login: +250789751597 / admin123

## 💰 Cost: $0/month
Your app uses ~$3/month, Railway gives you $5/month FREE!

## 🎉 Benefits
- ✅ Users stay forever (persistent PostgreSQL)
- ✅ Backend always awake
- ✅ No more database wipes
- ✅ 1GB RAM (2x better than Render)
- ✅ Professional reliability

---

**Need help?** Check RAILWAY_DEPLOYMENT.md for detailed guide.
