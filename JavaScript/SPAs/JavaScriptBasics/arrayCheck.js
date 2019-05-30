const a = [1, 3, 5, "sdfj", 8];
const b = [1, 3, 5, 8];
const c = [8, 6, 4, 2];
const d = [1, 3, 5, 9, 8];
const e = [1, 3, 5, 9, 8];

const arrayCheck = arr => {
  if (arr.some(e => typeof e !== "number")) {
    return `${arr}: has non-number element.`;
  }
  if (
    arr.every((elem, index, arr) => (index > 0 ? elem >= arr[index - 1] : true))
  ) {
    return `${arr}: is sorted by ascending order.`;
  }
  if (
    arr.every((elem, index, arr) => (index > 0 ? elem <= arr[index - 1] : true))
  ) {
    return `${arr}: is sorted by descending order.`;
  }
  return `${arr}: is not sorted.`;
};

const arraysEqualityCheck = (a1, a2) =>
  a1.length === a2.length && a2.every((elem, index) => elem === a1[index]);

const checker = arr => console.log(arrayCheck(arr));

((...arrs) => arrs.map(checker))(a, b, c, d);

console.log(arraysEqualityCheck(d, e));
console.log(arraysEqualityCheck(d, c));
