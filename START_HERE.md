# 🚀 DEPLOY YOUR RTB DOCUMENT PLANNER NOW!

## Quick Start (5 Minutes)

### 1️⃣ Run Deployment Script
```bash
deploy.bat
```

### 2️⃣ Create GitHub Repository
- Go to: https://github.com/new
- Name: `rtb-planner`
- Create repository

### 3️⃣ Push Code
```bash
git remote add origin https://github.com/YOUR_USERNAME/rtb-planner.git
git push -u origin main
```

### 4️⃣ Deploy Backend (Railway)
1. Visit: https://railway.app
2. Sign in with GitHub
3. Click: **New Project** → **Deploy from GitHub repo**
4. Select: `rtb-planner`
5. Click: **Deploy Now**
6. Add Database: Click **+ New** → **Database** → **PostgreSQL**
7. ⏰ Wait 3-5 minutes
8. ✅ Copy your backend URL (Settings → Domains)

### 5️⃣ Update Frontend
```bash
prepare_deploy.bat
# Enter your backend URL when prompted
git push origin main
```

### 6️⃣ Deploy Frontend (Cloudflare)
1. Visit: https://dash.cloudflare.com
2. **Workers & Pages** → **Create** → **Pages**
3. Connect GitHub
4. Select: `rtb-planner`
5. Build output: `frontend`
6. Click: **Save and Deploy**
7. ⏰ Wait 2-3 minutes
8. ✅ Done!

## 🎉 Your App is LIVE!

- **Frontend**: https://rtb-planner.pages.dev
- **Backend**: https://rtb-planner-backend.up.railway.app
- **Database**: PostgreSQL on Railway
- **Cost**: FREE ($5/month Railway credit)

## 📱 Share with Teachers

"Visit https://rtb-planner.pages.dev to create professional RTB session plans and schemes of work!"

## 🔐 Admin Access

- Phone: +250789751597
- Password: admin123

## 📚 Need Help?

- **Full Guide**: DEPLOY_NOW.md
- **Checklist**: DEPLOYMENT_CHECKLIST.txt
- **Troubleshooting**: DEPLOYMENT_GUIDE.md

---

© 2026 Official RTB Document Planner | Developed for TVET Excellence
**DEVELOPED BY Trainer Leon**

Made with ❤️ for TVET Excellence in Rwanda 🇷🇼
