# OctoFit Tracker Project Structure Overview

This document provides a high-level explanation of the entire OctoFit Tracker project, including both the backend (Django) and frontend (React) parts. It is designed for beginners to help you understand what each folder and file does and how everything works together.

---

## Top-Level Structure

```
OctoFit_Tracker/
├── LICENSE
├── README.md
├── docs/
│   └── octofit_story.md
├── octofit-tracker/
│   ├── backend/
│   │   ├── db.sqlite3
│   │   ├── manage.py
│   │   ├── requirements.txt
│   │   └── octofit_tracker/
│   │       ├── __init__.py
│   │       ├── asgi.py
│   │       ├── models.py
│   │       ├── settings.py
│   │       ├── urls.py
│   │       ├── wsgi.py
│   │       ├── management/
│   │       │   └── commands/
│   │       │       └── populate_db.py
│   │       └── migrations/
│   │           └── 0001_initial.py
│   └── frontend/
│       └── octofit-frontend/
│           ├── package.json
│           ├── public/
│           └── src/
│               └── components/
│                   ├── Activities.js
│                   ├── Leaderboard.js
│                   ├── Teams.js
│                   ├── Users.js
│                   └── Workouts.js
```

---

## Backend: Django (Python)

### Main Folders and Files
- **backend/**: Contains all backend code and configuration.
  - **db.sqlite3**: The database file (SQLite, used for development).
  - **manage.py**: Command-line utility for Django (runserver, migrations, etc.).
  - **requirements.txt**: Lists Python packages needed for the backend.
  - **octofit_tracker/**: Main Django app folder.
    - **__init__.py**: Marks this as a Python package.
    - **asgi.py, wsgi.py**: Entry points for running the app on web servers.
    - **models.py**: Defines the database models (users, activities, etc.).
    - **settings.py**: Configuration for the Django project (database, apps, etc.).
    - **urls.py**: Maps URLs to views (API endpoints).
    - **management/commands/populate_db.py**: Custom command to populate the database with initial data.
    - **migrations/**: Tracks changes to the database schema.

### How It Works
- Django runs the backend server, handles user authentication, stores data, and provides REST API endpoints for the frontend.
- You interact with the backend using `python manage.py` commands.
- The backend exposes endpoints like `/api/activities/`, `/api/leaderboard/`, etc.

---

## Frontend: React (JavaScript)

### Main Folders and Files
- **frontend/octofit-frontend/**: Contains all frontend code and configuration.
  - **package.json**: Lists dependencies and scripts for the React app.
  - **public/**: Static files (HTML, icons, manifest).
    - **index.html**: Main HTML file where React renders the app.
  - **src/**: All React code.
    - **index.js**: Entry point, renders the app.
    - **App.js**: Main component, sets up navigation and routes.
    - **components/**: Contains React components for each feature:
      - **Activities.js**: Shows activities from the backend.
      - **Leaderboard.js**: Shows leaderboard data.
      - **Teams.js**: Shows teams.
      - **Users.js**: Shows users.
      - **Workouts.js**: Shows workouts.

### How It Works
- The React app fetches data from the Django backend using REST API endpoints.
- Navigation is handled by `react-router-dom` in `App.js`.
- Each component fetches and displays data from its corresponding API endpoint.
- Bootstrap is used for styling.

---

## Other Files
- **LICENSE**: Project license.
- **README.md**: Project overview and instructions.
- **docs/octofit_story.md**: Documentation about the project story and goals.

---

## How Everything Works Together
1. **Backend (Django)** runs the server, manages data, and exposes REST API endpoints.
2. **Frontend (React)** fetches data from these endpoints and displays it to users.
3. You run the backend and frontend servers separately (usually backend on port 8000, frontend on port 3000).
4. The frontend uses URLs like `https://[codespace]-8000.app.github.dev/api/activities/` to get data from the backend.

---

## Quick Reference Table
| Folder/File                        | Purpose                                      |
|------------------------------------|----------------------------------------------|
| backend/                           | All backend (Django) code                    |
| backend/manage.py                  | Django command-line tool                     |
| backend/requirements.txt           | Python dependencies for backend              |
| backend/octofit_tracker/           | Main Django app code                         |
| backend/octofit_tracker/models.py  | Database models                              |
| backend/octofit_tracker/settings.py| Django settings/configuration                 |
| backend/octofit_tracker/urls.py    | URL routing for backend                      |
| backend/octofit_tracker/migrations/| Database schema changes                      |
| frontend/octofit-frontend/         | All frontend (React) code                    |
| frontend/octofit-frontend/package.json | React dependencies and scripts           |
| frontend/octofit-frontend/public/  | Static files for frontend                    |
| frontend/octofit-frontend/src/     | React source code                            |
| frontend/octofit-frontend/src/components/ | Feature components (Activities, etc.) |
| LICENSE                            | Project license                              |
| README.md                          | Project overview                             |
| docs/                              | Additional documentation                     |

---

If you have any questions about a specific file or folder, just ask!
