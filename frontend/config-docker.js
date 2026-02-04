// RTB Document Planner Configuration - Docker Local
// For use with Docker containers

const API_BASE = 'http://localhost:8000';

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
            console.log('✅ Docker backend connected:', data);
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
    console.log('🚀 RTB Document Planner Frontend Loaded (Docker)');
    console.log('📡 Testing Docker backend...');
    
    const connected = await testConnection();
    if (!connected) {
        console.warn('⚠️ Backend not available. Please check Docker containers.');
    }
});

// Export for use in other scripts
window.API_BASE = API_BASE;
window.testConnection = testConnection;