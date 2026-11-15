const button = document.querySelector('.menu-btn');
const menu = document.querySelector('.mobile-nav');
if (button && menu) {
  button.addEventListener('click', () => {
    const opened = menu.classList.toggle('open');
    button.setAttribute('aria-expanded', String(opened));
    button.textContent = opened ? 'Fermer' : 'Menu';
  });
  menu.querySelectorAll('a').forEach(link => link.addEventListener('click', () => {
    menu.classList.remove('open');
    button.setAttribute('aria-expanded', 'false');
    button.textContent = 'Menu';
  }));
}
