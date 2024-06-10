const themeToggleBtn = document.getElementById('theme-toggle');
let currentTheme = localStorage.getItem('theme') || 'light';
let currentIcon = localStorage.getItem('icon') || 'fa-moon';
const icon = document.getElementById('icon-theme');

document.documentElement.setAttribute('data-theme', currentTheme);
document.documentElement.setAttribute('icon', currentIcon);

themeToggleBtn.addEventListener('click', () => {
        const newTheme = currentTheme === 'light' ? 'dark' : 'light';
        const newIcon = currentIcon === 'fa-moon' ? 'fa-sun' : 'fa-moon';
        currentIcon = newIcon;
        currentTheme = newTheme;
        document.documentElement.setAttribute('data-theme', newTheme);
        document.documentElement.setAttribute('icon', newIcon);
        localStorage.setItem('theme', newTheme);
        localStorage.setItem('icon', newIcon);

        icon.classList.toggle('fa-moon');
        icon.classList.toggle('fa-sun');
});

function getDate() {
    let date = new Date();

    const format = {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
    };

    return date.toLocaleDateString('en-US', format);
}

function getTime() {
    const date = new Date();

    const format = {
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
    };

    return date.toLocaleTimeString('en-US', format);
}

function update() {
    const date = getDate();
    const time = getTime();
    document.getElementById('date').textContent = date;
    document.getElementById('time').textContent = time;
}

update();
setInterval(update, 1000);
window.onload = function() {
    update();
};