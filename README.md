# Django-test-task
Test task for a trainee position

## Getting Started

### Dependencies
Python 3, Django 4, VK auth with python-social-auth library

### Installing
It's recommended to use ***poetry*** as a package manager. It also includes virtual environment functions, so instead of using such virtualenv management systems as venv or pipenv you can try poetry. For complete and full reference proceed: https://python-poetry.org/docs/.

Once you've created a directory for the project, cloned it and downloaded poetry use `poetry install` command to install all the needed dependecies.

### Executing program
As this project uses [https://pypi.org/project/python-dotenv/](python-dotenv) library, first of all you need to configure your .env with the following Django settings variables according to your needs:
```
SECRET_KEY
ALLOWED_HOSTS
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
SOCIAL_AUTH_VK_OAUTH2_KEY
SOCIAL_AUTH_VK_OAUTH2_SECRET
```
This project uses PostgreSQL, so your should provide .env module with the need database settings

## Makefile
For your convenience, use "make name-of-command". E.g. command "make runserver" will execute "poetry run python manage.py runserver" (in more common case - "python manage.py runserver"). All the make commands are listed in django-test-task/my_django_project/Makefile.
* To run server use `make runserver` command in terminal (from "your dir"/my_django_project)
* `make migrations` and `make migrate` for the corresponding commands


## Licence
This project follows the MIT license. See the [LICENSE](LICENSE) for details.


# The problems I couldn't solve
<<<<<<< HEAD
During  my work on this project I've encountered some difficulties beyond my ***current*** knowledge and skills. Since this was my first touch of Django framework, I couldn't manage to close all the tasks in time. In particular, there no any tests covering the project. Also, I had some additional tasks, such as setting up CI/CD, deploying the project using Docker - all of these now are one of my educational priorities.
=======
During  my work on this project I've encountered some difficulties beyond my ***current*** knowledge and skills. Since this was my first touch of Django framework, I couldn't manage to close all the tasks in time. In particular, there no any tests covering the project. Also, I had some additional tasks, such as setting up CI/CD, deploying the project using Docker - all of these now are one of my educational priorities.
>>>>>>> 33d59143d8a08135bb7f3d26d8672fd5a32c8ed1
