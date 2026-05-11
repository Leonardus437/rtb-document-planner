# RTB Document Planner - Deployment Steps

## 🚀 STEP 1: Push to GitHub

```bash
# Initialize git (if not done)
git init

# Add all files
git add .

# Commit
git commit -m "RTB Document Planner - Production Ready 2026"

# Create GitHub repo at: https://github.com/new
# Then run:
git remote add origin https://github.com/YOUR_USERNAME/rtb-planner.git
git branch -M main
git push -u origin main
```

## 📦 STEP 2: Deploy Backend to Railway

1. Go to: https://railway.app
2. Sign up/Login with GitHub
3. Click: **New Project** → **Deploy from GitHub repo**
4. Select your repository: `rtb-planner`
5. Click: **Deploy Now**
6. Add PostgreSQL: Click **+ New** → **Database** → **PostgreSQL**
7. Wait 3-5 minutes for deployment
8. Go to Settings → Domains → Generate Domain
9. Copy your backend URL: `https://rtb-planner-backend.up.railway.app`

## 🌐 STEP 3: Update Frontend Configuration

```bash
# Run this script
prepare_deploy.bat

# When prompted, enter your Render backend URL
# Example: https://rtb-planner-backend.onrender.com
```

## 🔄 STEP 4: Push Frontend Updates

```bash
git add frontend/config.js
git commit -m "Update API URL for production"
git push origin main
```

## ☁️ STEP 5: Deploy Frontend to Cloudflare

1. Go to: https://dash.cloudflare.com
2. Navigate: **Workers & Pages** → **Create** → **Pages**
3. Click: **Connect to Git**
4. Select your repository: `rtb-planner`
5. Configure:
   - **Project name**: `rtb-planner`
   - **Build command**: (leave empty)
   - **Build output directory**: `frontend`
   - **Root directory**: `/`
6. Click: **Save and Deploy**
7. Wait 2-3 minutes
8. Copy your frontend URL: `https://rtb-planner.pages.dev`

## 🔧 STEP 6: Update CORS (Important!)

Edit `backend/main.py` line 20-25:

```python
allow_origins=[
    "https://rtb-planner.pages.dev",  # Your Cloudflare URL
    "http://localhost:5173",
],
```

Push changes:
```bash
git add backend/main.py
git commit -m "Update CORS for production"
git push origin main
```

Render will auto-redeploy in 2-3 minutes.

## ✅ STEP 7: Test Your Deployment

1. Visit: `https://rtb-planner.pages.dev`
2. Register a test account
3. Login
4. Create a session plan
5. Download the DOCX file
6. Test admin login: +250789751597 / admin123

## 🎉 DONE!

Your RTB Document Planner is now live!

- Frontend: https://rtb-planner.pages.dev
- Backend: https://rtb-planner-backend.onrender.com
- Database: PostgreSQL (Render managed)
- Cost: FREE

## 📊 Monitor Your App

- **Render Dashboard**: https://dashboard.render.com
- **Cloudflare Dashboard**: https://dash.cloudflare.com

## 🐛 Troubleshooting

**Backend not responding?**
- Check Render logs
- Verify DATABASE_URL is set
- Check build logs

**Frontend can't connect?**
- Verify config.js has correct API_URL
- Check CORS settings
- Open browser console (F12) for errors

**Need help?**
- Check DEPLOYMENT_GUIDE.md
- Review Render logs
- Test locally first with test_system.bat
