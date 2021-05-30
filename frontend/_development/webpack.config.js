var WebpackNotifierPlugin = require("webpack-notifier");

module.exports = {
  mode: "development",
  entry: {
    styles: "./src/scss/main.scss",
  },
  output: {
    path: __dirname + "/../src/assets/minify",
  },
  plugins: [new WebpackNotifierPlugin()],
  externals: {
    // require("jquery") is external and available
    //  on the global var jQuery
    jquery: "jQuery",
  },
  module: {
    rules: [
      {
        test: /\.s[ac]ss$/i,
        use: [
          {
            loader: "file-loader",
            options: {
              name: "css/[name].css",
            },
          },
          {
            loader: "extract-loader",
          },
          {
            loader: "css-loader?-url",
          },
          {
            loader: "postcss-loader",
          },
          {
            loader: "sass-loader",
          },
        ],
      },
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
          options: {
            presets: ["@babel/preset-env"],
          },
        },
      },
    ],
  },
};
