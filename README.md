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


#### 12. Activating Django default models


```bash

# Create migration files
(django-tenant) λ python manage.py makemigrations
No changes detected

# Apply migrations files
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK

```


#### 13. Creating Shop and Domain models


```py
# shop/models.

# Django modules
from django.db import models
from django_tenants import TenantMixin, DomainMixin

# Create your models here.


# MODEL: Shop as client
class Shop(TenantMixin):

  name = models.CharField(max_length=100)

  # Default true, schema will be authomatically 
  # created and synced when it is save
  auto_create_schema = True

  def __str__(self):
    return self.name 


# MODEL: Domain
class Domain(DomainMixin):
  pass 

```
<<<<<<< HEAD


#### 14. Fixing impor of  django_tenants, add TENANT_MODEL and TENANT_DOMAIN_MODEL to settings.py


```py

# Fixing import django_tenants
# Before
from django_tenants import TenantMixin, DomainMixin # do not use this, use bellow

# After fixing
from django_tenants.models import TenantMixin, DomainMixin

# Add TENANT_MODEL and TENANT_DOMAIN_MODEL to settings.py
# NEW
TENANT_MODEL = "shop.Shop"
TENANT_DOMAIN_MODEL = "shop.Domain"

```


#### 15. Adding middleware to settings.py


```py

MIDDLEWARE = [
    # Must put on the top
    'django_tenants.middleware.main.TenantMainMiddleware', # new    

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

```


#### 16. Darurat


```py

# shop/models.

# Django modules
from django.db import models
# Fixing this bellow
from django_tenants.models import TenantMixin, DomainMixin


        both modified:   README.md
        both modified:   shop/models.py

```


#### 17. Split the INSTALLED_APPS


```py
SHARED_APPS = [
    
    # Third party apps

    # django_tenants MUST be placed at 
    # the highest position possible
    'django_tenants',

    # Locals
    'shop.apps.ShopConfig',  

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

INSTALLED_APPS = list(SHARED_APPS) + [
    app for app in TENANT_APPS if app not in SHARED_APPS
]

```


#### 18. Run migrations


```py

# Run migrations
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py makemigrations
Migrations for 'shop':
  shop\migrations\0001_initial.py
    - Create model Shop
    - Create model Domain

# Apply migration
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py migrate
[standard:public] === Starting migration
[standard:public] Operations to perform:
[standard:public]   Apply all migrations: admin, auth, contenttypes, sessions, shop
[standard:public] Running migrations:
[standard:public]   Applying shop.0001_initial...
[standard:public]  OK

# The result

# Generated by Django 4.0 on 2022-02-03 06:56

from django.db import migrations, models
import django.db.models.deletion
import django_tenants.postgresql_backend.base


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_name', models.CharField(db_index=True, max_length=63, unique=True, validators=[django_tenants.postgresql_backend.base._check_schema_name])),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(db_index=True, max_length=253, unique=True)),
                ('is_primary', models.BooleanField(db_index=True, default=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='domains', to='shop.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

```


#### 19. Creating tenants


```py

# Checking management commands
(django-tenant) λ python manage.py

Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[django_tenants]
    all_tenants_command
    clone_tenant
    collectstatic_schemas
    create_missing_schemas
    create_tenant # <--- to be used to create tenant
    create_tenant_superuser
    delete_tenant
    migrate
    migrate_schemas
    rename_schema
    tenant_command

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver

# Create tenant

(django-tenant) λ python manage.py create_tenant
schema name: shop1
name: shop1
[1/1 (100%) standard:shop1] === Starting migration
[1/1 (100%) standard:shop1] Operations to perform:
[1/1 (100%) standard:shop1]   Apply all migrations: admin, auth, contenttypes, sessions, shop
[1/1 (100%) standard:shop1] Running migrations:
[1/1 (100%) standard:shop1]   Applying contenttypes.0001_initial...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0001_initial...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying admin.0001_initial...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying admin.0002_logentry_remove_auto_add...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying admin.0003_logentry_add_action_flag_choices...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying contenttypes.0002_remove_content_type_name...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0002_alter_permission_name_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0003_alter_user_email_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0004_alter_user_username_opts...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0005_alter_user_last_login_null...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0006_require_contenttypes_0002...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0007_alter_validators_add_error_messages...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0008_alter_user_username_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0009_alter_user_last_name_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0010_alter_group_name_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0011_update_proxy_permissions...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying auth.0012_alter_user_first_name_max_length...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying sessions.0001_initial...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying shop.0001_initial...
[1/1 (100%) standard:shop1]  OK
domain: shop1.localhost
is primary (leave blank to use 'True'):
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ

# Note: 
# 1. Make sure your postgres server is running
# 2. Refresh your postgres db
# 3. You should she a new schema named 'shop1' bellow the public schema in your postgres database
# On my part, the new schema 'shop1' was succesfully created. :)
```


#### 20. Creating sweet_shared app and sweet_tenant app and install them to settings.py


```py

# Create apps
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py startapp sweet_tenant

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py startapp sweet_shared

# Install to settings

SHARED_APPS = [
    
    # Third party apps

    # django_tenants MUST be placed at 
    # the highest position possible
    'django_tenants',

    # Locals
    'shop.apps.ShopConfig',  

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'sweet_shared',
]

TENANT_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Locals
    'sweet_tenant',
]
```


#### 21. Creating SweetType and Sweet models


```py

# 1. Create SweetType model

# sweet_shared/models.py

# Django modules
from django.db import models

# Create your models here.


class SweetType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name 

# 3. Register to admin

# sweet_shared/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import SweetType

# Register your models here.


admin.site.register(SweetType)


# 3. Create Sweet model

# sweet_tenant/models.py

# Django modules
from django.db import models
from sweet_shared.models import SweetType

# Create your models here.


class Sweet(models.Model):
    sweet_type = models.ForeignKey(SweetType, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name 

# 3. Register to admin

# sweet_tenant/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import Sweet

# Register your models here.


admin.site.register(Sweet)
```


#### 22. Run migrations


```py

# Create migrations

E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py makemigrations
Migrations for 'sweet_shared':
  sweet_shared\migrations\0001_initial.py
    - Create model SweetType
Migrations for 'sweet_tenant':
  sweet_tenant\migrations\0001_initial.py
    - Create model Sweet

# Apply migrations
E:\workspace\django-2022\TENANTCY\2022-django-tenant-guide\2022-django-tenant-guide\sweetshop (main)
(django-tenant) λ python manage.py migrate
[standard:public] === Starting migration
[standard:public] Operations to perform:
[standard:public]   Apply all migrations: admin, auth, contenttypes, sessions, shop, sweet_shared, sweet_tenant
[standard:public] Running migrations:
[standard:public]   Applying sweet_shared.0001_initial...
[standard:public]  OK
[standard:public]   Applying sweet_tenant.0001_initial...
[standard:public]  OK
[1/1 (100%) standard:shop1] === Starting migration
[1/1 (100%) standard:shop1] Operations to perform:
[1/1 (100%) standard:shop1]   Apply all migrations: admin, auth, contenttypes, sessions, shop, sweet_shared, sweet_tenant
[1/1 (100%) standard:shop1] Running migrations:
[1/1 (100%) standard:shop1]   Applying sweet_shared.0001_initial...
[1/1 (100%) standard:shop1]  OK
[1/1 (100%) standard:shop1]   Applying sweet_tenant.0001_initial...
[1/1 (100%) standard:shop1]  OK

```


#### 23. Darurat - Delete db, migrations files and recreate db

```py

        modified:   shop/migrations/0001_initial.py
        modified:   sweet_shared/migrations/0001_initial.py
        modified:   sweet_tenant/migrations/0001_initial.py
```
