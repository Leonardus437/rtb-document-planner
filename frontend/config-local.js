// RTB Document Planner Configuration - Local Backend Fix
// Bypasses PythonAnywhere CORS issues

const API_BASE = 'http://localhost:5000';

// Connection test function
async function testConnection() {
    try {
        const response = await fetch(`${API_BASE}/`, {
            method: 'GET',
            mode: 'cors',
            credentials: 'omit',
            headers: {
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            }
        });
        
        if (response.ok) {
            const data = await response.json();
            console.log('✅ Local backend connected:', data);
            return true;
        } else {
            console.error('❌ Backend connection failed:', response.status, response.statusText);
            return false;
        }
    } catch (error) {
        console.error('❌ Backend connection error:', error.message);
        return false;
    }
}

// Initialize connection on page load
document.addEventListener('DOMContentLoaded', async () => {
    console.log('🚀 RTB Document Planner Frontend Loaded (Local Backend)');
    console.log('📡 Testing local backend...');
    
    const connected = await testConnection();
    if (!connected) {
        console.warn('⚠️ Local backend not available. Run fix_cors_local.bat');
    }
});

// Export for use in other scripts
window.API_BASE = API_BASE;
window.testConnection = testConnection;