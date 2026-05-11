# 🎓 RTB Document Planner - Complete Setup Guide

Professional TVET Session Plans & Schemes of Work Generator for Rwanda Technical Board (RTB).

## ✨ Features

- ✅ **Session Plans**: Create RTB-compliant session plans with SMART objectives
- ✅ **Schemes of Work**: Generate comprehensive 3-term schemes
- ✅ **Professional DOCX Output**: Download formatted Word documents
- ✅ **User Management**: Registration, login, and subscription system
- ✅ **Admin Panel**: Manage users and view statistics
- ✅ **Download Limits**: Free users get 2 session plans + 2 schemes
- ✅ **Premium Accounts**: Unlimited downloads for premium users

## 🚀 Quick Start (Windows)

### Option 1: Automated Setup (Recommended)

1. **Double-click** `start_rtb_system.bat`
2. Wait for servers to start
3. Browser opens automatically at http://localhost:5173

### Option 2: Manual Setup

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Initialize Database**
   ```bash
   cd backend
   python init_database.py
   ```

3. **Start Backend**
   ```bash
   cd backend
   uvicorn main:app --reload --port 5000
   ```

4. **Start Frontend** (new terminal)
   ```bash
   cd frontend
   python -m http.server 5173
   ```

5. **Open Browser**
   - Navigate to: http://localhost:5173

## 🔐 Default Credentials

### Administrator
- **Phone**: +250789751597
- **Password**: admin123
- **Access**: Admin panel + unlimited downloads

### Teachers
- Register a new account at http://localhost:5173/register.html
- Free accounts get 2 session plans + 2 schemes

## 📁 Project Structure

```
rtb-document-planner-main/
├── backend/
│   ├── main.py                 # FastAPI application
│   ├── models.py               # Database models
│   ├── schemas.py              # Pydantic schemas
│   ├── database.py             # Database configuration
│   ├── document_generator.py   # DOCX generation
│   ├── init_database.py        # Database initialization
│   ├── requirements.txt        # Python dependencies
│   └── rtb_planner.db         # SQLite database (auto-created)
├── frontend/
│   ├── index.html             # Main dashboard
│   ├── wizard.html            # Session plan wizard
│   ├── scheme-wizard.html     # Scheme of work wizard
│   ├── login.html             # Login page
│   ├── register.html          # Registration page
│   ├── admin-fixed.html       # Admin panel
│   ├── config.js              # API configuration
│   └── auth.js                # Authentication logic
└── start_rtb_system.bat       # Automated startup script
```

## 🎯 How to Use

### For Teachers

1. **Register Account**
   - Go to http://localhost:5173/register.html
   - Fill in your details (name, phone, email, institution)
   - Create a password

2. **Login**
   - Use your phone number and password
   - You'll see your dashboard with download limits

3. **Create Session Plan**
   - Click "Session Plan" button
   - Fill in the 4-step wizard:
     - Step 1: Basic Info (sector, trade, level, date)
     - Step 2: Course Details (module, week, class)
     - Step 3: Learning Content (topic, outcomes, activities)
     - Step 4: Review & Generate
   - Click "Generate Session Plan"
   - Download automatically starts

4. **Create Scheme of Work**
   - Click "Scheme of Work" button
   - Fill in the 4-step wizard:
     - Step 1: Institution Info
     - Step 2: Module Details
     - Step 3: Term Content (3 terms)
     - Step 4: Review & Generate
   - Click "Generate Scheme of Work"
   - Download automatically starts

### For Administrators

1. **Login as Admin**
   - Go to http://localhost:5173/login.html?type=admin
   - Use admin credentials

2. **Admin Panel Features**
   - View all registered users
   - See system statistics
   - Upgrade users to premium
   - Monitor downloads

## 🛠️ Technical Details

### Backend (FastAPI)
- **Framework**: FastAPI 0.104.1
- **Database**: SQLite (rtb_planner.db)
- **ORM**: SQLAlchemy 2.0.23
- **Document Generation**: python-docx 1.1.0
- **Port**: 5000

### Frontend
- **HTML5, CSS3, JavaScript**
- **No build process required**
- **Port**: 5173

### API Endpoints

```
GET  /                          # API status
POST /users/register            # User registration
POST /users/login               # User login
GET  /user-limits/{phone}       # Get user download limits
POST /session-plans/            # Create session plan
GET  /session-plans/{id}/download  # Download session plan DOCX
POST /schemes/                  # Create scheme of work
GET  /schemes/{id}/download     # Download scheme DOCX
GET  /users/                    # Get all users (admin)
GET  /stats                     # Get system statistics (admin)
PUT  /users/{id}/premium        # Update premium status (admin)
```

## 📝 Document Formats

### Session Plan Features
- RTB official header with logo placeholders
- 22-row structured table
- SMART objectives auto-generation
- Technique-specific activities (6 methods):
  - Brainstorming
  - Trainer Guided
  - Group Discussion
  - Simulation
  - Experiential Learning
  - Jigsaw
- Professional Bookman Old Style 12pt font
- Proper borders and formatting

### Scheme of Work Features
- Landscape orientation
- 3-term structure
- 9-column table format
- Learning outcomes and indicative contents
- Default activities, resources, and assessment
- Sign-off sections for DOS and Manager

## 🔧 Troubleshooting

### Database Issues
```bash
cd backend
python init_database.py
```

### Port Already in Use
- Backend: Change port in start script (default: 5000)
- Frontend: Change port in start script (default: 5173)

### Module Not Found
```bash
cd backend
pip install -r requirements.txt
```

### CORS Errors
- Ensure backend is running on port 5000
- Check `frontend/config.js` has correct API_BASE

## 📊 Database Schema

### Users Table
- user_id, name, phone, email, institution
- password, role (user/admin)
- is_premium, session_plans_limit, schemes_limit
- session_plans_downloaded, schemes_downloaded

### Session Plans Table
- All form fields from wizard
- sector, trade, module, learning outcomes, etc.

### Schemes of Work Table
- Institution details
- Module information
- 3 terms with learning outcomes and contents

## 🎨 Customization

### Change API URL
Edit `frontend/config.js`:
```javascript
const API_BASE = 'http://localhost:5000';
```

### Modify Download Limits
Edit `backend/init_database.py`:
```python
session_plans_limit=2,  # Change this
schemes_limit=2,        # Change this
```

### Add New Facilitation Techniques
Edit `backend/document_generator.py` in the `generate_session_plan_docx` function.

## 📞 Support

For issues or questions:
1. Check this README
2. Review error messages in browser console (F12)
3. Check backend terminal for API errors

## 🎓 RTB Compliance

This system generates documents that comply with:
- Rwanda Technical Board formatting standards
- TVET session plan requirements
- Scheme of work official templates
- RQF (Rwanda Qualifications Framework) levels

## 📄 License

Developed for TVET Excellence in Rwanda

---

**Ready to start?** Run `start_rtb_system.bat` and begin creating professional RTB documents! 🚀
