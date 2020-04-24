# Firefly Health Take Home Back-End

This Django project provides the API and model definitions for Clinicians and Availabilities

# Getting started

### 1) Verify that you're using Python version 3.7.7

e.g. `python --version`

### 2) Install this project's requirements

First, create a virtual environment to isolate our package dependencies locally:

```
python -m venv env # You should only have to do this once
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Then,

```
python -m pip install -r requirements.txt
```

### 2) Run migrations

```
python manage.py migrate
```

This will initialize your SQLite database, and also seed it with some sample data for Clinicians and Availabilities.

### 3) Start the server with `python manage.py runserver`

Then, in a browser, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and verify that you see the sample Django start page

Or, try [http://127.0.0.1:8000/clinicians/](http://127.0.0.1:8000/clinicians/) to view the index page for Clinicians.

**Note:** The django admin panel is available at `/admin`

```
username: firefly
password: firefly
```
