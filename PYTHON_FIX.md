# 🔧 PYTHON INSTALLATION FIX

## ❌ Problem: "pip is not recognized"

This means Python is either:
1. Not installed
2. Not added to system PATH

---

## ✅ SOLUTION

### Option 1: Install Python (Recommended)

1. **Download Python**
   - Go to: https://www.python.org/downloads/
   - Download Python 3.11 or 3.12 (latest stable)

2. **Install Python**
   - Run the installer
   - ⚠️ **IMPORTANT**: Check ☑️ "Add Python to PATH"
   - Click "Install Now"
   - Wait for installation to complete

3. **Verify Installation**
   - Double-click: `check_python.bat`
   - Should show Python version

4. **Install RTB System**
   - Double-click: `install.bat`
   - Should work now!

---

### Option 2: Add Python to PATH (If Already Installed)

1. **Find Python Location**
   - Open File Explorer
   - Common locations:
     - `C:\Users\YourName\AppData\Local\Programs\Python\Python311`
     - `C:\Python311`
     - `C:\Program Files\Python311`

2. **Add to PATH**
   - Right-click "This PC" → Properties
   - Click "Advanced system settings"
   - Click "Environment Variables"
   - Under "System variables", find "Path"
   - Click "Edit"
   - Click "New"
   - Add Python path (e.g., `C:\Python311`)
   - Add Scripts path (e.g., `C:\Python311\Scripts`)
   - Click OK on all windows

3. **Restart Command Prompt**
   - Close all command prompt windows
   - Open new command prompt
   - Type: `python --version`
   - Should show version

4. **Install RTB System**
   - Double-click: `install.bat`

---

### Option 3: Manual Installation (Advanced)

If you have Python but scripts don't work:

```bash
# Open Command Prompt in project folder
cd backend

# Install dependencies manually
python -m pip install fastapi==0.104.1
python -m pip install uvicorn[standard]==0.24.0
python -m pip install sqlalchemy==2.0.23
python -m pip install pydantic==2.5.0
python -m pip install python-multipart==0.0.6
python -m pip install python-docx==1.1.0
python -m pip install lxml==4.9.3

# Initialize database
python init_database.py

# Start backend
python -m uvicorn main:app --reload --port 5000
```

In another Command Prompt:
```bash
cd frontend
python -m http.server 5173
```

---

## 🧪 TEST YOUR SETUP

Run these commands in Command Prompt:

```bash
# Check Python
python --version

# Check pip
python -m pip --version

# Check if you're in the right folder
dir
```

You should see:
- Python version (e.g., Python 3.11.5)
- pip version (e.g., pip 23.2.1)
- backend/ and frontend/ folders

---

## 📞 QUICK CHECKLIST

Before running install.bat:
- [ ] Python 3.8+ installed
- [ ] "Add to PATH" was checked during install
- [ ] Command Prompt restarted
- [ ] `python --version` works
- [ ] `python -m pip --version` works

---

## 🎯 AFTER PYTHON IS INSTALLED

1. Run: `check_python.bat` (verify Python works)
2. Run: `install.bat` (install dependencies)
3. Run: `start_rtb_system.bat` (start system)
4. Open: http://localhost:5173

---

## 💡 COMMON ISSUES

### "python is not recognized"
- Python not installed or not in PATH
- Solution: Reinstall Python with "Add to PATH" checked

### "No module named 'pip'"
- pip not installed
- Solution: `python -m ensurepip --upgrade`

### "Access denied"
- Running as non-admin
- Solution: Right-click Command Prompt → "Run as administrator"

### Port already in use
- Another app using port 5000 or 5173
- Solution: Close other apps or change ports in start script

---

## 🆘 STILL NOT WORKING?

Try this minimal test:

1. Open Command Prompt
2. Type: `python`
3. You should see Python prompt: `>>>`
4. Type: `exit()`

If step 2 fails, Python is not installed correctly.

---

**Need Python?** → https://www.python.org/downloads/

**After installing Python, run:** `install.bat`
