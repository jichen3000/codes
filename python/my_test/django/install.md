## install
pip install Django==1.11.12

python -m django --version

python manage.py startapp polls


# tutorial


## part1
https://docs.djangoproject.com/en/1.11/intro/tutorial01/
 
###Creating a project

django-admin startproject mysite

mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.

manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.

The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).

mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.

mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.

mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.

mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details.  
Gunicorn

### run

python manage.py runserver 8000
python manage.py runserver 0:8000     

http://localhost:8000/polls/ 



## part2

### Database setup
mysite/settings.py
ENGINE – Either 'django.db.backends.sqlite3', 'django.db.backends.postgresql', 'django.db.backends.mysql', or 'django.db.backends.oracle'.

NAME – The name of your database. If you’re using SQLite, the database will be a file on your computer; in that case, NAME should be the full absolute path, including filename, of that file. The default value, os.path.join(BASE_DIR, 'db.sqlite3'), will store the file in your project directory.

###  INSTALLED_APPS

By default, INSTALLED_APPS contains the following apps, all of which come with Django:

django.contrib.admin – The admin site. You’ll use it shortly.
django.contrib.auth – An authentication system.
django.contrib.contenttypes – A framework for content types.
django.contrib.sessions – A session framework.
django.contrib.messages – A messaging framework.
django.contrib.staticfiles – A framework for managing static files.


### create tables
python manage.py migrate

### add models then create tables
python manage.py makemigrations polls

\# just print, not realy run
python manage.py sqlmigrate polls 0001

python manage.py migrate

### Playing with the API
python manage.py shell

from polls.models import Question, Choice
Question.objects.all()

from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())
q.save()
q.id
q.pub_date
q.question_text = "What's up?"
q.save()
Question.objects.all()

current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

Question.objects.get(id=2)

q = Question.objects.get(pk=1)
q.choice_set.create(choice_text='Not much', votes=0)
q.choice_set.create(choice_text='The sky', votes=0)
q.choice_set.create(choice_text='Just hacking again', votes=0)
q.choice_set.all()
q.choice_set.count()
q.save()

## django admin
python manage.py createsuperuser
admin
admin123

python manage.py runserver

http://127.0.0.1:8000/admin/

## test
import datetime
from django.utils import timezone
from polls.models import Question
future_question = Question(pub_date=timezone.now() + datetime.timedelta(days=30))
future_question.was_published_recently()

python manage.py test polls

### shell
python manage.py shell

from django.test.utils import setup_test_environment
setup_test_environment()

from django.test import Client
client = Client()
response = client.get('/')
response.status_code

from django.urls import reverse
response = client.get(reverse('polls:index'))
response.status_code
response.content
response.context['latest_question_list']