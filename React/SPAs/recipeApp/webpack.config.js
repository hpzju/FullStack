const path = require("path");
const HTMLWebpackPlugin = require("html-webpack-plugin");

module.exports = {
  entry: "./src/js/index.js", // string | object | array
  output: {
    path: path.resolve(__dirname, "dist"), // string
    filename: "js/bundle.js" // string
  },
  devServer: {
    contentBase: path.resolve(__dirname, "dist"),
    port: 9999
  },
  plugins: [
    new HTMLWebpackPlugin({
      filename: "index.html",
      template: path.resolve(__dirname, "src/index.html")
    })
  ]
};
