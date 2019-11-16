# Django Forms Deployment on Heroku - Local Branch

This project is about to explain how to deploy the django forms project from lynda on heroku.

## Getting Started

Get PostgreSQL 11.05 , Python 3.6.8 on the global path , pip3 9.0.3 and the latest virtualenv library on any Windows Machine 64 bits

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

**Install pip3 version 9.0.3 for this project**

```
pip3 install pip3==9.0.3
```

**Install the latest virtualenv**

```
pip3 install virtualenv
```

# Test Local Branch

**Clone the local branch from the repository. Local branch is connected to nandiansgardendb**

```
git clone https://github.com/Yoimer/nandians-garden.git --branch local --single-branch
```

**Move to nandians-garden folder**

```
cd nandians-garden
```

**Create virtual enviroment folder**

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

Move back to nandians-garden folder

**Install all the dependencies from requirements.txt using pip3**

```
pip3 install -r requirements.txt
```

**Check migrations and migrate**

```
python manage.py makemigrations pizza
```

```
python manage.py migrate
```

Creates **superuser** in order to manipulate data from Admin. It asks for user, email and password

```
python manage.py createsuperuser
```

**Test django server is running**

``` python
python manage.py runserver
```

**Check server on browser**

http://127.0.0.1:8000/

**Add some data to pizza Size (Small, Medium and Large)**

![Alt text](./docs/img/admin.jpg?raw=true "admin")

**Order a pizza**

![Alt text](./docs/img/order-a-pizza.jpg?raw=true "order a pizza")

**Checking Ordered Pizza**

![Alt text](./docs/img/ordered-pizza.jpg?raw=true "ordered pizza")