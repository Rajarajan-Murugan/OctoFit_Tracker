# OctoFit Tracker Frontend React App Structure

This document explains the purpose of each major file and folder in your React frontend project, and how they work together.

## Project Root: `octofit-frontend/`
This is the main directory for your React app. It contains all the code, configuration, and assets needed for the frontend.

### Key Files and Folders

- **`package.json`**
  - Describes your project, its dependencies (like React, Bootstrap), and scripts (like `start`, `build`).
  - Used by npm to install packages and run commands.

- **`package-lock.json`**
  - Automatically generated. Locks the exact versions of installed packages for consistency.

- **`node_modules/`**
  - Contains all installed npm packages. You don't edit files here.

- **`public/`**
  - Contains static files served directly to the browser.
  - **`index.html`**: The main HTML file. React injects your app here.
  - **`favicon.ico`, `logo192.png`, `logo512.png`**: Icons for your app.
  - **`manifest.json`**: Metadata for Progressive Web Apps (PWAs).
  - **`robots.txt`**: Tells search engines how to crawl your site.

- **`src/`**
  - Contains all your React code (JavaScript, CSS, images, etc.).
  - **`index.js`**: Entry point for your app. Loads React and renders the root component (`App`).
  - **`App.js`**: Main component. Sets up navigation and routes to other components.
  - **`App.css`, `index.css`**: Stylesheets for your app and main component.
  - **`components/`**: Folder for your custom React components:
    - **`Activities.js`**: Fetches and displays activities from the backend API.
    - **`Leaderboard.js`**: Shows the leaderboard from the backend API.
    - **`Teams.js`**: Displays teams from the backend API.
    - **`Users.js`**: Shows users from the backend API.
    - **`Workouts.js`**: Displays workouts from the backend API.
  - **`logo.svg`**: Default React logo (can be replaced).
  - **`App.test.js`, `setupTests.js`**: For automated testing (optional for beginners).
  - **`reportWebVitals.js`**: For measuring app performance (optional).

## How It Works

- When you run `npm start`, React uses `index.js` to render your app into `public/index.html`.
- `App.js` sets up the navigation menu and routes using `react-router-dom`.
- Each component in `components/` fetches data from the backend Django REST API and displays it.
- Bootstrap is used for styling, loaded in `index.js`.
- All dependencies are managed by npm and listed in `package.json`.

## Typical Workflow
1. Edit or add components in `src/components/`.
2. Update navigation in `App.js` if you add new pages.
3. Run `npm start` to see changes live.
4. Use the browser to interact with your app.

## Summary Table
| File/Folder                | Purpose                                                      |
|---------------------------|--------------------------------------------------------------|
| package.json               | Project config, dependencies, scripts                        |
| package-lock.json          | Exact package versions                                       |
| node_modules/              | Installed npm packages                                       |
| public/index.html          | Main HTML file                                               |
| src/index.js               | App entry point, renders React                               |
| src/App.js                 | Main component, navigation, routes                          |
| src/components/            | Custom React components                                      |
| src/App.css, src/index.css | Stylesheets                                                  |
| src/logo.svg               | App logo                                                     |
| src/App.test.js            | Test file (optional)                                         |
| src/reportWebVitals.js     | Performance measurement (optional)                           |
| src/setupTests.js          | Test setup (optional)                                        |

If you have more questions, just ask!
