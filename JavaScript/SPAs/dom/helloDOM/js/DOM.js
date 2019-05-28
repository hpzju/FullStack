// Document Object

const range = (n, elem = 0) => Array.from(new Array(n).keys()).map(val => elem);

// querySelector select the first matched element, return Node
let count = 0;
const btn = document.querySelector(".btn-success");

btn.addEventListener("click", () => {
  btn.innerHTML = `clicked button: ${++count}`;
});

// querySelectorAll select the all matched element, return NodeList
const btns = document.querySelectorAll(".btn-success");
let counts = range(btns.length, 0);

// console.log(counts);
// console.log(btns);
btns.forEach((elem, index) => {
  elem.addEventListener("click", () => {
    elem.innerHTML = `button-${index + 1}: clicked ${++counts[index]} times.`;
  });
});
