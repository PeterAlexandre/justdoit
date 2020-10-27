# Justdoit <img src="static/img/icon.png" width="20">
> A portfolio application made in django to manage tasks and increase productivity.
> To access click here: https://justdoit-todolist.herokuapp.com/

> To access the API documentation click here: https://justdoit-todolist.herokuapp.com/api/v1/docs/

[![Python Version](https://img.shields.io/badge/python-v3.8-blue)](https://www.python.org/)
[![Django Version](https://img.shields.io/badge/django-v.3.0-green)](https://www.djangoproject.com/)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-v3.0-blueviolet)](https://getbootstrap.com/docs/3.3/)
[![Bootstrap Template](https://img.shields.io/badge/bootstrap--template-lumino-9cf)](https://medialoot.com/preview/lumino/index.html)
[![License GPL-3.0](https://img.shields.io/badge/license-%20GPL--3.0-yellow.svg)](https://github.com/Ilhasoft/bothub-engine/blob/master/LICENSE)

Dependencies
---
- [Postgresql database](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04)
- [Environment variables](README.md#Environment-variables)

Installation
-------
    $ python -m venv env
	$ source env/bin/activate
	$ pip install -r requirements.txt

#### Migrations
    $ ./manage.py makemigrations
	$ ./manage.py migrate

#### Local usage
	$ ./manage.py runserver

Environment variables
---
| Variable | Explanation |
|--|--|
| SECRET_KEY | This is used to provide cryptographic signing and should be set to a unique, unpredictable value. |
| DEBUG | Set boolean value True if you want see django debug responses. |
| ALLOWED_HOSTS | To run this project in local, set "*". |
| DATABASE_URL | postgres://<user_name>:<user_password>@localhost:5432/<database_name> |
| ALLOW_MEDIA | Boolean value. Use True if the project supports the use of media files |

Copyright
---
See the [LICENSE](/LICENSE) for details.
