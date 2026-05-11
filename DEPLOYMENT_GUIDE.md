# 🚀 RTB Document Planner - Deployment Guide

## Pre-Deployment Testing

### Run System Test
```bash
test_system.bat
```
This will verify:
- ✅ Python installation
- ✅ Dependencies
- ✅ Database
- ✅ Backend files
- ✅ Frontend files
- ✅ Backend server
- ✅ API endpoints

---

## 🗄️ Database Options

### Option 1: PostgreSQL on Render (RECOMMENDED)
- **Cost**: FREE
- **Storage**: 1GB
- **Best for**: Production deployment
- **Auto-configured** in render.yaml

### Option 2: SQLite (Current)
- **Cost**: FREE
- **Storage**: Unlimited (file-based)
- **Best for**: Local development
- **Limitation**: File storage on Render (resets on redeploy)

### Option 3: External PostgreSQL
- **Supabase**: Free tier with 500MB
- **ElephantSQL**: Free tier with 20MB
- **Neon**: Free tier with 3GB

**RECOMMENDATION**: Use PostgreSQL on Render (Option 1) - it's free and integrated!

---

## 📦 Backend Deployment (Render)

### Step 1: Prepare Repository
```bash
# Initialize git if not already done
git init
git add .
git commit -m "Ready for deployment"

# Push to GitHub
git remote add origin YOUR_GITHUB_REPO_URL
git push -u origin main
```

### Step 2: Deploy to Render

1. **Go to**: https://render.com
2. **Sign up/Login** with GitHub
3. **Click**: "New +" → "Blueprint"
4. **Connect** your GitHub repository
5. **Render will auto-detect** `render.yaml`
6. **Click**: "Apply"

Render will:
- ✅ Create PostgreSQL database
- ✅ Create web service
- ✅ Install dependencies
- ✅ Initialize database
- ✅ Start backend

### Step 3: Get Backend URL
After deployment completes:
- Your backend URL: `https://rtb-planner-backend.onrender.com`
- Copy this URL for frontend configuration

---

## 🌐 Frontend Deployment (Cloudflare Pages)

### Step 1: Prepare Frontend

Create `frontend/config.js`:
```javascript
const API_URL = 'https://rtb-planner-backend.onrender.com';
```

Update all frontend files to use `API_URL`:
```javascript
// Replace all instances of:
// 'http://localhost:5000'
// with:
// API_URL
```

### Step 2: Deploy to Cloudflare Pages

1. **Go to**: https://dash.cloudflare.com
2. **Navigate**: Workers & Pages → Create application → Pages
3. **Connect** your GitHub repository
4. **Configure**:
   - **Build command**: (leave empty)
   - **Build output directory**: `frontend`
   - **Root directory**: `/`
5. **Click**: "Save and Deploy"

### Step 3: Get Frontend URL
- Your frontend URL: `https://rtb-planner.pages.dev`
- Custom domain available in settings

---

## 🔧 Alternative: Simple Render Deployment

If you prefer simpler setup without Blueprint:

### Backend Only
1. **New Web Service** on Render
2. **Connect** GitHub repo
3. **Configure**:
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && python init_database.py && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Root Directory**: `/`
4. **Add PostgreSQL Database**:
   - Go to Dashboard → New → PostgreSQL
   - Connect to your web service
5. **Deploy**

---

## 🔄 Update CORS in Backend

Edit `backend/main.py`:
```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://rtb-planner.pages.dev",  # Your Cloudflare URL
        "http://localhost:5173",  # Local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ Post-Deployment Checklist

### Backend
- [ ] Service is running (green status)
- [ ] Database connected
- [ ] API endpoint responds: `/api`
- [ ] Admin user created

### Frontend
- [ ] Site loads correctly
- [ ] Login page works
- [ ] Registration works
- [ ] Session plan creation works
- [ ] Scheme creation works
- [ ] Document download works

### Test URLs
```bash
# Backend health
curl https://YOUR-BACKEND.onrender.com/api

# Frontend
https://YOUR-FRONTEND.pages.dev
```

---

## 🐛 Troubleshooting

### Backend Issues

**Database Connection Error**
```bash
# Check environment variables in Render dashboard
# Ensure DATABASE_URL is set
```

**Build Failed**
```bash
# Check Python version (3.11.0)
# Verify requirements.txt
# Check build logs
```

**Service Won't Start**
```bash
# Check start command
# Verify init_database.py runs
# Check application logs
```

### Frontend Issues

**API Calls Failing**
- Check CORS settings in backend
- Verify API_URL in frontend config
- Check browser console for errors

**Pages Not Loading**
- Verify build output directory
- Check file paths (case-sensitive)
- Review deployment logs

---

## 💰 Cost Breakdown

### FREE Tier (Recommended)
- **Render Backend**: FREE (750 hours/month)
- **Render PostgreSQL**: FREE (1GB storage)
- **Cloudflare Pages**: FREE (Unlimited requests)
- **Total**: $0/month

### Limitations
- Backend sleeps after 15 min inactivity (wakes in ~30s)
- 1GB database storage
- 512MB RAM

### Upgrade Options
- **Render Starter**: $7/month (no sleep, 1GB RAM)
- **PostgreSQL**: $7/month (10GB storage)

---

## 🔐 Security Recommendations

Before going live:

1. **Add Password Hashing**
```python
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"])
```

2. **Add JWT Authentication**
```python
from jose import JWTError, jwt
```

3. **Environment Variables**
```bash
# Add to Render
SECRET_KEY=your-secret-key
ALGORITHM=HS256
```

4. **HTTPS Only**
- Render provides free SSL
- Cloudflare provides free SSL

---

## 📊 Monitoring

### Render Dashboard
- View logs
- Monitor CPU/Memory
- Check request metrics
- Database connections

### Cloudflare Analytics
- Page views
- Bandwidth usage
- Geographic distribution
- Performance metrics

---

## 🎯 Quick Deploy Commands

```bash
# Test locally first
test_system.bat

# Commit changes
git add .
git commit -m "Production ready"
git push origin main

# Render will auto-deploy on push
# Cloudflare will auto-deploy on push
```

---

## 📞 Support Resources

- **Render Docs**: https://render.com/docs
- **Cloudflare Docs**: https://developers.cloudflare.com/pages
- **FastAPI Docs**: https://fastapi.tiangolo.com
- **PostgreSQL Docs**: https://www.postgresql.org/docs

---

## 🎉 Success!

Your RTB Document Planner is now live:
- ✅ Backend API running on Render
- ✅ PostgreSQL database active
- ✅ Frontend hosted on Cloudflare
- ✅ Free tier with room to grow

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
