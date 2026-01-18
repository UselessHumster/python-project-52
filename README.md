### Hexlet tests and linter status:
[![Actions Status](https://github.com/UselessHumster/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/UselessHumster/python-project-52/actions)

# Task Manager

Task Manager is a simple and powerful web application for managing tasks, inspired by services like Asana and GitHub Issues.

The application allows you to:

- Register and authenticate users
- Create and manage tasks
- Assign executors and statuses to tasks
- Use labels to categorize tasks
- Filter tasks by status, executor, labels and author
- Track errors in production using Rollbar

---

## 🚀 Live Demo

👉 https://task-manager-t9m4.onrender.com

---

## 🧰 Tech Stack

- Python 3.10+
- Django
- PostgreSQL
- Bootstrap 5
- Gunicorn
- Rollbar
- django-filter
- uv

---

## ⚙️ Features

- User registration and authentication
- CRUD for:
  - Users
  - Statuses
  - Tasks
  - Labels
- Task filtering:
  - by status
  - by executor
  - by label
  - only own tasks
- Permissions:
  - Only task author can delete a task
  - Users cannot be deleted if they are used in tasks
  - Statuses cannot be deleted if they are used in tasks
  - Labels cannot be deleted if they are used in tasks
- Flash messages
- Error tracking with Rollbar
- Fully covered with tests

---

## 🛠 Installation (Local)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/python-project-52.git
cd python-project-52
```

### 2. Install dependencies

```bash
make install
```

### 3. Create .env file

```bash
cp .env.example .env

Or create .env manually:

DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
ROLLBAR_ACCESS_TOKEN=
```

⸻

### 4. Apply migrations
```bash
make migrate
```


⸻

### 5. Run development server
```bash
make dev
```

Open in browser:

http://127.0.0.1:8000/

⸻

### 🧪 Run tests

```bash
make test
```

⸻

### 🏗 Production

The project is ready to be deployed to PaaS platforms like Render.

It uses:
	•	Gunicorn
	•	PostgreSQL via DATABASE_URL
	•	WhiteNoise / static collection
	•	Environment variables for configuration
	•	Rollbar for error tracking

⸻

### 📦 Environment variables

Variable	Description
DEBUG	Enable/disable debug mode
SECRET_KEY	Django secret key
DATABASE_URL	Database connection string
ALLOWED_HOSTS	Allowed hosts
ROLLBAR_ACCESS_TOKEN	Rollbar project token
