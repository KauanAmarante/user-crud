# Flask User Management API

A lightweight RESTful API built with Python and Flask to manage users.

## 🛠️ Tech Stack
* **Language:** Python 3.11+
* **Framework:** Flask
* **Database:** SQLite (SQLAlchemy ORM)
* **Testing:** Pytest
* **Environment Management:** Pyenv + Virtualenv

## 📂 Project Structure
```text
.
├── app/
│   ├── __init__.py      # Application Factory
│   ├── models.py        # Database Schemas
│   ├── routes.py        # API Endpoints & Validation
│   └── repository.py    # Data Access Logic
├── tests/
│   └── test_app.py      # Unit & Integration Tests
├── run.py               # Entry point
├── requirements.txt     # Project Dependencies
└── README.md            