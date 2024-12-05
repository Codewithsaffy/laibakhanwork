const icon = document.querySelector(".icon");
const btn = document.querySelector(".btn");
function changeColor() {
  let random = Math.floor(Math.random() * 100);
  let random2 = Math.floor(Math.random() * 100);
  let random3 = Math.floor(Math.random() * 100);
  icon.style.color = `rgb(${random}, ${random2}, ${random3})`;
}

btn.addEventListener("click", () => {
  changeColor();
});

