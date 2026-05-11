# 🚀 DEPLOYMENT GUIDE - RTB Document Planner

## ✅ Logo Upload Feature Added!

### New Features
- ✅ RTB Logo upload (left side of documents)
- ✅ School Logo upload (right side of documents)
- ✅ Works for both Session Plans and Schemes of Work
- ✅ Optional - documents work without logos too

---

## 📦 Deployment Options

### Option 1: Render (Backend) + Cloudflare Pages (Frontend)

#### Backend on Render
1. Push code to GitHub: https://github.com/Leonardus437/rtb-document-planner
2. Go to https://render.com
3. Click "New +" → "Web Service"
4. Connect your GitHub repository
5. Configure:
   - **Name**: rtb-document-planner-api
   - **Environment**: Python 3
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: Free
6. Add Environment Variable:
   - `PYTHON_VERSION` = `3.11.0`
7. Deploy!

Your backend will be at: `https://rtb-document-planner-api.onrender.com`

#### Frontend on Cloudflare Pages
1. Go to https://dash.cloudflare.com
2. Pages → Create a project
3. Connect to Git → Select your repository
4. Configure:
   - **Project name**: rtb-document-planner
   - **Production branch**: main
   - **Build command**: (leave empty)
   - **Build output directory**: frontend
5. Environment variables:
   - `API_URL` = `https://rtb-document-planner-api.onrender.com`
6. Deploy!

Your frontend will be at: `https://rtb-document-planner.pages.dev`

---

### Option 2: Full Deployment on Render

1. Push to GitHub
2. Create Web Service on Render
3. Use these settings:
   - **Build Command**: `pip install -r backend/requirements.txt`
   - **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
4. Your app will serve both frontend and backend

---

## 🔧 Configuration Files Created

### For Render: `render.yaml`
```yaml
services:
  - type: web
    name: rtb-document-planner
    env: python
    buildCommand: pip install -r backend/requirements.txt
    startCommand: cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

### For Frontend: Update `config.js`
```javascript
const CONFIG = {
    API_URL: 'https://rtb-document-planner-api.onrender.com'
};
```

---

## 📝 Pre-Deployment Checklist

- [x] Logo upload feature added
- [x] Database migration completed
- [x] Models updated
- [x] Schemas updated
- [x] Frontend wizards updated
- [x] Document generator updated
- [x] All features tested locally

---

## 🚀 Quick Deploy Steps

### 1. Push to GitHub
```bash
cd e:\rtb-document-planner-main
git init
git add .
git commit -m "Add logo upload feature and prepare for deployment"
git branch -M main
git remote add origin https://github.com/Leonardus437/rtb-document-planner.git
git push -u origin main
```

### 2. Deploy Backend (Render)
- Go to render.com
- New Web Service
- Connect GitHub repo
- Auto-deploy from `render.yaml`

### 3. Deploy Frontend (Cloudflare Pages)
- Go to Cloudflare Pages
- Connect GitHub repo
- Set build output: `frontend`
- Add API_URL environment variable
- Deploy!

---

## 🌐 After Deployment

### Update Frontend Config
Edit `frontend/config.js`:
```javascript
const CONFIG = {
    API_URL: 'https://your-backend-url.onrender.com'
};
```

### Test Your Deployment
1. Visit your Cloudflare Pages URL
2. Register a new account
3. Create a session plan with logos
4. Create a scheme of work with logos
5. Download and verify documents

---

## 🎉 You're Live!

Your RTB Document Planner will be accessible at:
- **Frontend**: https://rtb-document-planner.pages.dev
- **Backend API**: https://rtb-document-planner-api.onrender.com

---

## 📞 Support

If you encounter issues:
1. Check Render logs for backend errors
2. Check Cloudflare Pages build logs
3. Verify API_URL in config.js
4. Test API endpoints directly

---

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
