const path = require("path");

module.exports = {
  mode: "development", // "production" | "development" | "none"
  entry: "./src/js/index.js", // string | object | array
  output: {
    path: path.resolve(__dirname, "dist"), // string
    filename: "bundle.js" // string
  }
};
