# Django Forms Deployment on Heroku - Master Branch

This project is about to explain how to deploy the django forms project from lynda on heroku using the **master** branch code.

### Requisites

* Git for Windows 64 bit version ``` 2.24.0.windows.1 ``` or above from https://git-scm.com/download/win.

* Python 3 ``` Python 3.6.8 ``` from https://www.python.org/ftp/python/3.6.8/python-3.6.8-amd64.exe (using another python version might not work as expected).

* PostgreSQL ``` 11.05 (Graphical User Interface) ``` from https://get.enterprisedb.com/postgresql/postgresql-11.5-1-windows-x64.exe

* Heroku CLI ``` heroku/7.35.0 win32-x64 node-v12.13.0 ``` or above from https://cli-assets.heroku.com/heroku-x64.exe .

### Configuration for Heroku deployment 
When clonning this branch, all of these changes will be made already. We are just explaning what heroku
requires to work from a django project

We need to modify the **settings.py** file inside the **nandiasgarden** folder

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

We need to create a folder called **static** inside the **root project (nandiasgarden)** folder

``` python
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

```
Generate **Procfile** in root directory. It has to have the project name (in our case is nandiasgarden)

```
web: gunicorn nandiasgarden.wsgi --log-file -
```

Add from **django.conf import settings** and **django.conf.urls.static import static** on nandiasgarden/urls.py and **+static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)** at the end of the **urlpatterns** list


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