// ===== DOCUMENT READY =====
document.addEventListener('DOMContentLoaded', function() {
    // Initialize animations
    initAnimations();
    initFormValidation();
    initTooltips();
});

// ===== ANIMATIONS =====
function initAnimations() {
    // Auto-dismiss alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });

    // Animate elements on scroll
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.animation = 'slideUp 0.6s ease-out forwards';
                observer.unobserve(entry.target);
            }
        });
    }, { threshold: 0.1 });

    document.querySelectorAll('.card, .account-card, .atm-card').forEach(el => {
        observer.observe(el);
    });
}

// ===== FORM VALIDATION =====
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });

    // Add input animations
    const inputs = document.querySelectorAll('.form-control, .form-select');
    inputs.forEach(input => {
        input.addEventListener('focus', function() {
            this.parentElement.classList.add('focused');
        });
        input.addEventListener('blur', function() {
            this.parentElement.classList.remove('focused');
        });
    });
}

// ===== TOOLTIPS =====
function initTooltips() {
    // Bootstrap tooltips if needed
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function(tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// ===== CURRENCY FORMATTER =====
function formatCurrency(value) {
    return new Intl.NumberFormat('fr-FR', {
        style: 'currency',
        currency: 'EUR'
    }).format(value);
}

// ===== BALANCE UPDATE ANIMATION =====
function animateBalanceUpdate(element, newValue) {
    const oldValue = parseFloat(element.textContent);
    const duration = 1000;
    const start = Date.now();

    function update() {
        const elapsed = Date.now() - start;
        const progress = Math.min(elapsed / duration, 1);
        const current = oldValue + (newValue - oldValue) * progress;
        element.textContent = formatCurrency(current);

        if (progress < 1) {
            requestAnimationFrame(update);
        }
    }

    element.style.animation = 'glow 0.6s ease-out';
    update();
}

// ===== COPY TO CLIPBOARD =====
function copyToClipboard(text, button) {
    navigator.clipboard.writeText(text).then(() => {
        const originalText = button.textContent;
        button.textContent = '✓ Copié !';
        button.style.background = '#10B981';
        
        setTimeout(() => {
            button.textContent = originalText;
            button.style.background = '';
        }, 2000);
    });
}

// ===== PAGE TRANSITION =====
function pageTransition(href) {
    document.body.style.opacity = '0';
    setTimeout(() => {
        window.location.href = href;
    }, 300);
}

// ===== CONFIRM DIALOG =====
function confirmAction(message) {
    return confirm(message);
}

// ===== TOAST NOTIFICATION =====
function showToast(message, type = 'info') {
    const toastHtml = `
        <div class="toast" role="alert" aria-live="assertive">
            <div class="toast-header bg-${type} text-white">
                <strong class="me-auto">${type.toUpperCase()}</strong>
                <button type="button" class="btn-close btn-close-white" data-bs-dismiss="toast"></button>
            </div>
            <div class="toast-body">
                ${message}
            </div>
        </div>
    `;
    
    const toastContainer = document.getElementById('toastContainer') || createToastContainer();
    toastContainer.insertAdjacentHTML('beforeend', toastHtml);
    
    const toastElement = toastContainer.lastElementChild;
    const toast = new bootstrap.Toast(toastElement);
    toast.show();
}

function createToastContainer() {
    const container = document.createElement('div');
    container.id = 'toastContainer';
    container.style.position = 'fixed';
    container.style.top = '20px';
    container.style.right = '20px';
    container.style.zIndex = '9999';
    document.body.appendChild(container);
    return container;
}

// ===== NUMBER INPUT FORMAT =====
document.querySelectorAll('input[type="number"]').forEach(input => {
    input.addEventListener('input', function() {
        const value = parseFloat(this.value);
        if (!isNaN(value)) {
            this.value = value.toFixed(2);
        }
    });
});

// ===== SMOOTH SCROLL =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({
                behavior: 'smooth',
                block: 'start'
            });
        }
    });
});

// ===== PAGE LOAD ANIMATION =====
window.addEventListener('load', function() {
    document.body.style.opacity = '1';
});

// ===== DARK MODE TOGGLE (Optional) =====
function toggleDarkMode() {
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
    const newDarkMode = !isDarkMode;
    localStorage.setItem('darkMode', newDarkMode);
    applyDarkMode(newDarkMode);
}

function applyDarkMode(isDarkMode) {
    const root = document.documentElement;
    if (isDarkMode) {
        root.style.colorScheme = 'dark';
    } else {
        root.style.colorScheme = 'light';
    }
}

// ===== KEYBOARD SHORTCUTS =====
document.addEventListener('keydown', function(e) {
    // Alt + L for login
    if (e.altKey && e.key === 'l') {
        const loginBtn = document.querySelector('a[href*="login"]');
        if (loginBtn) loginBtn.click();
    }
    // Alt + D for dashboard
    if (e.altKey && e.key === 'd') {
        const dashboardBtn = document.querySelector('a[href*="dashboard"]');
        if (dashboardBtn) dashboardBtn.click();
    }
});

// ===== PREVENT DOUBLE SUBMIT =====
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function() {
        const submitBtn = form.querySelector('[type="submit"]');
        if (submitBtn) {
            submitBtn.disabled = true;
            const originalText = submitBtn.textContent;
            submitBtn.textContent = '⏳ Traitement...';
            
            setTimeout(() => {
                if (!form.classList.contains('submitted')) {
                    form.classList.add('submitted');
                }
            }, 1000);
        }
    });
});

console.log('%c🏦 Furie Banque - Frontend Loaded', 'color: #0052CC; font-size: 16px; font-weight: bold;');
