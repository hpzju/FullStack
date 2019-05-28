const concateArr = (...args) => Array.from(args).flat();

//console.log(concateArr([1, 2, 3], [4, 5, 6], 2, 4, [2, 3, 4, [2, 4]]));

const andAll = (...args) =>
  Array.from(args).every(value => (value ? true : false));

// console.log(andAll(1, 2, 3));
// console.log(andAll(1, 2, 3, 0));
// console.log(andAll(1, 2, 3, ""));
// console.log(andAll(1, 2, 3, undefined));
// console.log(andAll(1, 2, 3, null));
// console.log(andAll(1, 2, 3, NaN));

const orAll = (...args) =>
  Array.from(args).some(value => (value ? true : false));
// console.log(orAll(1, 2, 0));
// console.log(orAll(1, 0, "", undefined, null, NaN));
// console.log(orAll(0, "", undefined, null, NaN));

const selectFalsy = (...args) =>
  Array.from(args).filter(value => (value ? false : true));

// console.log(selectFalsy(1, 0, "", 3, undefined, null, NaN));

const capitalizeStrs = (...args) =>
  Array.from(args).map(str =>
    str
      .trim()
      .split(" ")
      .map(word => word.charAt(0).toUpperCase() + word.slice(1))
      .join(" ")
  );

// console.log(capitalizeStrs("this is a string    ", "   and another string."));
var val;
function func() {
  return 0;
}
var array = [];
var object = {};

const typeofAll = (...args) => Array.from(args).map(elem => typeof elem);

console.log(typeofAll(1, 0, -1, 0.2, NaN));
console.log(typeofAll("", "", " ", "str"));
console.log(typeofAll(true, false, 1, 0, Boolean(1), Boolean(0), Boolean("")));
console.log(typeofAll(val, undefined, "undefined"));
console.log(typeofAll(func, () => {}, typeofAll, Array));
console.log(typeofAll({}, [], array, object, Array, String, this));
