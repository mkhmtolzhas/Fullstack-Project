// Получаем все якорные ссылки
const links = document.querySelectorAll('a[href^="#"]');

// Прокручиваем к якорю с плавной анимацией при клике на ссылку
links.forEach(link => {
    link.addEventListener('click', function(e) {
        e.preventDefault();

        const targetId = this.getAttribute('href').slice(1);
        const targetElement = document.getElementById(targetId);
        const topOffset = targetElement.offsetTop;

        window.scrollTo({
            top: topOffset,
            behavior: 'smooth'
        });
    });
});
