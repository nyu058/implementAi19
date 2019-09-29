const path = require('path');
const wpMerge = require('webpack-merge');
const common = require('./webpack.config.common.js');

const parentDir = path.join(__dirname, '../');

module.exports = wpMerge(common, {
  mode: 'development',
  devtool: 'eval-source-map',
  devServer: {
    port: 5000,
    host: 'localhost',
    contentBase: parentDir,
    historyApiFallback: true
  }
});
