# RTB Document Planner - System Restart Guide

## 🚀 Current System Configuration

### Backend (PythonAnywhere)
- **URL**: https://leonardus437.pythonanywhere.com
- **Status**: Should be running Flask backend
- **Code**: Based on `FINAL_PYTHONANYWHERE_CODE.py`

### Frontend (Cloudflare/Local)
- **Production**: Deployed on Cloudflare
- **Local**: Can run on http://localhost:5173
- **Configuration**: Points to PythonAnywhere backend

### GitHub Repository
- **URL**: https://github.com/Leonardus437/rtb-document-planner
- **Status**: Contains all source code

## 🔧 How to Restart the System

### Option 1: Quick System Check (Recommended)
```bash
# Run this script to check system status
restart_rtb_system.bat
```

This will:
1. ✅ Start local frontend server
2. 🔍 Open system status check page
3. 📊 Test all system components
4. 🚀 Launch app if everything works

### Option 2: Manual Steps

1. **Check Backend Status**
   - Visit: https://leonardus437.pythonanywhere.com
   - Should return: `{"message": "RTB Document Planner API", "status": "online"}`

2. **Start Frontend Locally**
   ```bash
   cd frontend
   python -m http.server 5173
   ```

3. **Open Application**
   - Visit: http://localhost:5173
   - Check browser console for connection status

## 🔍 System Status Checks

### Backend Health Check
- **URL**: https://leonardus437.pythonanywhere.com/
- **Expected**: JSON response with status "online"

### Frontend Configuration
- **Config**: Points to PythonAnywhere backend
- **Auth**: User session management working
- **Wizards**: Session plan and scheme creation available

### Key Endpoints to Test
- `GET /` - Health check
- `POST /users/register` - User registration
- `POST /users/login` - User login
- `GET /user-limits/{phone}` - Download limits

## 🎯 For TSS Teachers

### If System is Working:
1. **Visit**: http://localhost:5173 (or production URL)
2. **Register**: Create new teacher account
3. **Login**: Use your credentials
4. **Create**: Session plans and schemes of work
5. **Download**: Professional RTB-compliant documents

### If System Has Issues:
1. **Run**: `restart_rtb_system.bat`
2. **Check**: System status page
3. **Fix**: Any red status items
4. **Contact**: System administrator if needed

## 📋 Admin Access

### Default Admin Credentials
- **Phone**: +250789751597
- **Password**: admin123
- **Access**: Full user management

### Admin Functions
- View all registered users
- Upgrade users to premium
- System statistics
- User management

## 🔄 Last Working Configuration

The system was last working with:
- **Backend**: Flask on PythonAnywhere
- **Frontend**: Static files on Cloudflare
- **Database**: In-memory (users_db dictionary)
- **Documents**: Generated via backend endpoints

## 🆘 Troubleshooting

### Common Issues:
1. **Backend not responding**: Check PythonAnywhere app status
2. **CORS errors**: Backend should have CORS enabled for all origins
3. **Login fails**: Check if backend `/users/login` endpoint works
4. **Documents not generating**: Backend needs document generation code

### Quick Fixes:
1. **Restart PythonAnywhere app**: Go to PythonAnywhere dashboard
2. **Clear browser cache**: Hard refresh (Ctrl+F5)
3. **Check console**: Look for JavaScript errors
4. **Test endpoints**: Use browser dev tools Network tab

---

**🎓 Ready to serve TSS Teachers across Rwanda!**

The system is designed to help teachers create professional, RTB-compliant session plans and schemes of work quickly and easily.