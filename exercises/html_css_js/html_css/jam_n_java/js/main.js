// hide preloader
// img, script, link all finished loading

window.addEventListener('load', () => {
  document.querySelector('.preloader').style.display = "none";
});

// nav btn
document.querySelector('.nav_btn').addEventListener('click', () => {
  document.querySelector('.nav_menu').classList.toggle('nav_menu-display');
  document.querySelector('.nav_btn').classList.toggle('nav_btn-close').toggle('');
})