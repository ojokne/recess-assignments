"""
web scrapping with beautiful soup
Learn on you own
Python MYSQL and MongoDB Database
Python as language,Data science,Machine learning, and web development Framweork

"""
# introduction to Django
"""
Django is a python framework that makes it easier to build web applications.
Open source web framework for python -  Uses the MVT architecture (Model View Template)

-Admin interface
# Django provides an automatic admin interface that can be used to manage models in the application.

compare django with client-side apps React, Angular, Vue
#Django is a server-side application. compare django wirh ASP.NET, C, Express

#Database Support

Django includes DB like PostgreSQL, MySQL, SQLite, Oracle, and NoSQL databases like MongoDB.


# url Routing: helps to map URLs to views,make it easier to define URL patterns
of your application

# Template. Allows you to create dynamic html templates page , bootstrap

# Form handling: Validating of inputd, processing user inputs

# Authentication: User authentication, login, logout, password reset

# Middleware: Allows you to add extra functionalities to request/response pipeline

# Testing: Allows you to test your application automatically

# Internalization: Allows you to translate your application to multiple languages

# Django uses the CRUD operations (Create, Read, Update, Delete) to manage data in the database.

# how Django works
Model = Data you want to present
View = A request handle that returns the relevant template and content
template = A html file that is returned to the client

Gettting started with Django
-Create virtual environment
-Install Django
-Create a Django project
-Create a Django app
-Create a view
-Create a URL
-Create a template
- Model
- insert data
- update data
- delete data
- read data

# install django
pipenv install django

# activate virtual environment
pipenv shell

# Start new Django project
django-admin startproject django_note

# Run server
python manage.py runserver #remember it will use default port 8000

to specify port
python manage.py runserver 8080

# Create a virtual environment for vs code to automatically the virtual environment

pipenv --venv

# Integrate terminal in vs code

C:\Users\oen\.virtualenvs\django-ImTm9ogv\scripts\python 
# then bin instead of scripts for linux and mac

"""

