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



