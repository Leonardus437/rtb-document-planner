# 🚀 RTB Document Planner - Complete Deployment Guide

## 📋 Pre-Deployment Checklist

### Step 1: Test Local System
```bash
# Run the test batch file
test_and_verify_system.bat
```

This will verify:
- ✅ Python installation
- ✅ Project structure
- ✅ Dependencies
- ✅ Database connection
- ✅ Port availability
- ✅ Backend startup
- ✅ Frontend files

### Step 2: Start Local System (Verify Everything Works)
```bash
# Start the system locally
start_rtb_system.bat
```

Test these features:
1. Register a new user
2. Login as user
3. Create a session plan
4. Create a scheme of work
5. Download both documents
6. Login as admin (+250789751597 / admin123)
7. View users and statistics

---

## 🗄️ Database Recommendation

**Recommended: PostgreSQL with Docker** ✅

### Why PostgreSQL?
- ✅ Production-ready and scalable
- ✅ Better performance for concurrent users
- ✅ Free tier on Render
- ✅ Easy migration from SQLite
- ✅ Better data integrity

### Current Setup:
Your system already supports both:
- **SQLite**: For local development (automatic)
- **PostgreSQL**: For production (via DATABASE_URL env variable)

---

## 🚀 Deployment Steps

### Part 1: Deploy Backend to Render (with PostgreSQL)

#### 1.1 Create Render Account
1. Go to https://render.com
2. Sign up with GitHub
3. Connect your GitHub repository

#### 1.2 Create PostgreSQL Database
1. Click "New +" → "PostgreSQL"
2. Settings:
   - **Name**: `rtb-planner-db`
   - **Database**: `rtb_planner`
   - **User**: `rtb_user`
   - **Region**: Frankfurt (or closest to you)
   - **Plan**: Free
3. Click "Create Database"
4. Wait for database to be ready (2-3 minutes)
5. **Copy the Internal Database URL** (starts with `postgres://`)

#### 1.3 Deploy Backend Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Settings:
   - **Name**: `rtb-planner-backend`
   - **Region**: Frankfurt (same as database)
   - **Branch**: main
   - **Root Directory**: (leave empty)
   - **Runtime**: Python 3
   - **Build Command**:
     ```bash
     cd backend && pip install --upgrade pip && pip install -r requirements.txt
     ```
   - **Start Command**:
     ```bash
     cd backend && python init_database.py && uvicorn main:app --host 0.0.0.0 --port $PORT
     ```
   - **Plan**: Free

4. **Environment Variables** (click "Advanced"):
   - `PYTHON_VERSION` = `3.11.0`
   - `DATABASE_URL` = (paste the Internal Database URL from step 1.2)
   - `CORS_ORIGINS` = `*`

5. Click "Create Web Service"
6. Wait for deployment (5-10 minutes)
7. **Copy your backend URL**: `https://rtb-planner-backend.onrender.com`

#### 1.4 Test Backend
Open in browser:
```
https://rtb-planner-backend.onrender.com/api
```

You should see:
```json
{
  "message": "RTB Document Planner API",
  "status": "online",
  "version": "3.0"
}
```

---

### Part 2: Deploy Frontend to Cloudflare Pages

#### 2.1 Update Frontend Config
1. Open `frontend/config.js`
2. Update the API_URL:
   ```javascript
   const CONFIG = {
       API_URL: 'https://rtb-planner-backend.onrender.com',
   };
   ```
3. Save and commit to GitHub

#### 2.2 Create Cloudflare Account
1. Go to https://pages.cloudflare.com
2. Sign up with email or GitHub
3. Verify your email

#### 2.3 Deploy to Cloudflare Pages
1. Click "Create a project"
2. Connect to Git → Select your repository
3. Settings:
   - **Project name**: `rtb-document-planner`
   - **Production branch**: main
   - **Build command**: (leave empty)
   - **Build output directory**: `frontend`
   - **Root directory**: `/`

4. Click "Save and Deploy"
5. Wait for deployment (2-3 minutes)
6. **Your site URL**: `https://rtb-document-planner.pages.dev`

#### 2.4 Configure Custom Domain (Optional)
1. In Cloudflare Pages → Custom domains
2. Add your domain (e.g., `rtbplanner.com`)
3. Follow DNS configuration instructions

---

## 🔧 Alternative: Docker Deployment (Local/VPS)

If you prefer Docker with PostgreSQL:

### 1. Start with Docker Compose
```bash
# Start all services (backend, frontend, PostgreSQL)
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### 2. Access Application
- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- PostgreSQL: localhost:5433

### 3. Deploy to VPS (DigitalOcean, AWS, etc.)
1. Copy project to VPS
2. Install Docker and Docker Compose
3. Run `docker-compose up -d`
4. Configure nginx reverse proxy
5. Add SSL certificate (Let's Encrypt)

---

## 🧪 Post-Deployment Testing

### Test Backend (Render)
```bash
# Test API
curl https://rtb-planner-backend.onrender.com/api

# Test registration
curl -X POST https://rtb-planner-backend.onrender.com/users/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","phone":"+250788888888","password":"test123"}'

# Test login
curl -X POST https://rtb-planner-backend.onrender.com/users/login \
  -H "Content-Type: application/json" \
  -d '{"phone":"+250788888888","password":"test123"}'
```

### Test Frontend (Cloudflare)
1. Open `https://rtb-document-planner.pages.dev`
2. Register new account
3. Login
4. Create session plan
5. Create scheme of work
6. Download documents
7. Test admin login

---

## 📊 Database Migration (SQLite → PostgreSQL)

If you have existing data in SQLite:

### Option 1: Manual Export/Import
```bash
# Export from SQLite
cd backend
python -c "
from database import SessionLocal
from models import User, SessionPlan, SchemeOfWork
import json

db = SessionLocal()
users = db.query(User).all()
plans = db.query(SessionPlan).all()
schemes = db.query(SchemeOfWork).all()

# Export to JSON
with open('export.json', 'w') as f:
    json.dump({
        'users': [u.__dict__ for u in users],
        'plans': [p.__dict__ for p in plans],
        'schemes': [s.__dict__ for s in schemes]
    }, f)
"

# Then import to PostgreSQL (set DATABASE_URL first)
```

### Option 2: Use pgloader (Recommended)
```bash
# Install pgloader
# Ubuntu/Debian: apt-get install pgloader
# macOS: brew install pgloader

# Convert
pgloader sqlite://rtb_planner.db postgresql://user:pass@host/dbname
```

---

## 🔐 Security Checklist

### Before Going Live:
- [ ] Change admin password from default
- [ ] Add password hashing (bcrypt)
- [ ] Implement JWT tokens
- [ ] Enable HTTPS only
- [ ] Set up environment variables properly
- [ ] Configure CORS for specific domains
- [ ] Add rate limiting
- [ ] Set up backup strategy
- [ ] Enable database SSL
- [ ] Add monitoring (Sentry, LogRocket)

---

## 📈 Monitoring & Maintenance

### Render Dashboard
- Monitor backend health
- View logs
- Check database usage
- Set up alerts

### Cloudflare Analytics
- Track page views
- Monitor performance
- Check error rates
- View geographic distribution

### Database Backups
Render automatically backs up PostgreSQL (free tier: 7 days retention)

---

## 🐛 Troubleshooting

### Backend Issues
```bash
# Check Render logs
# Go to Render Dashboard → Your Service → Logs

# Common issues:
# 1. Database connection: Check DATABASE_URL
# 2. Port binding: Render sets $PORT automatically
# 3. Dependencies: Check requirements.txt
```

### Frontend Issues
```bash
# Check Cloudflare Pages logs
# Go to Cloudflare Dashboard → Pages → Deployments

# Common issues:
# 1. API URL: Check config.js
# 2. CORS: Check backend CORS settings
# 3. Build: Ensure frontend/ directory is correct
```

### Database Issues
```bash
# Check PostgreSQL connection
# In Render Dashboard → Database → Connections

# Test connection
psql $DATABASE_URL
```

---

## 💰 Cost Breakdown

### Free Tier (Recommended for Start)
- **Render Backend**: Free (750 hours/month)
- **Render PostgreSQL**: Free (90 days, then $7/month)
- **Cloudflare Pages**: Free (unlimited)
- **Total**: $0/month (first 90 days), then $7/month

### Paid Tier (For Production)
- **Render Backend**: $7/month (always on)
- **Render PostgreSQL**: $7/month (1GB storage)
- **Cloudflare Pages**: Free
- **Custom Domain**: $10-15/year
- **Total**: ~$15/month + domain

---

## 🎯 Next Steps After Deployment

1. **Test Everything**: Run through all features
2. **Update Documentation**: Add your URLs to README
3. **Share with Users**: Send login instructions
4. **Monitor Usage**: Check analytics daily
5. **Gather Feedback**: Improve based on user input
6. **Add Features**: Implement payment, notifications, etc.

---

## 📞 Support Resources

- **Render Docs**: https://render.com/docs
- **Cloudflare Pages**: https://developers.cloudflare.com/pages
- **PostgreSQL**: https://www.postgresql.org/docs
- **FastAPI**: https://fastapi.tiangolo.com

---

## ✅ Deployment Checklist

### Pre-Deployment
- [ ] Run `test_and_verify_system.bat`
- [ ] Test all features locally
- [ ] Commit all changes to GitHub
- [ ] Backup local database (if needed)

### Render Deployment
- [ ] Create PostgreSQL database
- [ ] Deploy backend web service
- [ ] Set environment variables
- [ ] Test API endpoints
- [ ] Verify database connection

### Cloudflare Deployment
- [ ] Update frontend config.js
- [ ] Push changes to GitHub
- [ ] Create Cloudflare Pages project
- [ ] Deploy frontend
- [ ] Test full application

### Post-Deployment
- [ ] Test registration
- [ ] Test login
- [ ] Test session plan creation
- [ ] Test scheme creation
- [ ] Test document downloads
- [ ] Test admin panel
- [ ] Update README with URLs
- [ ] Share with users

---

**🎉 You're Ready to Deploy!**

Start with: `test_and_verify_system.bat`

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
