# 2022-django-tenant-guide
This is my exercise BUILDING MULTI TENANT SWEETSHOP based on the tutorials made by  Tom's Python and Django on Youtube

Github repository: https://github.com/gurnitha/2022-django-tenant-guide
Tutorials on Youtube: https://www.youtube.com/channel/UCUKoRhPhS0INxh6RC1xN_TQ


#### 1. Clone Github repository

```bash
# Clone Github repository
λ git clone git@github.com:gurnitha/2022-django-tenant-guide.git
Cloning into '2022-django-tenant-guide'...
Enter passphrase for key '/c/Users/hp/.ssh/id_rsa':
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (5/5), done.
remote: Total 5 (delta 0), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (5/5), done.

# Go to the project folder
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide
λ cd 2022-django-tenant-guide\
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)

# Push changes to Github
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
λ git push
```


#### 2. Create virtual environment


```bash
# Create virtual environment
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
λ python -m venv venv3940 --promp django-tenant

# Virtual environtment's structure
.
├── LICENSE
├── README.md
└── venv3940
    ├── Include
    ├── Lib
    │  └── site-packages
    ├── Scripts
    │  ├── Activate.ps1
    │  ├── activate
    │  ├── activate.bat
    │  ├── deactivate.bat
    │  ├── pip.exe
    │  ├── pip3.9.exe
    │  ├── pip3.exe
    │  ├── python.exe
    │  └── pythonw.exe
    └── pyvenv.cfg
```


#### 3. Install Django v4.0


```bash
# Activate virtual environment (venv3940)
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
λ venv3940\Scripts\activate.bat

# Install Django v4.0
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ pip install django==4.0
Collecting django==4.0
  Using cached Django-4.0-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.4.1
  Using cached asgiref-3.5.0-py3-none-any.whl (22 kB)
Collecting tzdata
  Using cached tzdata-2021.5-py2.py3-none-any.whl (339 kB)
Collecting sqlparse>=0.2.2
  Using cached sqlparse-0.4.2-py3-none-any.whl (42 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.5.0 django-4.0 sqlparse-0.4.2 tzdata-2021.5
WARNING: You are using pip version 21.1.1; however, version 22.0.2 is available.
You should consider upgrading via the 'e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\scripts\python.exe -m pip install --upgrade pip' command.

# Upgrate pip
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\lib\site-packages (21.1.1)
Collecting pip
  Using cached pip-22.0.2-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.1.1
    Uninstalling pip-21.1.1:
      Successfully uninstalled pip-21.1.1
Successfully installed pip-22.0.2
```


#### 4. Creating django project 'sweetshop'

```bash
# Checking django version

(django-tenant) λ pip freeze
asgiref==3.5.0
Django==4.0
sqlparse==0.4.2
tzdata==2021.5

# Checking django-admin commands

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ django-admin

Type 'django-admin help <subcommand>' for help on a specific subcommand.

Available subcommands:

[django]
    check
    compilemessages
    ...
    startapp
    startproject
    test
    testserver

# Create django project 'sweetshop'

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ django-admin startproject sweetshop

# Project structures
.
├── LICENSE
├── README.md
├── sweetshop
│   ├── manage.py
│   └── sweetshop
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── venv3940
    ├── Include
    ├── Lib
    │   └── site-packages
    ├── Scripts
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── django-admin.exe
    │   ├── pip.exe
    │   ├── pip3.9.exe
    │   ├── pip3.exe
    │   ├── python.exe
    │   ├── pythonw.exe
    │   └── sqlformat.exe
    └── pyvenv.cfg
```


#### 5. Creating django app 'shop'


```bash

# Creating django app 'shop'

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ ls
LICENSE  README.md  sweetshop  venv3940

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide (main)
(django-tenant) λ cd sweetshop\

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ django-admin startapp shop

# Project's structure
.
├── LICENSE
├── README.md
├── sweetshop
│   ├── manage.py
│   ├── shop
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── migrations
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── sweetshop
│       ├── __init__.py
│       ├── asgi.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
└── venv3940
    ├── Include
    ├── Lib
    │   └── site-packages
    ├── Scripts
    │   ├── Activate.ps1
    │   ├── activate
    │   ├── activate.bat
    │   ├── deactivate.bat
    │   ├── django-admin.exe
    │   ├── pip.exe
    │   ├── pip3.9.exe
    │   ├── pip3.exe
    │   ├── python.exe
    │   ├── pythonw.exe
    │   └── sqlformat.exe
    └── pyvenv.cfg

```


#### 6. Installing the shop app to the project's settings.py


```py

# Install the shop app

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'shop.apps.ShopConfig', # new
]

```


#### 7. Run the local server for testing


```bash

# Run the server

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 03, 2022 - 11:11:28
Django version 4.0, using settings 'sweetshop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

# Open your browser and paste this url + enter

http://127.0.0.1:8000/
```


#### 8. Installing django_tenants


```bash

# Install django_tenants
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ pip install django_tenants
Collecting django_tenants
  Using cached django-tenants-3.4.2.tar.gz (107 kB)
  Preparing metadata (setup.py) ... done
Requirement already satisfied: Django<=4.1,>=2.1 in e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\lib\site-packages (from django_tenants) (4.0)
Requirement already satisfied: tzdata in e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\lib\site-packages (from Django<=4.1,>=2.1->django_tenants) (2021.5)
Requirement already satisfied: sqlparse>=0.2.2 in e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\lib\site-packages (from Django<=4.1,>=2.1->django_tenants) (0.4.2)
Requirement already satisfied: asgiref<4,>=3.4.1 in e:\workspace\django-2022\tenantcy\2022-django-tenant-guide\2022-django-tenant-guide\venv3940\lib\site-packages (from Django<=4.1,>=2.1->django_tenants) (3.5.0)
Using legacy 'setup.py install' for django_tenants, since package 'wheel' is not installed.
Installing collected packages: django_tenants
  Running setup.py install for django_tenants ... done
Successfully installed django_tenants-3.4.2

# Check the result

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ pip freeze
asgiref==3.5.0
Django==4.0
django-tenants==3.4.2
sqlparse==0.4.2
tzdata==2021.5

# Create requirements.txt file

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ pip freeze r> requirements.txt
```


#### 9. Creating Postgres Database


```bash

# Login to the server
E:\workspace
λ psql -U postgres
psql (13.0)
WARNING: Console code page (437) differs from Windows code page (1252)
         8-bit characters might not work correctly. See psql reference
         page "Notes for Windows users" for details.
Type "help" for help.

# Create database

postgres=# CREATE DATABASE django_tenant_guide_2022;
CREATE DATABASE

# Connecting with the database

postgres=# \c django_tenant_guide_2022;
You are now connected to database "django_tenant_guide_2022" as user "postgres".
```


#### 10. Connecting the project with the postgres database


```py

# POSTGRES DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django_tenants.postgresql_backend',
        'NAME': 'django_tenant_guide_2022',
        'USERNAME': 'postgres',
        'PASSWORD': 'ing',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

```


#### 11. Install postgres package


```bash
# Install postgres package

(django-tenant) λ pip install psycopg2
Collecting psycopg2
  Using cached psycopg2-2.9.3-cp39-cp39-win_amd64.whl (1.2 MB)
Installing collected packages: psycopg2
Successfully installed psycopg2-2.9.3

# Run the server for tesing

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
February 03, 2022 - 11:51:34
Django version 4.0, using settings 'sweetshop.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
````
