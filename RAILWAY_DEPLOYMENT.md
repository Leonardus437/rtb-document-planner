# 🚂 Railway.app Deployment Guide

## ✅ What You Get (100% FREE)
- $5 free credit every month (auto-renews)
- Persistent PostgreSQL database (users never disappear)
- Always awake backend
- 1GB RAM (better than Render)
- No credit card required to start

## 📋 Step-by-Step Deployment

### 1. Create Railway Account
1. Go to https://railway.app
2. Click "Login" → Sign in with GitHub
3. Authorize Railway to access your GitHub

### 2. Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `Leonardus437/rtb-document-planner`
4. Click "Deploy Now"

### 3. Add PostgreSQL Database
1. In your project, click "New"
2. Select "Database" → "PostgreSQL"
3. Railway automatically creates database
4. Wait for database to be ready (green status)

### 4. Configure Environment Variables
Railway auto-detects `DATABASE_URL` from PostgreSQL.

**Optional**: Add custom variables:
1. Click on your service (web)
2. Go to "Variables" tab
3. Add any custom variables if needed

### 5. Deploy!
1. Railway automatically builds and deploys
2. Wait 2-3 minutes for deployment
3. Click "Generate Domain" to get your URL
4. Your backend will be at: `https://your-app.up.railway.app`

### 6. Update Frontend Config
1. Copy your Railway URL
2. Update `frontend/config.js`:
```javascript
const API_URL = 'https://your-app.up.railway.app';
```
3. Commit and push to GitHub
4. Redeploy frontend on Cloudflare Pages

### 7. Initialize Database (First Time Only)
Visit these URLs once:
```
https://your-app.up.railway.app/migrate-database?secret_key=RTB2024MIGRATE
https://your-app.up.railway.app/init-production-db?secret_key=RTB2024INIT
```

## ✅ Verification
1. Visit: `https://your-app.up.railway.app/`
2. Should see: `{"message": "RTB Document Planner API", "status": "online"}`
3. Test login at your frontend: https://ikidanago.pages.dev

## 🎯 Benefits Over Render
| Feature | Render Free | Railway Free |
|---------|-------------|--------------|
| Storage | ❌ Wipes | ✅ Persistent |
| Uptime | ❌ Sleeps | ✅ Always awake |
| RAM | 512MB | 1GB |
| Database | SQLite (temp) | PostgreSQL (permanent) |
| Users Stay | ❌ No | ✅ Yes |

## 💰 Cost Tracking
- Check usage: Railway Dashboard → Project → Usage
- Typical usage: $2-4/month (well under $5 free credit)
- If you exceed $5: Railway pauses service until next month

## 🔧 Troubleshooting

### Build Fails
- Check "Deployments" tab for error logs
- Ensure `requirements.txt` is correct
- Verify Python version compatibility

### Database Connection Error
- Ensure PostgreSQL service is running (green)
- Check `DATABASE_URL` is set automatically
- Restart the web service

### App Not Responding
- Check "Logs" tab for errors
- Verify PORT environment variable is used
- Ensure `--host 0.0.0.0` in start command

## 📞 Support
- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- Check logs in Railway dashboard

## 🎉 Success!
Once deployed:
- ✅ Backend always awake
- ✅ Users stay forever
- ✅ No more database wipes
- ✅ Professional reliability
- ✅ 100% FREE (within $5/month)

---

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
