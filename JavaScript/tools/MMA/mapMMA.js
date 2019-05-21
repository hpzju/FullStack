// map function acting like mathematica map[]

function mapObject(obj, fn) {
  return Object.keys(obj).reduce((res, key) => {
    res[key] = fn(obj[key]);
    return res;
  }, {});
}

function deepMap(obj, fn) {
  const deepMapper = val =>
    typeof val === "object" ? deepMap(val, fn) : fn(val);
  if (Array.isArray(obj)) {
    return obj.map(deepMapper);
  }
  if (typeof obj === "object") {
    return mapObject(obj, deepMapper);
  }
  return obj;
}

const map = (func, array, level = 1) => {
  array.map(func);
};

const adder1 = e => (typeof e === "number" ? e + 1 : e);

const arr = [1, 2, 3, 4, 5, [34]];

console.log(map(adder1, arr));
