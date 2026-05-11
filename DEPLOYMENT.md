# RTB Document Planner - Online Deployment

## 🚀 Deploy to Cloud Platforms

### Option 1: Render (Recommended)
1. Fork this repository to your GitHub
2. Go to [render.com](https://render.com)
3. Connect your GitHub account
4. Create new Web Service
5. Select this repository
6. Use these settings:
   - **Build Command:** `pip install -r requirements.txt && cd backend && python init_database.py`
   - **Start Command:** `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment:** Python 3.11

### Option 2: Heroku
1. Install Heroku CLI
2. Run these commands:
```bash
git init
git add .
git commit -m "Deploy RTB System"
heroku create your-app-name
git push heroku main
```

### Option 3: Railway
1. Go to [railway.app](https://railway.app)
2. Connect GitHub repository
3. Deploy automatically

## 🌐 Access Your Deployed App
- **Frontend:** Your deployment URL
- **Backend API:** Your deployment URL/docs
- **Admin Login:** +250789751597 / admin123

## ✅ All Features Included:
- ✓ Shield word removal from objectives
- ✓ Tick bullet objectives (✓)
- ✓ 1.5 line spacing throughout
- ✓ Enhanced facilitation techniques
- ✓ Optimized 19-row table structure
- ✓ Professional RTB-compliant documents

## 📱 Mobile Responsive
Works perfectly on all devices - phones, tablets, computers.

## 🔧 Environment Variables (Optional)
Set these in your hosting platform:
- `DATABASE_URL` - For PostgreSQL (production)
- `SECRET_KEY` - For enhanced security

Ready for production use! 🇷🇼