// API Configuration
// Change this URL when deploying to production
const CONFIG = {
    // Local development
    API_URL: 'http://localhost:5000',
    
    // Production (uncomment and update after deploying backend)
    // API_URL: 'https://rtb-planner-backend.onrender.com',
};

// Export for use in other files
if (typeof module !== 'undefined' && module.exports) {
    module.exports = CONFIG;
}
