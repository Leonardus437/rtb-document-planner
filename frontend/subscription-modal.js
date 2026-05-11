// RTB Document Planner - Subscription Modal
// Shows upgrade options when users reach download limits

function showSubscriptionModal(type = 'general') {
    // Remove existing modal if any
    const existingModal = document.getElementById('subscriptionModal');
    if (existingModal) {
        existingModal.remove();
    }
    
    const session = getCurrentSession();
    const userName = session ? session.name : 'Teacher';
    
    let title, message, benefits;
    
    if (type === 'session_plans') {
        title = 'Session Plan Limit Reached';
        message = 'You\'ve used all your free session plan downloads.';
        benefits = [
            'Unlimited session plan downloads',
            'Unlimited scheme of work downloads', 
            'Priority support',
            'Advanced document features'
        ];
    } else if (type === 'schemes') {
        title = 'Scheme of Work Limit Reached';
        message = 'You\'ve used all your free scheme downloads.';
        benefits = [
            'Unlimited scheme of work downloads',
            'Unlimited session plan downloads',
            'Priority support', 
            'Advanced document features'
        ];
    } else {
        title = 'Upgrade to Premium';
        message = 'Get unlimited access to all RTB Document Planner features.';
        benefits = [
            'Unlimited session plans',
            'Unlimited schemes of work',
            'Priority support',
            'Advanced features',
            'No download limits'
        ];
    }
    
    const modalHTML = `
        <div id="subscriptionModal" class="subscription-modal-overlay">
            <div class="subscription-modal">
                <div class="modal-header">
                    <h2><i class="fas fa-crown"></i> ${title}</h2>
                    <button class="close-btn" onclick="closeSubscriptionModal()">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
                
                <div class="modal-body">
                    <div class="limit-message">
                        <i class="fas fa-exclamation-triangle"></i>
                        <p>Hello ${userName}!</p>
                        <p>${message}</p>
                    </div>
                    
                    <div class="upgrade-section">
                        <h3><i class="fas fa-star"></i> Upgrade to Premium</h3>
                        <div class="benefits-list">
                            ${benefits.map(benefit => `
                                <div class="benefit-item">
                                    <i class="fas fa-check"></i>
                                    <span>${benefit}</span>
                                </div>
                            `).join('')}
                        </div>
                    </div>
                    
                    <div class="contact-section">
                        <h4><i class="fas fa-phone"></i> How to Upgrade</h4>
                        <p>Contact your system administrator to upgrade your account to premium.</p>
                        <div class="contact-info">
                            <p><strong>Admin Phone:</strong> +250789751597</p>
                            <p><strong>Email:</strong> admin@rtb.rw</p>
                        </div>
                    </div>
                </div>
                
                <div class="modal-footer">
                    <button onclick="closeSubscriptionModal()" class="btn-secondary">
                        <i class="fas fa-times"></i> Close
                    </button>
                    <button onclick="contactAdmin()" class="btn-primary">
                        <i class="fas fa-phone"></i> Contact Admin
                    </button>
                </div>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', modalHTML);
    
    // Add event listeners
    document.getElementById('subscriptionModal').addEventListener('click', (e) => {
        if (e.target.id === 'subscriptionModal') {
            closeSubscriptionModal();
        }
    });
    
    // Add escape key listener
    document.addEventListener('keydown', handleEscapeKey);
}

function closeSubscriptionModal() {
    const modal = document.getElementById('subscriptionModal');
    if (modal) {
        modal.remove();
    }
    document.removeEventListener('keydown', handleEscapeKey);
}

function handleEscapeKey(e) {
    if (e.key === 'Escape') {
        closeSubscriptionModal();
    }
}

function contactAdmin() {
    // Try to open phone dialer
    window.open('tel:+250789751597', '_self');
    closeSubscriptionModal();
}

// Export for global use
window.showSubscriptionModal = showSubscriptionModal;
window.closeSubscriptionModal = closeSubscriptionModal;