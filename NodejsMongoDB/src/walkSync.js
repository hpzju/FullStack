const dirTree = require("directory-tree");
var jmespath = require("jmespath");

const directory = `C:\\Codes\\Websites\\kb.knoconida.com\\docs`;
const outputFilename = "docsDir.json";
const tree = dirTree(directory);

console.log(JSON.stringify(tree, null, 2));
