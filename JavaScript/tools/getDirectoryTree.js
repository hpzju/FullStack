const dirTree = require("directory-tree");
const tree = dirTree("../../JavaScript", { exclude: /node_modules/ });

//console.log(JSON.stringify(tree));

const root = tree.name;
var indent = 0;
console.log(root);

const dirL1 = tree.children.map(items => items.name);

const dirs = tree.children.map;

console.log(dirL1);
