# 🔧 INITIALIZE RENDER DATABASE

## ⚡ Quick Fix for Admin Login

The admin account doesn't exist in Render's database yet. Initialize it now!

### Step 1: Call Initialization Endpoint

Open this URL in your browser:

```
https://rtb-document-planner-api.onrender.com/init-production-db?secret_key=RTB2024INIT
```

### Step 2: Wait for Response

You'll see:
```json
{
  "message": "Production database initialized successfully!",
  "admin_created": true,
  "demo_teachers_created": 5,
  "admin_credentials": {
    "phone": "+250789751597",
    "password": "admin123"
  }
}
```

### Step 3: Login Now!

Go to: https://ikidanago.pages.dev

**Admin Login**:
- Phone: +250789751597
- Password: admin123

**Demo Teacher**:
- Phone: +250788123456
- Password: teacher123

---

## ✅ DONE!

Your Render database is now initialized with:
- ✅ 1 Admin account
- ✅ 5 Demo teacher accounts
- ✅ Ready for production!

---

**Note**: This endpoint can only be called once. After initialization, it will return "Database already initialized".
