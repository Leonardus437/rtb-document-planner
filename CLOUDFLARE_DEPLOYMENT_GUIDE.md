# 🚀 CLOUDFLARE PAGES DEPLOYMENT - ikidanago.pages.dev

## PART 3: Deploy Frontend on Cloudflare Pages

### Step 1: Access Cloudflare Pages
1. You're already at: https://dash.cloudflare.com
2. In the left sidebar, click **"Workers & Pages"**
3. Click **"Create application"** button
4. Select **"Pages"** tab
5. Click **"Connect to Git"**

### Step 2: Connect GitHub Repository
1. Click **"Connect GitHub"**
2. If prompted, authorize Cloudflare to access GitHub
3. Select **"Leonardus437/rtb-document-planner"** repository
4. Click **"Begin setup"**

### Step 3: Configure Build Settings

**Project name**: `ikidanago` (This will make your URL: ikidanago.pages.dev)

**Production branch**: `main`

**Framework preset**: `None`

**Build command**: (leave empty)

**Build output directory**: `frontend`

### Step 4: Environment Variables
Click **"Add variable"** and add:
- **Variable name**: `NODE_VERSION`
- **Value**: `18`

### Step 5: Deploy
1. Click **"Save and Deploy"**
2. Wait 2-3 minutes for deployment
3. Your site will be live at: **https://ikidanago.pages.dev**

---

## ✅ VERIFICATION STEPS

### Test Your Deployment

1. **Visit**: https://ikidanago.pages.dev
2. **Register** a new account
3. **Login** with your credentials
4. **Create Session Plan**:
   - Upload RTB logo (optional)
   - Upload School logo (optional)
   - Fill in details
   - Generate and download
5. **Create Scheme of Work**:
   - Upload logos (optional)
   - Fill in 3 terms
   - Generate and download
6. **Verify Documents**:
   - Open downloaded DOCX files
   - Check logos appear correctly
   - Verify RTB formatting

---

## 🔧 TROUBLESHOOTING

### If Frontend Can't Connect to Backend

**Option 1: Update Backend URL**
1. Go to your Render dashboard
2. Copy the exact backend URL
3. Update `frontend/config.js`:
```javascript
const CONFIG = {
    API_URL: 'https://YOUR-ACTUAL-RENDER-URL.onrender.com'
};
```
4. Push to GitHub
5. Cloudflare will auto-redeploy

**Option 2: Check CORS**
Backend already has CORS enabled for all origins, so this should work.

### If Render Backend is Sleeping
Free Render services sleep after 15 minutes of inactivity.
- First request takes 30-60 seconds to wake up
- Subsequent requests are fast
- This is normal for free tier

---

## 📋 YOUR LIVE URLS

### Frontend (Cloudflare Pages)
```
https://ikidanago.pages.dev
```

### Backend API (Render)
```
https://rtb-document-planner-api.onrender.com
```

### GitHub Repository
```
https://github.com/Leonardus437/rtb-document-planner
```

---

## 🎯 TEST CREDENTIALS

### Admin Account
- Phone: `+250789751597`
- Password: `admin123`

### Test Teacher
- Phone: `+250789751558`
- Password: `test123`

---

## 🎉 SUCCESS CHECKLIST

- [ ] Render backend deployed and running
- [ ] Cloudflare Pages deployed at ikidanago.pages.dev
- [ ] Can access https://ikidanago.pages.dev
- [ ] Can register new account
- [ ] Can login successfully
- [ ] Can create session plan
- [ ] Can create scheme of work
- [ ] Can upload logos
- [ ] Can download DOCX files
- [ ] Logos appear in documents

---

## 💡 IMPORTANT NOTES

### Free Tier Limitations

**Render (Backend)**:
- Sleeps after 15 minutes inactivity
- First request takes 30-60 seconds
- 750 hours/month free
- Perfect for this project!

**Cloudflare Pages (Frontend)**:
- Unlimited bandwidth
- Unlimited requests
- Always fast
- No sleep time
- Perfect for this project!

### Database
- SQLite database on Render
- Resets when service restarts
- For production, consider PostgreSQL
- Current setup works great for testing!

---

## 🚀 NEXT STEPS

1. **Share the link**: https://ikidanago.pages.dev
2. **Train teachers** on how to use it
3. **Collect feedback** and improve
4. **Monitor usage** via admin dashboard
5. **Celebrate success!** 🎉

---

**Your RTB Document Planner is now LIVE and accessible worldwide!** 🌍

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
