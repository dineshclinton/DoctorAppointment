# Back-end setup

This Django project provides the API and model definitions for Clinicians and Availabilities.

## Set up your local environment

You can do this with or without [Docker](https://docs.docker.com/).

### Option 1: Without Docker

#### 1) Verify that you're using Python version 3.7.7

e.g. `python --version`

#### 2) Install this project's requirements

First, create a virtual environment to isolate our package dependencies locally:

```
python -m venv env # You should only have to do this once
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

Then install requirements with,

```
python -m pip install -r requirements.txt
```

### Option 2: Docker based setup

Use the provided Dockerfile with 
either

```sh
docker build -t takehome . 
docker run -t -p 8000:8000 takehome
```

or with docker-compose (see [docker-compose.yaml](/backend/docker-compose.yaml))

```sh
docker-compose build
docker-compose up -d
```

## Run migrations

```
python manage.py migrate
```

This will initialize your SQLite database, and also seed it with some sample data for Clinicians and Availabilities.

## Start the server

```
python manage.py runserver
```

This should start the Django server on port 8000.

In a browser, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and verify that you see the sample Django start page

Or, try [http://127.0.0.1:8000/clinicians/](http://127.0.0.1:8000/clinicians/) to view the index page for Clinicians.

**Note:** The Django admin panel is available at `/admin`.

After you migrate, you can create an admin by running 
```
python manage.py createsuperuser
```
