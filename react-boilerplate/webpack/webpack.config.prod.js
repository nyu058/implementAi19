const path = require('path');
const webpack = require('webpack');
const wpMerge = require('webpack-merge');
const common = require('./webpack.config.common.js');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const CompressionPlugin = require('compression-webpack-plugin');

const parentDir = path.join(__dirname, '../');

module.exports = wpMerge(common, {
  mode: 'production',
  plugins: [
    new webpack.optimize.AggressiveMergingPlugin(),
    new webpack.optimize.OccurrenceOrderPlugin(),
    new HtmlWebpackPlugin({
      inject: false,
      template: './index.html',
      favicon: './favicon.ico'
    }),
    new CompressionPlugin({
      asset: '[path].gz[query]',
      algorithm: 'gzip',
      test: /\.js$|\.jsx$|\.css$|\.html$/,
      threshold: 10240,
      minRatio: 0.8
    })
  ],
  performance: {
    maxAssetSize: 512000,
    maxEntrypointSize: 512000
  },
  devServer: {
    port: process.env.PORT || 5000,
    compress: true,
    contentBase: parentDir,
    historyApiFallback: true
  }
});
