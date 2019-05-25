let a = [];
let b = {};

console.log(
  [a, b, a[0], b[0]].forEach(e =>
    e ? console.log("true") : console.log("false")
  )
);

b = { name: "name" };

console.log(b, b[0]);
