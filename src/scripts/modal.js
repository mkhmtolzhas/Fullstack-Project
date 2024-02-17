// Получаем ссылку на модальное окно
var modal = document.getElementById("myModal");

// Получаем ссылку на элемент закрытия модального окна (крестик)
var closeButton = document.querySelector(".close");

// Получаем ссылку на блок с содержимым модального окна
var modalContent = document.querySelector(".modal-content");

// Функция для открытия модального окна
function openModal() {
    modal.style.display = "block";
}

// Функция для закрытия модального окна
function closeModal() {
    modal.style.display = "none";
}

// Открываем модальное окно при клике на кнопку
document.getElementById("openModalBtn").addEventListener("click", openModal);

window.onclick = function(event) {
    if (event.target == modalContent) {
        closeModal();
    }
};
// Закрываем модальное окно при клике на крестик
// closeButton.onclick = function() {
//     closeModal();
// };

// Закрываем модальное окно при клике вне его области
