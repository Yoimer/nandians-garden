# Django Forms Deployment on Heroku - Master Branch

This project is about to explain how to deploy the django forms project from lynda on heroku using the **master** branch code.

### Requisites

* Git for Windows 64 bit version ``` 2.24.0.windows.1 ``` or above from https://git-scm.com/download/win.

* Python 3 ``` Python 3.6.8 ``` from https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe (using another python version might not work as expected).

* Heroku CLI ``` heroku/7.35.0 win32-x64 node-v12.13.0 ``` or above from https://cli-assets.heroku.com/heroku-x64.exe .

### Configuration for Heroku deployment 
When cloning this branch, all of these changes will be made already. We are just explaning what heroku
requires to work from a django project

We need to modify the **settings.py** file inside the **nandiansgarden** folder

Heroku requires this adaption in order to work as expected.

Modify **DEBUG** to False and **ALLOWED_HOSTS** to all.

```python
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = ['*']
```

Add **whitenoise.middleware.WhiteNoiseMiddleware** in the **MIDDLEWARE** list

```python
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]
```

Remove the local database configuration on **DATABASES** and add the **decouple** configuration

Everytime we create a database on heroku it saves the credentials on a variable called **'DATABASE_URL'**

Using the **decouple** configuration prevents harcoding heroku crendentials on **settings.py**


```python
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'pruebadb',
#         'USER': 'prueba',
#         'PASSWORD': '12345',
#         'HOST': 'localhost',
#         'PORT': '5432',
#     }
# }

import dj_database_url
from decouple import config

DATABASES = {
    'default': dj_database_url.config(
        default=config('DATABASE_URL')
    )
}
```
Let's add the Django **static** files configuration.

``` python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```
Generate **Procfile** in root directory. It has to have the project name (in our case is nandiansgarden)

```
web: gunicorn nandiansgarden.wsgi --log-file -
```

Add from **django.conf import settings** and **django.conf.urls.static import static** on nandiansgarden/urls.py and **+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)** at the end of the **urlpatterns** list


``` python

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'), #default page
    path('order', views.order, name='order'),
    path('pizzas', views.pizzas, name='pizzas'),
    path('order/<int:pk>', views.edit_order, name='edit_order'),
    path('multiorder/<int:pk>/<int:nop>', views.edit_multi_order, name='edit_multi_order'), #nop stands for number of pizzas
]   +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

### Installation and Cloning


* Cloning master branch in your Windows computer

```
git clone https://github.com/Yoimer/nandians-garden.git --branch master --single-branch
```

* Python 3.6.8

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

* Heroku Command Line Interface (CLI)

Download and install the **heroku cli** depending on your **OS**

https://devcenter.heroku.com/articles/heroku-cli

**Heroku is installed in the **global path** by default in Windows. Inside of nandians-garden folder, login with your account from **cmd** by typing:**

```
heroku login
```

**Create an app including its name (in our case it is nandiansgarden, yours has to be different)**

```
heroku create -a nandiansgarden
```

**Add heroku git remote repository**

```
heroku git:remote -a nandiansgarden
```

**Create postgresql db in heroku**

heroku addons:create heroku-postgresql:hobby-dev --app appname (in our case nandiansgarden, yours has to be different)

```
heroku addons:create heroku-postgresql:hobby-dev --app nandiansgarden
```

**Push code to heroku**

```
git push heroku master
```

If deployment is successful, console should show http://appname.herokuapp.com **(https://nandiansgarden.herokuapp.com)** deployed to heroku
![Alt text](./docs/img/heroku-deployment.jpg?raw=true "heroku deployment")

**Migrate in heroku**

```
heroku run python manage.py migrate
```
Console should apply all the migration sessions a shown above
![Alt text](./docs/img/heroku-migrate.jpg?raw=true "heroku migrate")


**Activate pizza app on heroku**

The next steps were needed in order to activate the **pizza** app saved on **nandiasgarden/settings.py**
on heroku.

```
heroku run bash
```

```
python manage.py  makemigrations
```

```
python manage.py  makemigrations pizza
```

Once again

```
python manage.py migrate
```

![Alt text](./docs/img/heroku-makemigrations-pizza.jpg?raw=true "heroku make migration pizza")

**Create django super user on heroku**

We first need exit from the heroku bash enviroment

```
exit
```

```
heroku run python manage.py createsuperuser
```
![Alt text](./docs/img/heroku-manage-createsuperuser.jpg?raw=true "heroku manage createsuperuser")

Now, it is needed to configure the pizza sizes in order to order pizzas.

Get on https://nandiansgarden.herokuapp.com/admin/ and login with the password you previously set it

![Alt text](./docs/img/heroku-django-admin.jpg?raw=true "heroku django admin")

* Add pizza sizes

![Alt text](./docs/img/heroku-django-pizza-size.jpg?raw=true "heroku django pizza size")

* Order a Pizza

![Alt text](./docs/img/heroku-django-order.jpg?raw=true "heroku django order")

* Edit Pizza Order

![Alt text](./docs/img/heroku-django-edit-your-order.jpg?raw=true "heroku django edit your order")

* Testing more than one pizza

![Alt text](./docs/img/heroku-django-testing-all-empty-fields.jpg?raw=true "heroku django-testing all empty fields")