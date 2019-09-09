# Django Forms Deployment on Heroku

This project is about to explain how to deploy the django forms project from lynda on heroku.

## Getting Started

Get PostgreSQL 11.05 , Python 3.6.8 on the global path , pip 9.0.3 and the latest virtualenv library on any Windows Machine 64 bits

PostgreSQL 11.05 (GUI)

https://get.enterprisedb.com/postgresql/postgresql-11.5-1-windows-x64.exe

Python 3 (Python 3.6.8)

https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe


### Installing


## PostgreSQL

It is not recomended to install in the default location which is ProgramFiles since this will place your database files in the Progams directory as well.

If the installer fails durring the C++ 2013 runtime install, you probably already have a version of C++ 2013.
You can solve this issue by openening a cmd window in your installer directory and enter:
postgresql-11.4-1-windows-x64.exe --install_runtimes 0

Be sure to select a directory other than ProgramFiles.
The installer should by default install PostgreSQL as a service and start the service.

In order to start and stop the service you will need to be running a cmd window as administrator or open the Windows Services dialog.

You can use the following cmd commands to start and stop the PostgreSQL service.
This assumes your service was named "postgresql-x64-11"
The Windows Services dialog will have the exact name of your installed service if you need to confirm this.

net start postgresql-x64-11
net stop postgresql-x64-11

In order to use the documented pg_ctl command, you will need to set the following environmental variables in your system.
The following assumes you installed PostgreSQL in **C:\PostgreSQL**

Add to System variables Path:

```
C:\PostgreSQL\bin
```
Create the following new System variables

```
PGDATA
C:\PostgreSQL\data
```

```
PGDATABASE
postgres
```

```
PGUSER
postgres
```
```
PGPORT
5432
```

```
PGLOCALEDIR
C:\PostgreSQL\share\locale
```
If your Windows PostgreSQL service is still running, you should now be able to control the server via the documented pg_ctl commands documented here

If you open a new cmd window and type pg_ctl status you should see something like

pg_ctl: server is running (PID: 9344)
C:/PostgreSQL/bin/postgres.exe "-D" "C:\PostgreSQL\data
Be aware that these commands override your windows service commands.
This means that if you stop and start the server via the pg_ctl commands it will then be running under the cmd and not the service, therefore; if you close the current cmd window it will shut down your server.

**Create a local db**

Once postgres server has started (in this case using the services.msc activate since Postgres instalation is with GUI):


**Connect to server**
```
psql -U postgres
```

Then your connected with the postgres server shell. This looks something like this:
```
postgres=# 
```

**Creating role with password (nandiansgarden 12345)**
```
CREATE user nandiansgarden with password '12345';
```

**Creating db (nandiansgardendb)**

```
CREATE DATABASE nandiansgardendb;
```

**Grants privileges in db (nandiansgardendb) to role (nandiansgarden)**
```
GRANT ALL PRIVILEGES ON DATABASE nandiansgardendb TO nandiansgarden;
```

**Log out postgre user(\q) and log in the role just created(nandiansgarden)**
```
psql -U nandiansgarden -d nandiansgardendb -h 127.0.0.1 -W
```

## Python 3.6.8

**Install the python-3.6.8-amd64.exe file using the default instalation and add Python 3.6 to PATH**

```
Default path
C:\Users\User\AppData\Local\Programs\Python\Python36
```

```
Add Python 3.6 to PATH
```

**Verify that python is installed in the global enviroment variables by typing on cmd**

```
python --version
```

**Install pip version 9.0.3 for this project**

```
pip install pip==9.0.3
```

**Install the latest virtualenv**

```
pip install virtualenv
```

**Create a folder called django-forms-course folder and open cmd (or PowerShell) and create an virtual enviroment**

```
python -m venv env
```

**cd to env\Scripts folder and activate the virtual enviroment**

```
activate.bat (if using cmd)
```

```
Activate.ps1 (if using PowerShell)
```

**Install all the python packages required using pip**

```
pip install django
```

**Create nandiansgarden project (including the dot at the end of the command)**
``` python
django-admin startproject nandiasgarden .
```

**Test django server is running**
``` python
python manage.py runserver
```

**Check server on browser**

http://127.0.0.1:8000/

**Open Git Bash on django-forms-course folder and initialize a git repository**
```
git init
```

**Create a local branch**

We will create two branches for this project, **local** and  **master** branch.

Heroku will build this project only in the **master** branch (this is imperative for heroku), however we need to test all the code in the **local** enviroment first.

Heroku deployment requires a lot of adaptation in the **settings.py** file, files and folder addition such has **requirements.txt**, **Procfile** and **static/** folder also.

So, as soon as we're ready to make the deployment, we will create a master **branch** off of the **local** branch and we'll
start making the Heroku's configuration-adaptation.

Command to create the **local** branch

```
git checkout -b local
```

Now Git bash should show that we're in the **local** branch

**Let's create the .gitignore file**

This is for avoiding unnecessary changes prompting on the git bash console. Windows tends to include a lot of files that we won't care about in the project

```
touch .gitignore
```
.gitignore configuration (your's may vary depending on the OS)

``` shell
# don't track content of these folders
nandiasgarden/__pycache__/
nandiasgarden/__init__.py
env/

# compiled source #
###################
*.pyc

# sqlite3 file (We'd be using postgreSQL)
*.sqlite3
```

Git add the rests of the files

```
git add .
```

Create a github repository and add it to the local configuration. We decided to call it "heroku"
```
git remote add heroku https://github.com/Yoimer/nandians-garden.git
```

Git commit
```
git commit -m "initial django configurations based on the local enviroment"
```

Git Push the commit
```
git push -u heroku local
```

Create a new app. One of our main products is "pizza", so let's create it

```
django-admin startapp pizza
```

Add pizza/__init__.py and pizza/migrations/__init__.py to .gitignore

``` shell
# don't track content of these folders
nandiasgarden/__pycache__/
nandiasgarden/__init__.py
pizza/__init__.py
pizza/migrations/__init__.py
env/

# compiled source #
###################
*.pyc

# sqlite3 file (We'd be using postgreSQL)
*.sqlite3
```

Add home and ordering page to the project. In order to do so, let's add the new pages on the **nandiasgarden\url.py**:

``` python
from django.contrib import admin
from django.urls import path
from pizza import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #default page
    path('order', views.order, name='order'),
]
```

Since we have just installed our pizza app, we have to add it to the **nandiasgarden/settings.py** INSTALLED_APPS list:

``` python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pizza',
]
```

Let's make some views that return back this two sites (home and order) on **pizza/views.py**

``` python
from django.shortcuts import render

def home(request):
    return render(request, 'pizza/home.html')

def order(request):
    return render(request, 'pizza/order.html')
```

Let's add the templatess for both of these views:

Inside of the **pizza** folder let's create **templates** folder and inside of it let's create one called **pizza** and in that folder the **home.html**

```
pizza/templates/pizza/home.html
```

```
pizza/templates/pizza/order.html
```

Content of home.html
``` html
<h1>Nadian's Garden</h1>
<a href="{% url 'order' %}">Order a pizza</a>
```

Content of order.html
``` html
<h1>Order a Pizza</h1>
```