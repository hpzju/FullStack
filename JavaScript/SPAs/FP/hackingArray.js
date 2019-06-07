function vector() {
  let arr = [];
  return {
    get(i) {
      return arr[i];
    },
    store(i, v) {
      arr[i] = v;
    },
    append(v) {
      arr.push(v);
    }
  };
}

let vec = vector();
let arr;

for (i of [3, 5, 6, 6556, 23]) {
  vec.append(i);
}

console.log(vec.get(2));

vec.store("push", function() {
  arr = this;
});

vec.append();

console.log(arr);
