# Firefly Health Take-home Interview

Hello and thank you for interviewing with Firefly!

This document is not the interview — it is a "pre-brief" to make sure your environment and expectations are properly calibrated before beginning.

Please make sure you read through this document thoroughly. Once you are ready, the detailed prompt can be found in [INSTRUCTIONS.md](INSTRUCTIONS.md)

## What to expect

For this project, you'll be building a miniature version of one of Firefly's real tools. You'll also be using a tech stack that is very similar to Firefly's.

We ask that you dedicate no more than 4 hours to this project and submit your solution within 2-3 days.  After receiving your solution, Firefly will schedule a review session with our engineering team.

Our primary goal for this exercise is to discuss your approach and design decisions.  These technologies may be entirely new to you, and we don't expect a perfect solution.  

This is also not meant to be a test of your familiarity with specific tools or technologies.  It is perfectly fine to Google, refer to documentation / Stack Overflow, and even install packages that you find useful.  Likewise, its fine to leverage workaround if you get stuck on a specific technology.  If this happens, please let us know so we can do better next time!

## The Stack / Frameworks

Within this repo is a self-contained project reliant on a few technologies — if you're unfamiliar with any of them, it's recommended to take some time to explore before diving in. We've included some tips and links to documentation below.

### 1) [Django](https://docs.djangoproject.com/en/3.2/)

You'll want to be comfortable building basic Models and Views. Django's [introduction](https://www.djangoproject.com/start/) is a great place to start if you're new to it.

### 2) [Django REST Framework](https://www.django-rest-framework.org/)

The [Example](https://www.django-rest-framework.org/#example) page  is a good starting place.

### 3) [React](https://reactjs.org)

React's [Getting started](https://reactjs.org/docs/getting-started.html) page offers a few ways to get familiar with the library. There's no requirement to add any other front-end libraries.

The database is SQLite3, but you shouldn't need to worry about that.

## Getting started and submitting your solution


### Base requirements

Have the following tools installed before starting:

- [Docker](https://www.docker.com/products/docker-desktop)

### Getting started

```shell
docker-compose build
docker-compose up
```

This will initialize your SQLite database, and also seed it with some sample data for Clinicians, Availabilities and Appointments.

This should also start the server on port 8000.

In a browser, visit [http://127.0.0.1:8000/](http://127.0.0.1:8000/) and verify that you see the sample Django start page


The Django admin panel is available at `http://127.0.0.1:8000/admin`. The credentials for the admin panel
can be created with : 

```shell
docker-compose exec web python manage.py createsuperuser
```

The front end is available at [http://127.0.0.1:3000/](http://127.0.0.1:3000/).

### Communicating with the API

For an example, see `fetchClinicians` in `frontend/src/requests.js`

The url of the backend server is defined by the `proxy` field in `package.json`. It defaults to `localhost:8000`.

### Submitting your solution

Please fork this repository to your own GitHub account.

When you're finished and ready to submit your solution, please either include an email link to your fork, or provide your solution as a git bundle over email.

The instructions for the project can be found in [INSTRUCTIONS.md](INSTRUCTIONS.md).

Good luck!
