// const ranger = (start = 0, end, interval = 1) => {
//   arr = [];
//   for (let i = start; i < end; i += interval) {
//     arr.push(i);
//   }
//   return arr;
// };

const range = n => Array.from(new Array(n).keys());

const rangeRandom = (n, max) => {
  return Array.from(new Array(n).keys()).map(val =>
    Math.ceil(Math.random() * max)
  );
};

const maxElement = arr =>
  arr.reduceRight((acc, cur) => (acc = Math.max(acc, cur)), arr[0]);

const minElement = arr =>
  arr.reduceRight((acc, cur) => (acc = Math.min(acc, cur)), arr[0]);

var arr = range(10);

var a = rangeRandom(10, 100);

// console.log(arr);
// console.log(a);
// console.log(maxElement(a));
// console.log(minElement(a));
// console.log(maxElement([1]));
// console.log(minElement([2]));
