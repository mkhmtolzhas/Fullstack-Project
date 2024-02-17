// Получаем ссылки на элементы
var modal = document.getElementById("myModal");
var content = document.getElementById("close-login")
var btn = document.getElementById("openModalBtn");
var span = document.getElementsByClassName("close")[0];

// Когда пользователь кликает на кнопку, открываем модальное окно
btn.onclick = function() {
  console.log("Button clicked");
  modal.style.display = "block";
}

// Когда пользователь кликает на крестик, закрываем модальное окно
span.onclick = function() {
  modal.style.display = "none";
}

// Когда пользователь кликает за пределами модального окна, закрываем его
window.onclick = function(event) {
  if (event.target == content) {
    modal.style.display = "none";
  }
}
