function toggleTheme() {
    const html = document.documentElement;
    const btn = document.getElementById("themeToggleBtn");

    if (html.getAttribute("data-theme") === "dark") {
        html.setAttribute("data-theme", "light");
        btn.innerHTML = "🌙 Dark Mode";
        localStorage.setItem("theme", "light");
    } else {
        html.setAttribute("data-theme", "dark");
        btn.innerHTML = "☀️ Light Mode";
        localStorage.setItem("theme", "dark");
    }
}

// Load saved theme & button text
document.addEventListener("DOMContentLoaded", () => {
    const savedTheme = localStorage.getItem("theme") || "light";
    const btn = document.getElementById("themeToggleBtn");

    document.documentElement.setAttribute("data-theme", savedTheme);

    if (savedTheme === "dark") {
        btn.innerHTML = "☀️ Light Mode";
    } else {
        btn.innerHTML = "🌙 Dark Mode";
    }
});
