// RTB Document Planner - Authentication Helper
// Handles user sessions, login/logout, and authentication checks

// Get current user session
function getCurrentSession() {
    try {
        const session = localStorage.getItem('rtb_session');
        return session ? JSON.parse(session) : null;
    } catch (error) {
        console.error('Error parsing session:', error);
        localStorage.removeItem('rtb_session');
        return null;
    }
}

// Set user session
function setSession(userData) {
    try {
        localStorage.setItem('rtb_session', JSON.stringify(userData));
        return true;
    } catch (error) {
        console.error('Error setting session:', error);
        return false;
    }
}

// Clear user session
function clearSession() {
    localStorage.removeItem('rtb_session');
    sessionStorage.setItem('rtb_logged_out', 'true');
}

// Logout user
function logoutUser() {
    if (confirm('Are you sure you want to logout?')) {
        clearSession();
        window.location.href = 'login-select.html';
    }
}

// Check if user is logged in
function isLoggedIn() {
    return getCurrentSession() !== null;
}

// Check if user is admin
function isAdmin() {
    const session = getCurrentSession();
    return session && session.role === 'admin';
}

// Check if user is premium
function isPremium() {
    const session = getCurrentSession();
    return session && session.is_premium;
}

// Redirect to login if not authenticated
function requireAuth() {
    if (!isLoggedIn()) {
        window.location.href = 'login-select.html';
        return false;
    }
    return true;
}

// Redirect to admin login if not admin
function requireAdmin() {
    const session = getCurrentSession();
    if (!session || session.role !== 'admin') {
        window.location.href = 'login.html?type=admin';
        return false;
    }
    return true;
}

// Get user limits from API
async function fetchUserLimits(phone) {
    try {
        const response = await fetch(`${API_BASE}/user-limits/${encodeURIComponent(phone)}`, {
            method: 'GET',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            return await response.json();
        } else {
            throw new Error(`HTTP ${response.status}: ${response.statusText}`);
        }
    } catch (error) {
        console.error('Error fetching user limits:', error);
        // Return default limits on error
        return {
            session_plans_limit: 2,
            schemes_limit: 2,
            session_plans_downloaded: 0,
            schemes_downloaded: 0,
            is_premium: false,
            session_plans_remaining: 2,
            schemes_remaining: 2
        };
    }
}

// Login function
async function loginUser(phone, password) {
    try {
        const response = await fetch(`${API_BASE}/users/login`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ phone, password })
        });
        
        if (response.ok) {
            const userData = await response.json();
            setSession(userData);
            return { success: true, user: userData };
        } else {
            const error = await response.json();
            return { success: false, error: error.detail || 'Login failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error: ' + error.message };
    }
}

// Register function
async function registerUser(userData) {
    try {
        const response = await fetch(`${API_BASE}/users/register`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(userData)
        });
        
        if (response.ok) {
            const result = await response.json();
            return { success: true, result };
        } else {
            const error = await response.json();
            return { success: false, error: error.detail || 'Registration failed' };
        }
    } catch (error) {
        return { success: false, error: 'Network error: ' + error.message };
    }
}

// Initialize authentication on page load
document.addEventListener('DOMContentLoaded', () => {
    // Clear logout flag if user is on login page
    if (window.location.pathname.includes('login')) {
        sessionStorage.removeItem('rtb_logged_out');
        localStorage.removeItem('rtb_logged_out');
    }
    
    // Check for expired sessions (optional)
    const session = getCurrentSession();
    if (session) {
        console.log('User session active:', session.name, `(${session.role})`);
    }
});

// Export functions for global use
window.getCurrentSession = getCurrentSession;
window.setSession = setSession;
window.clearSession = clearSession;
window.logoutUser = logoutUser;
window.isLoggedIn = isLoggedIn;
window.isAdmin = isAdmin;
window.isPremium = isPremium;
window.requireAuth = requireAuth;
window.requireAdmin = requireAdmin;
window.fetchUserLimits = fetchUserLimits;
window.loginUser = loginUser;
window.registerUser = registerUser;