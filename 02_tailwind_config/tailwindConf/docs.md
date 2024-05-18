## Configration Of Tailwind CSS in Django:

#### Steps:

1) Create a Virtual env for the django project.
```console
python -m venv env
``` 

2) Activate the virtual env by command:
**On Window:**
```console
env\Scripts\activate
``` 
**On Unix or macOS:**
```console
source env/bin/activate
``` 

3) Install django in the virtual env 
```console
pip install django
```

4) Start the django project:
```console
django-admin startproject project_name
```

5) Install packages related to tailwind css such as:
```console
python -m pip install django-tailwind
python -m pip install 'django-tailwind[reload]'
```

6) Open settings.py file in your django project directory & check the INSTALLED_APPS sections and add 'tailwind'.
```python
# setting.py
INSTALLED_APPS = [
    ....
    'tailwind',
    ....
]
```

7) Now initaite the 'tailwind' APP :
```console
python manage.py tailwind init
```
**Note:** you should be on the base directory so you can acces the manage.py file.

8) Now theme named folder would be shown the the base directory in django project. Now consider theme files as an app so you need to add it to the INSTALLED_APPS in setting.py of django project.
```python
# setting.py
INSTALLED_APPS = [
    ....
    'tailwind',
    'theme',
    ....
]
```

9) Register the generated 'theme' app by adding the following line to settings.py file:
```python
# setting.py
TAILWIND_APP_NAME = 'theme'
```

10) Now IP is need to provide to run the tailwind server so :
```python
# settings.py
INTERNAL_IPS = ["127.0.0.1",]
```
11) To run tailwind on the dajngo project, node should be install to your machine, [Install nodejs from offical site](https://nodejs.org/en/download/package-manager) and set the path to the npm executable in settings.py file manually:
In order to find the path run the folowing command in terminal :
```console
where npm
```
**On Window:**
Various path will be diplayed select which contain .cmd on last. 
```python
NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
``` 
**On Unix or macOS:**
```python
NPM_BIN_PATH = '/usr/local/bin/npm'
``` 
12) Now, Install Tailwind CSS dependencies, by running the following command:
```console
python manage.py tailwind install
```

13) Now tailwind CSS will works on the webpage. But you have to refresh the page after changing the css. We have install dependience for the reload early i.e 'django-tailwind[reload]', now we have to congig it in django settings so follows the below steps:
```python 
INSTALLED_APPS = [
  # other Django apps
  'tailwind',
  'theme',
  'django_browser_reload'
]

MIDDLEWARE = [
  # ...
  "django_browser_reload.middleware.BrowserReloadMiddleware",
  # ...
]
```

14) Include django_browser_reload URL in your root url.py:
```python
# urls.py (project-level)
from django.urls import include, path
urlpatterns = [
    ...,
    path("__reload__/", include("django_browser_reload.urls")),
]

```
15) Finally, you should be able to use Tailwind CSS classes in HTML. Start the development server by running the following command in your terminal:
```python 
    python manage.py tailwind start
```

Now the css will load as you change .

[ALSO REFER OFFICAL DOCS IF ANY ERROR](https://django-tailwind.readthedocs.io/en/latest/installation.html#)
  
    
## How To Load Tailwind CSS To Django Templete


```html 
Just add : {% load static tailwind_tags %} to top of html file
and : {% tailwind_css %} near css head tag.
```


## Setting this Repository

1) Clone the repo :
```git
    git clone https://github.com/AdityaTote/learn-django-with-me.git
```

2) Move to the Django Project :
```console
     cd 02_tailwind_config/tailwindConf/
```
You can watch the code, its is simple age not has much css.