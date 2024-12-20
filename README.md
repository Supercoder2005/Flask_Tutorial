# Flask ORM Model Tutorial

This project demonstrates how to set up and use Flask with SQLAlchemy ORM to interact with a SQLite database. The folder contains all necessary files to get started with creating, managing, and querying database tables using Flask.

## Folder Structure

```
Flask_ORM_Tutorial/
|
|-- instance/
|   |-- mydatabase.sqlite3   # SQLite database file
|
|-- app.py                   # Main Flask application
|-- first.py                 # Script defining ORM models and database creation
|
|-- README.md                # Project documentation (this file)
```

---

## Requirements

Make sure you have the following installed:

- Python 3.6+
- Flask
- Flask-SQLAlchemy

You can install the required dependencies using pip:

```bash
pip install flask flask-sqlalchemy
```

---

## Setting Up the Project

1. **Clone the Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd Flask_ORM_Tutorial
   ```

2. **Run the Application**:
   Execute the following commands in the terminal:
   ```bash
   python
   >>> from app import *
   >>> db.create_all()
   >>> exit()
   ```
   This will create the `mydatabase.sqlite3` file in the `instance` folder.

---

## Files Description

### `app.py`
This is the main Flask application file that initializes Flask and SQLAlchemy:

- Configures the app to use SQLite database.
- Sets up the database URI.
- Creates the `db` object for managing ORM operations.

### `first.py`
Contains the ORM model and script for initializing the database:

- Defines a `User` model with columns `id`, `username`, and `password`.
- Contains the `db.create_all()` function to create the database tables.

### `mydatabase.sqlite3`
The SQLite database file that stores all the tables and data. This is auto-generated after running the database creation commands.

---

## Example Usage

1. **Define Models**: Define your database models in `first.py` or any additional scripts.
2. **Initialize Database**: Run the `db.create_all()` command to generate tables in the database.
3. **Insert Data**:
   ```python
   from app import db
   from first import User

   new_user = User(username='test_user', password='password123')
   db.session.add(new_user)
   db.session.commit()
   ```
4. **Query Data**:
   ```python
   users = User.query.all()
   for user in users:
       print(user.username)
   ```



