const str = "this is a long string with limited length display.";

const limit = 20;

console.log(str.substr(0, limit));
index = str.substr(0, limit).lastIndexOf(" ");
console.log(index);
console.log(str.substr(0, index));
