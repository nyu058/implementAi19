# react-boilerplate

<div align="center">
  <img src="favicon.ico" alt="react boilerplate banner"/>
  <br>
  <!-- Version -->
  <a href="https://github.com/theGirrafish/react-boilerplate/releases">
    <img src="https://img.shields.io/github/release/theGirrafish/react-boilerplate.svg" alt="Github Version"/>
  </a>
  <!-- Build Status -->
  <a href="https://travis-ci.com/theGirrafish/react-boilerplate">
    <img src="https://travis-ci.com/theGirrafish/react-boilerplate.svg?branch=master" alt="Build Status"/>
  </a>
  <!-- License -->
  <a href="https://github.com/theGirrafish/react-boilerplate/blob/master/LICENSE">
    <img src="https://img.shields.io/github/license/theGirrafish/react-boilerplate.svg" alt="Github License"/>
  </a>
</div>

A simple yet scalable boilerplate for your React projects with integrated CI, testing, linting and ready for deployment. Headache free and focused on quick development.

Features
========

- Write modern JavaScript without worrying about unsupported syntax thanks to ES6+ to ES5 transpilation.
- Have access to your arrow functions, destructuring, template strings and JSX syntax all while keeping your code as clean as ever thanks to ESLinting for React.
- Never worry about rebuilding when you code with live reloading from webpack-dev-server.
- Bundling and minification ready for static assets and JS/JSX files under `src`.
- There's a script for every environment, from development to production to deployment.
- Integrated Travis CI with linting, testing and deployment to Heroku.

Quick Start
===========

**Requires Node.js v11.1.0 and npm v6.4.1 or above installed.**

1. Clone this repository using `git clone git@github.com:theGirrafish/react-boilerplate.git <Your Project Name>`.
2. Run `cd <Your Project Name>` to move into your new directory.
3. Run `npm install` to install dependencies.
4. You can now run `npm run dev` to see the app on `http://localhost:5000`.

Extra Setup
-----------

- You can modify the `package.json` file to match your personal information/project. The following fields should be changed:
  - `name`, `description`, `author`, `repository.url`, `bugs.url`, `homepage`
- If using Travis CI to deploy your code to Heroku, you should modify the `deploy` field in the `.travis.yml` file to reflect your Heroku app's information.
- Currently, all linting issues are set to the warning level. You can specify which rules should be considered as an error by changing the `1` to `2` in the `.eslintrc` file.

Usage
=====

- All JavaScript and React code should be written under the `src/components/` folder while the static assets should be stored under `src/assets/`.
- Available commands:

  - `npm run dev`: Run a development version of the code on `http://localhost:5000` using `webpack-dev-server`. Includes live reloading and source map.
  - `npm run prod`: Run a production ready version of the code on `http://localhost:5000` using `webpack-dev-server`. Includes live reloading.
  - `npm run build`: Build and minify all files in `src/` folder for production use and store in `dist/` folder.
  - `npm run start`: Serve files in `dist/` using `express.js`. Defaults to `http://localhost:5000` if no port is specified.
  - `npm run lint`: Run linting on all `.js` and `.jsx` files under the `src/` and `webpack/` folders.
  - `npm run test`: Run Jest tests againsts the `test/` folder.
  - `npm run test:watch`: Run Jest tests againsts the `test/` folder and watches for code changes.
