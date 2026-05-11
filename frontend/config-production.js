// API Configuration for Production
// This file will be used when deployed to Cloudflare Pages
const CONFIG = {
    // Production API URL (Render backend)
    API_URL: 'https://rtb-planner-backend.onrender.com',
    
    // Fallback to local if needed
    // API_URL: 'http://localhost:5000',
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
