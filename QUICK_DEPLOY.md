# ⚡ QUICK DEPLOYMENT REFERENCE

## 🎯 YOUR MISSION: Get to ikidanago.pages.dev

---

## STEP 1: RENDER (Backend) ⏱️ 10 minutes

1. Go to: **https://render.com**
2. Sign in with GitHub
3. Click **"New +"** → **"Web Service"**
4. Select: **Leonardus437/rtb-document-planner**
5. Settings:
   - Name: `rtb-document-planner-api`
   - Build: `pip install -r backend/requirements.txt`
   - Start: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Add env: `PYTHON_VERSION` = `3.11.0`
6. Click **"Create Web Service"**
7. ✅ Wait for deployment (5-10 min)
8. 📋 Copy URL: `https://rtb-document-planner-api.onrender.com`

---

## STEP 2: CLOUDFLARE PAGES (Frontend) ⏱️ 5 minutes

1. Go to: **https://dash.cloudflare.com**
2. Click **"Workers & Pages"** (left sidebar)
3. Click **"Create application"**
4. Select **"Pages"** tab
5. Click **"Connect to Git"**
6. Select: **Leonardus437/rtb-document-planner**
7. Settings:
   - Project name: `ikidanago`
   - Branch: `main`
   - Build output: `frontend`
8. Click **"Save and Deploy"**
9. ✅ Wait for deployment (2-3 min)
10. 🎉 Live at: **https://ikidanago.pages.dev**

---

## STEP 3: TEST ⏱️ 2 minutes

1. Visit: **https://ikidanago.pages.dev**
2. Click **"Register"**
3. Create account
4. Login
5. Create a Session Plan or Scheme
6. Upload logos (optional)
7. Download DOCX
8. ✅ SUCCESS!

---

## 🆘 IF SOMETHING GOES WRONG

### Backend not responding?
- Wait 60 seconds (free tier wakes up)
- Check Render logs
- Verify build succeeded

### Frontend can't connect?
- Check `frontend/config.js` has correct Render URL
- Push changes to GitHub
- Cloudflare auto-redeploys

### Still stuck?
- Check: **CLOUDFLARE_DEPLOYMENT_GUIDE.md**
- Or: **DEPLOYMENT_SUCCESS.md**

---

## 📱 SHARE WITH TEACHERS

**Your Live System**: https://ikidanago.pages.dev

**Features**:
- ✅ Create Session Plans (6 techniques)
- ✅ Create Schemes of Work (3 terms)
- ✅ Upload RTB & School logos
- ✅ Download professional DOCX
- ✅ 90% time savings!

---

## 🎉 YOU'RE DONE!

Total time: **15-20 minutes**

Your RTB Document Planner is now:
- ✅ Live online
- ✅ Accessible worldwide
- ✅ Ready for teachers
- ✅ Saving time and effort!

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
