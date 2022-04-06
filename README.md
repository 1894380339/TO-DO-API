# TO-DO-API
INTRODUCTION

```
Deploy source code to localhost:
   - Install libraries: Django, djangorestframework, PyJWT, django-cors-headers, datetime
     + pip install django
     + pip install djangorestframework
     + pip install django-cors-headers
     + pip install datetime
   - Start Project:
     + python manage.py runserver <port>
     + <port>: 8000

```
```
Connect database:
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
               
  Create database: run in terminal
      + python manage.py makemigrations
      + python manage.py migrate
```

Database is used in testing: [Link database](https://drive.google.com/file/d/1h8eUZ-pnQnYBI94OZlnGaKzy9ZuDQgrH/view?usp=sharing)

