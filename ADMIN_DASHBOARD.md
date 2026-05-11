# 🎯 RTB Admin Dashboard - Complete Guide

## 🚀 Access
**URL**: https://ikidanago.pages.dev/admin-fixed.html

**Credentials**:
- Phone: `+250789751597`
- Password: `admin123`

## ✨ New Features

### 📊 Real-Time Statistics
- **Total Users** - Count of all registered teachers
- **Premium Users** - Count of premium accounts
- **Total Documents** - Session plans + Schemes created
- **Total Downloads** - All document downloads tracked

### 👥 User Management
- **Search Users** - Filter by name, phone, email, or institution
- **View Documents** - See each user's session plans and schemes count
- **Toggle Premium** - Grant or revoke premium access instantly
- **Delete Users** - Remove users (admin accounts protected)
- **Auto-refresh** - Updates every 30 seconds

### 📈 Recent Activity
- **Live Feed** - Last 20 document creations
- **Real-time Updates** - Auto-refreshes every 30 seconds
- **Activity Details** - User, document type, title, and timestamp
- **Time Formatting** - Shows "Just now", "5m ago", "2h ago", etc.

## 🎨 Design Improvements
- Modern gradient background (purple theme)
- Animated stat cards with hover effects
- Tab-based navigation (Users / Activity)
- Responsive design for all devices
- Professional color-coded badges
- Live update indicator with pulse animation

## 🔧 Backend Endpoints

### Statistics
```
GET /stats
Returns: total_users, premium_users, total_session_plans, total_schemes, total_downloads
```

### Recent Activity
```
GET /admin/recent-activity?limit=20
Returns: Array of recent document creations with user info
```

### User Documents
```
GET /admin/user-documents/{phone}
Returns: session_plans count, schemes count, total
```

### Update User
```
PUT /users/{phone}
Body: { is_premium, session_plans_limit, schemes_limit }
```

### Delete User
```
DELETE /users/{phone}
Deletes user (admin accounts protected)
```

## 📱 Features Breakdown

### User Table Columns
1. **Name** - Full name of user
2. **Phone** - Contact number
3. **Email** - Email address
4. **Institution** - School/IPRC name
5. **Status** - Badge showing Admin/Premium/Free
6. **Documents** - Session plans / Schemes count
7. **Actions** - Premium toggle and delete buttons

### Activity Feed
- Icon-coded by document type (green for session plans, purple for schemes)
- Shows document title and creator
- Relative timestamps (just now, minutes, hours, days ago)
- Scrollable list of last 20 activities

## 🔐 Security
- Admin role verification on page load
- Protected admin accounts (cannot be deleted)
- Confirmation dialogs for destructive actions
- Session-based authentication

## 🎯 Usage Tips
1. Use search box to quickly find users
2. Click "Refresh" to manually update data
3. Switch between tabs to view users or activity
4. Premium toggle is instant - no page reload needed
5. Activity feed shows real-time system usage

## 🌟 Auto-Refresh
- Dashboard refreshes every 30 seconds automatically
- Live indicator shows system is updating
- No manual refresh needed for monitoring

---

**Made with ❤️ for TVET Excellence in Rwanda** 🇷🇼
