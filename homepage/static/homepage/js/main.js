// Небольшое клиентское поведение интерфейса каталога.

// Текущий год в подвале страницы.
const yearElement = document.getElementById("current-year");

if (yearElement) {
  yearElement.textContent = new Date().getFullYear();
}

// Подсветка пункта меню текущего раздела.
const currentPath = window.location.pathname;

document.querySelectorAll(".site-nav .nav-link").forEach((link) => {
  const linkPath = link.getAttribute("href");
  const isHome = linkPath === "/" && currentPath === "/";
  const isSection = linkPath !== "/" && currentPath.startsWith(linkPath);

  if (isHome || isSection) {
    link.classList.add("active");
    link.setAttribute("aria-current", "page");
  }
});
