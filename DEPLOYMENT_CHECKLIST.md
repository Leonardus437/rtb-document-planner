# 🚀 RTB Document Planner - Deployment Checklist

## ✅ Pre-Deployment

### Local Testing
- [ ] Run `test_system.bat` - all tests pass
- [ ] Test user registration
- [ ] Test user login
- [ ] Test session plan creation
- [ ] Test session plan download
- [ ] Test scheme of work creation
- [ ] Test scheme of work download
- [ ] Test admin dashboard

### Code Preparation
- [ ] All files committed to git
- [ ] `.gitignore` configured
- [ ] `requirements.txt` updated with psycopg2-binary
- [ ] `database.py` supports PostgreSQL
- [ ] `render.yaml` configured

---

## 🗄️ Database Decision

Choose ONE option:

### ✅ Option 1: PostgreSQL on Render (RECOMMENDED)
**Pros:**
- Free tier (1GB storage)
- Integrated with Render
- Auto-configured via render.yaml
- Production-ready
- Persistent data

**Cons:**
- 1GB limit on free tier

**Setup:** Automatic via render.yaml

---

### Option 2: SQLite (Keep Current)
**Pros:**
- No setup needed
- Works locally
- Unlimited storage

**Cons:**
- File resets on Render redeploy
- Not recommended for production
- Data loss on restart

**Setup:** No changes needed (current setup)

---

### Option 3: External PostgreSQL
**Providers:**
- **Supabase**: 500MB free
- **ElephantSQL**: 20MB free  
- **Neon**: 3GB free

**Setup:** Manual DATABASE_URL configuration

---

## 📦 Backend Deployment (Render)

### Step 1: GitHub Setup
```bash
# Initialize repository
git init
git add .
git commit -m "Initial commit - RTB Document Planner"

# Create GitHub repo and push
git remote add origin https://github.com/YOUR_USERNAME/rtb-planner.git
git branch -M main
git push -u origin main
```

### Step 2: Render Deployment
- [ ] Go to https://render.com
- [ ] Sign up/Login with GitHub
- [ ] Click "New +" → "Blueprint"
- [ ] Select your repository
- [ ] Click "Apply"
- [ ] Wait for deployment (5-10 minutes)
- [ ] Copy backend URL: `https://rtb-planner-backend.onrender.com`

### Step 3: Verify Backend
- [ ] Visit: `https://YOUR-BACKEND.onrender.com/api`
- [ ] Should see: `{"message": "RTB Document Planner API", "status": "online"}`
- [ ] Check logs for errors
- [ ] Verify database connected

---

## 🌐 Frontend Deployment (Cloudflare Pages)

### Step 1: Update Configuration
```bash
# Run the preparation script
prepare_deploy.bat

# Enter your Render backend URL when prompted
```

OR manually edit `frontend/config.js`:
```javascript
const CONFIG = {
    API_URL: 'https://YOUR-BACKEND.onrender.com',
};
```

### Step 2: Commit Changes
```bash
git add frontend/config.js
git commit -m "Update API URL for production"
git push origin main
```

### Step 3: Cloudflare Deployment
- [ ] Go to https://dash.cloudflare.com
- [ ] Navigate: Workers & Pages → Create → Pages
- [ ] Connect GitHub repository
- [ ] Configure:
  - **Project name**: rtb-planner
  - **Build command**: (leave empty)
  - **Build output directory**: `frontend`
  - **Root directory**: `/`
- [ ] Click "Save and Deploy"
- [ ] Wait for deployment (2-3 minutes)
- [ ] Copy frontend URL: `https://rtb-planner.pages.dev`

### Step 4: Update CORS
Edit `backend/main.py` and update:
```python
allow_origins=[
    "https://rtb-planner.pages.dev",  # Your Cloudflare URL
    "http://localhost:5173",
],
```

Commit and push:
```bash
git add backend/main.py
git commit -m "Update CORS for production"
git push origin main
```

Render will auto-redeploy.

---

## 🧪 Post-Deployment Testing

### Backend Tests
- [ ] API health: `https://YOUR-BACKEND.onrender.com/api`
- [ ] Stats endpoint: `https://YOUR-BACKEND.onrender.com/stats`
- [ ] Check logs in Render dashboard

### Frontend Tests
- [ ] Visit: `https://YOUR-FRONTEND.pages.dev`
- [ ] Login page loads
- [ ] Register new user
- [ ] Login with test user
- [ ] Create session plan
- [ ] Download session plan DOCX
- [ ] Create scheme of work
- [ ] Download scheme DOCX
- [ ] Admin login: +250789751597 / admin123
- [ ] View admin dashboard

### Integration Tests
- [ ] Frontend connects to backend
- [ ] No CORS errors in browser console (F12)
- [ ] Documents generate correctly
- [ ] Downloads work
- [ ] Database persists data

---

## 🔧 Configuration Summary

### Local Development
```javascript
API_URL: 'http://localhost:5000'
DATABASE: SQLite (rtb_planner.db)
```

### Production
```javascript
API_URL: 'https://rtb-planner-backend.onrender.com'
DATABASE: PostgreSQL (Render managed)
```

---

## 📊 Monitoring

### Render Dashboard
- [ ] Backend service status: Running (green)
- [ ] Database status: Available (green)
- [ ] Check logs for errors
- [ ] Monitor CPU/Memory usage

### Cloudflare Dashboard
- [ ] Deployment status: Active
- [ ] Check analytics
- [ ] Monitor page views

---

## 🐛 Common Issues

### Backend Won't Start
```bash
# Check Render logs
# Verify Python version (3.11.0)
# Check DATABASE_URL environment variable
# Verify requirements.txt
```

### Database Connection Failed
```bash
# Ensure PostgreSQL service is running
# Check DATABASE_URL format
# Verify psycopg2-binary installed
```

### Frontend Can't Connect
```bash
# Check config.js has correct API_URL
# Verify CORS settings in backend
# Check browser console (F12) for errors
```

### CORS Errors
```bash
# Update allow_origins in backend/main.py
# Include your Cloudflare Pages URL
# Redeploy backend
```

---

## 💰 Cost Summary

### FREE Tier (Current Setup)
- Render Web Service: FREE (750 hrs/month)
- Render PostgreSQL: FREE (1GB)
- Cloudflare Pages: FREE (Unlimited)
- **Total: $0/month**

### Limitations
- Backend sleeps after 15 min inactivity
- First request after sleep: ~30s wake time
- 1GB database storage
- 512MB RAM

### Upgrade Path
- Render Starter: $7/month (no sleep)
- PostgreSQL: $7/month (10GB)

---

## 🎉 Deployment Complete!

Your RTB Document Planner is now live:

- ✅ Backend: `https://rtb-planner-backend.onrender.com`
- ✅ Frontend: `https://rtb-planner.pages.dev`
- ✅ Database: PostgreSQL (Render)
- ✅ Cost: FREE

### Share Your App
- Frontend URL: `https://rtb-planner.pages.dev`
- Admin: +250789751597 / admin123
- Teachers can register and start creating documents!

---

## 📞 Support

- **Render**: https://render.com/docs
- **Cloudflare**: https://developers.cloudflare.com/pages
- **Issues**: Check logs in respective dashboards

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
