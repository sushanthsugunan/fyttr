// ===== THEME TOGGLE =====
const themeToggle = document.getElementById('themeToggle');
const body = document.body;

// Load saved theme
const savedTheme = localStorage.getItem('theme') || 'light';
if (savedTheme === 'dark') {
    body.classList.add('dark-theme');
    themeToggle.textContent = '☀️';
} else {
    themeToggle.textContent = '🌙';
}

// Toggle theme
themeToggle.addEventListener('click', () => {
    body.classList.toggle('dark-theme');
    const isDark = body.classList.contains('dark-theme');
    localStorage.setItem('theme', isDark ? 'dark' : 'light');
    themeToggle.textContent = isDark ? '☀️' : '🌙';
});

// ===== TAB SWITCHING =====
function switchTab(tabName) {
    // Hide all tab contents
    const tabContents = document.querySelectorAll('.tab-content');
    tabContents.forEach(tab => tab.classList.remove('active'));

    // Deactivate all tab buttons
    const tabBtns = document.querySelectorAll('.tab-btn');
    tabBtns.forEach(btn => btn.classList.remove('active'));

    // Show selected tab
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.add('active');
    }

    // Activate corresponding button
    const correspondingBtn = document.querySelector(`.tab-btn[data-tab="${tabName}"]`);
    if (correspondingBtn) {
        correspondingBtn.classList.add('active');
    }

    // Scroll to top
    window.scrollTo(0, 0);
}

// Tab button click handlers
document.querySelectorAll('.tab-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        const tabName = btn.getAttribute('data-tab');
        switchTab(tabName);
    });
});

// ===== FORM VALIDATION & SUBMISSION =====
document.querySelectorAll('.registration-form').forEach(form => {
    form.addEventListener('submit', function(e) {
        // Optional: Add custom validation here
        console.log('Form submitted');
    });
});

// ===== SMOOTH SCROLL FOR ANCHOR LINKS =====
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        const href = this.getAttribute('href');
        if (href !== '#' && document.querySelector(href)) {
            e.preventDefault();
            // Scroll behavior is handled by CSS scroll-behavior: smooth
        }
    });
});

// ===== INITIAL SETUP =====
console.log('Fitness website loaded successfully');