# 🚂 Railway Deployment Guide

## Quick Deploy to Railway

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Production ready"
git remote add origin https://github.com/YOUR_USERNAME/rtb-planner.git
git push -u origin main
```

### Step 2: Deploy to Railway

1. Go to: https://railway.app
2. Sign up with GitHub
3. Click: **New Project**
4. Select: **Deploy from GitHub repo**
5. Choose: `rtb-planner`
6. Click: **Deploy Now**

### Step 3: Add PostgreSQL Database

1. In your project, click: **+ New**
2. Select: **Database**
3. Choose: **PostgreSQL**
4. Railway auto-connects it to your app

### Step 4: Generate Domain

1. Click on your service
2. Go to: **Settings** → **Domains**
3. Click: **Generate Domain**
4. Copy your URL: `https://rtb-planner-backend.up.railway.app`

### Step 5: Update Frontend

```bash
prepare_deploy.bat
# Enter your Railway backend URL
git push origin main
```

### Step 6: Deploy Frontend to Cloudflare

1. Go to: https://dash.cloudflare.com
2. Workers & Pages → Create → Pages
3. Connect GitHub repo
4. Build output: `frontend`
5. Deploy

## ✅ Done!

Your app is live on Railway + Cloudflare!

- Backend: Railway ($5/month free credit)
- Frontend: Cloudflare (Free unlimited)
- Database: PostgreSQL on Railway (Free)
