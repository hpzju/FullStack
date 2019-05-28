const range = n => Array.from(new Array(n).keys());

const rangeRandom = (n, max) => {
  return Array.from(new Array(n).keys()).map(val =>
    Math.ceil(Math.random() * max)
  );
};

const max = 1000000;
let arr;

console.time(`timing range(${max}):`);
arr = range(max);
console.log(`arr[500000] = ${arr[500000]}`);

console.timeEnd(`timing range(${max}):`);

console.time(`timing rangeRandom(${max}, ${max}):`);
arr = rangeRandom(max, max);
console.log(`arr[500000] = ${arr[500000]}`);
console.timeEnd(`timing rangeRandom(${max}, ${max}):`);
