module.exports = {
  entry: './src/main.js',
  output: {
    path: __dirname + '/../saite/static',
    filename: './main.bundle.js'
  },
  module: {
    rules: [
      //{ test: /\.js$/, use: ['babel-loader'], exclude: /node_modules/ },
      { test: /\.scss$/, use: ['style-loader', 'css-loader', 'sass-loader'] }
    ]
  }
}