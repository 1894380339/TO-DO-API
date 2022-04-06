# TO-DO-API
INTRODUCTION

```
Deploy source code to localhost:
   - Python Package: 
   Django 4.0.3
   djangorestframework 3.12.4
   PyJWT 1.7.1
   django-cors-headers 3.11.0
   datetime 4.4
   mysqlclient 2.1.0
   - Install:
     + pip install mysqlclient  
     + pip install django
     + pip install djangorestframework
     + pip install django-cors-headers
     + pip install datetime
   - Start Project in localhost:
     + python manage.py runserver <port>
     + <port>: 8000

```
```
Connect database:
      + First, replace the 'django.db.backends.sqlite3' to 'django.db.backends.mysql'.  
      + Update database section in settings.py file with the following setting:
         DATABASES = {
          'default': {
              'ENGINE': 'django.db.backends.mysql',
              'NAME'    : 'mydata', 
              'USER'    : 'root',
              'PASSWORD': '',
              'HOST'    : 'localhost',
              'PORT'    : '3306',
                   }
               }
               
Create database:
    - In mysql, create new database with name is mydata
    - In terminal, run:
      + python manage.py makemigrations
      + python manage.py migrate
    -  In mysql, Add sample data by SQL statements in data_test file
```

data_test file: [Link database](https://github.com/1894380339/TO-DO-API/blob/main/mydata.sql)

