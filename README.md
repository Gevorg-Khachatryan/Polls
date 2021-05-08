Polls

The project presents itself as the main back-end of polls site. There is no SECRET_KEY in the project.

Requirements

Python 3+
Django 3+

The first thing to do is to clone the repository:

$ git clone https://github.com/Gevorg-Khachatryan/Polls.git

$ cd poll

Create a virtual environment to install dependencies in and activate it:

`py -m pip install --user virtualenv`

`py -m venv env`

`.\env\Scripts\activate`

More: https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/


Then install the dependencies:

(env)$ pip install -r requirements.txt
Migrate:

`(venv)$ cd project`

`(venv)$ python manage.py migrate`

Make admin user:

(venv)$ python manage.py createsuperuser

Once `pip` has finished downloading the dependencies:

`(venv)$ cd project`

`(venv)$ python manage.py runserver`

And navigate to http://127.0.0.1:8000/.