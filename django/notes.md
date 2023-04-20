# Django

## Overview

Django is a  server-side web framework written in Python to faciliate web development

### Prerequisites

### Installation

````bash
pip3 install django
````

Check version:

````bash
django-admin --version
````

## First app: Hello world

* Create a directory for our web project

````bash
mkdir hello-world
````

* Move to that directory

````bash
cd hello-world
````

* The next step is to make a Django project inside our project folder. That can be done using the following command.

````bash
django-admin starproject config .
````

Note the dot(.) at the end.

Check the result using the tree command

````bash
tree
````

Then we get the following output:

````bash
.
├── config
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 6 files
````

The command created a folder named config and a file named manage.py

* manage.py is used to perform many task with the server such as run, perfor tests, etc.
* There are 5 files inside the config folder
  * wsgi.py where wsgi stands for web server gateway interfaceand serves as server for the app
  * asgi.py where asgi means asynchronous server gateway interface
  * settings.py is uded to configure the project settings
  * urls.py is used for response to the user URL requests
  * \_\_init\_\_.py

In fact, Django provide a local web server that can be ised to preview our application.

To run that server, use the command:

````bash
python3 manage.py runserver
````

output:

````output
````

That local server is available  runs on the port 8000.

So we can use ````127.0.0.1:8000```` (localhost) in a browser to access our django web app.

Image

Now use ctrl+C to stop the server.

Note that the previous command produces (wornings in read color). To avoid that, we can use the migrate sub-command.

````bash
python3 manage.py migrate
````

Then there will not be any warning caused by the runserver subcommand:

````bash
python3 manage.py runserver
````

Output

````output
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 19, 2023 - 11:18:09
Django version 4.1.7, using settings 'config.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
````

A django web project consists of one or several apps. Until now we start a django project but we hava not yet an app.

We use the startapp sub-command to create an app with django.

````bash
python3 manage.py startapp pages
````

That command creates an app named ````pages````.
Then we have a new folder,pages created.

````bash
tree pages
````

output:

````output
pages/
├── admin.py
├── apps.py
├── __init__.py
├── migrations
│   └── __init__.py
├── models.py
├── tests.py
└── views.py

1 directory, 7 files
````

* admin.py is the configuration file for the built-in django amin app
* apps.py is the configuration file for our app(pages)
* models.py is the configuration file for our(eventual) database
* tests.py isfilefor our app testing
* views.py is the file for request/response handling
* migations folder is for tracking changes to models.py

Then we should note to our Django that we have ceated an app named pages. To do so, we have to modify our config/settings.py file.

Inside the config/settings.pŷ file, there is a list named INSTALLED_APP:

````python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
````

That list contains for now the list of django bult-in apps. We have to add our pages app to that list. Then we'll have:

````py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'pages'
]
````

When we type a URL using the browser, we say that the concerned URL is requested. Then that URL is searched as an regular expression. If found, the URL specifies the concerned view which determines the conteent of the page based eventually on the model(database) and then, determines a template for styling. Finally, an HTTP response is sent to the user.

In our pages/ directory, we should create a file named urls.py. That file will contains essentially the list of the url patterns of our web app. For each of these patterns we'll specify to the server the behaviour to have. That behaviour is typically a function or a class, that specifies the answer to the request.

The concerned function or class should be defined in the pages/views.py file.

The config/urls file contains list of url patterns for our django apps.

In practice, the following steps can be followed, after ading our app to the list of app in the config/settins.py file:

* Include urls for our pages module inside our config/urls.py

````py
from django.contrib import admin
from django.urls import path,include #new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls')),#new
]

````

We use the include function to include the urls configuration file of our pages module.

* Define the homePageView function inside the pages/views.py file

````py
# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    #print("Hello bro")
    return HttpResponse('Hello world')
````

It just returns  'Hello world' as HttpResponse, for whatever request.

Note that function must return an HttpResponse object.

* Add url pattern and behaviour for  our home page  inside our pages/urls.py file.

````py
#pages/urls.py
from django.urls import path
from .views import homePageView
urlpatterns = [
path('',homePageView,name='home')
]
````

The name argument is not required.It specifies a name to the url.

The homePageView function is called whenever an user requests the home page

Now let's define another function as response to request of another url of our pages app, 'example' for example

* First of all define the function

````py
def exampleView():
    print('Just an example')
    return HttpResponse('This is another example')
````

* then add the url path to the urlpatterns

````py
#pages/urls.py
from django.urls import path
from .views import homePageView,exampleView#new
urlpatterns = [
path('',homePageView,name='home'),
path('example/',exampleView),#new
]
````

Now run the server and request the url ````127.0.0.1:8000/example````

output:

````output
This is another example
````

## Class based approach

The behavious we created above inside our views.py file are function and just return an HttpResponse.

We can use class approach to allow the view to use a template, which is typically a web page(html page).

In this projects we will have 2 web pages, one for home and another for about.

* Create a directory named webApp

````bash
mkdir webApp
````

* Move to that directory

````bash
cd webApp
````

* Start a Django project

````bash
django-admin startproject config .
````

* Use tree to check

````bash
tree
````

* Use migrate sub-commang to suppress warnings

````bash
python3 manage.py migrate
````

* Start the server for preview

````bash
python3 manage.py runserver
````

* Access the server to assure it runs properly
* Stop the server using Ctrl+C
* Create a Django app named pages

````bash
python3 manage.py startapp pages
````

* Check the pages are created:

````bash
tree pages
````

* Add the pages app inside the config/settings.py file

* Include pages.urls inside the config/urls.py file

* Create the template directory

````bash
mkdir template
````

* Add the template directory in the config/settings.py file

````py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR.joinpath('templates'))],#new
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
````

* Create template files, template/home.html and template/about.html, respectively for home view and about view.

````bash
touch templates/home.html templates/about.html
````

* Add content to these files

````html
<h1>This is our home page</>
````

````html
<h1>This is our about page</>
````

* Create a class for home view and another for about view, all inside the pages/views.py file.

````py
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name='home.html'

class AboutView(TemplateView):
    template_name='about.html'
````

* Create the pages/urls.py file

````bash
touch pages/urls.py
````

* Import HomeView and AboutView inside pages/urls.py and add them to the url patterns.

````py

from .views import HomeView,AboutView
urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutView.as_view(),name='about')
]
````

* Run the server
* Access the  home and about urls to check

You can change the content of the home page:

````django
<h1>This is our home page</h1>
<p><a href='about'>Link to about page</a></p>

<p><a href='about/'>Another link to about page</a></p>
<p><a href="{%url 'about'%}">Access about page</a></p>
````

We create a link to about page using the name of our url, the name we defined insidethe pages/urls.py file.

* First using about or about/ as the value of the href attribute
* Secondly using

````django
 {% url'about' %}
````

That's called template tag.

Themplate tags take the form {% something %} where "something" is the template itself.

Let's create a header template for our home and about view templates.

* Create templates/header.html

````bash
touch templates/header.html
````

* Add this content

````django
<h1>Header</h1>
<a href="{% url 'home' %}">Home page</a>
<a href="{% url 'about' %}">About page</a>

````

To include it in each template file we'll use the extends tag

Then we must use block and endblock tags
both in the header file and in home and about pages.

* header:

````html
<header>Header
<a href="{% url 'home' %}">Home page</a>
<a href="{% url 'about' %}">About page</a>
</h1>
{% block content %}{% endblock  %}
````

* home:

````html
{% extends 'header.html' %}

{% block content  %}
<h1>This is our home page</h1>
<p><a href='about'>Link to about page</a></p>
<p><a href='about/'>Another link to about page</a></p>
<p><a href="{%url 'about'%}">Access about page</a></p>
{% endblock  %}
````

* about:

````html
{% extends 'header.html' %}
{% block content %}
<h1>This is our about page</h1>
{% endblock  %}
````

## Introduction to Unit tests

Let's consider our previous project.

With Django, unit tests are written in the file pages/test.py

This is the initial content of that file:

````py
from django.test import TestCase

# Create your tests here.
````

That file import the TestCase class from the module django.test.

TestCase is a class used to perfor unit test on django apps that need database or not.

If an app doesn't need any database, the SimpleTestCase class is the recommended one.

### Examples of tests

````py
from django.test import SimpleTestCase

# Create your tests here.

#Our app doesn't use any database
class Tests(SimpleTestCase):
    def testHomePage(self):
        response=self.client.get('')
        self.assertEqual(response.status_code,200)
    def testAboutPage(self):
        response=self.client.get('/about/')
        self.assertEqual(response.status_code,200)
````

When a response to an URL request is correct, the cstatus code 200 is returned. Else, 404 is returnded.

Sowe write two functions to test the server respond correctly to the request of home page and the about page, using the assertEqual method. We compare the status code of the response to 200.

The tests will fail for a code different from 200 and will success if the status code is 200.

To run the test:

````bash
python3 manage.py test
````

There are some unit test methods:

* assertEqual
* assertNotEqual
* assertTrue
* assertFalse
* assertIsNot
* assertIsNotNone
* assertIsInstance
* asseertIsNotInstance
* assertIn
* assertNotIn
* assertContains
* assertLess
* assertLessEqual
* assertGreet
* assertGreatEqual
* assertRaises
* assertTemplateUsed
* assertTemplateNotUsed
* assertListEqual
* assertDictEqual
* assertTupleEqual
* etc

## Django syntax in templates

In that section we will learn Django syntax.

We'll essentially learn:

* how to make comment in templates
* how to use variable and expression inside templates
* how to transfer ata from view to template
* how to use if condition and for loop inside template

* Let's create a template file named syntax.html and add the following content:

````html
<h1>Django syntax</h1>
````

* Create a view class named SyntaxView inside the pages/views.py file

````py
class SyntaxView(TemplateView):
    template_name='syntax.html'
````

* Now link that view to an URL pattern, named syntax inside the pages/urls.

````py
# pages/urls.py
from django.urls import path
from .views import HomePageView, AboutPageView,SyntaxView
urlpatterns = [
path('about/',AboutPageView.as_view(),name='about'),
path('', HomePageView.as_view(), name='home'),
path('syntax/',SyntaxView.as_view(),name='syntax'),
]
````

* Now run the server and acesss the url 127.0.0.1/80000/syntax to confirm it works properly.

The tempates/syntax.html will be changing as we move on.

Then, for each step, complete the code and reload the page to preview.

### Comments

Comments are made using the comment tag:

````django
<h1>Django syntax</h1>
{% comment %}
<p>This is a comment</p>
{% endcomment  %}
````

### with tag and django expression

with tag is a template tag used to assign a value to a template inside template.

#### Example

````django
{% with name='Andrew' %}
<p>Hello {{name}}, how are you?</p>
{% endwith %}
````

{{name}} is called an expression and can be used only inside the with template tag block.

#### Other examples

````django
{% with age=18 %}
<p>I'm {{age}} years old</p>
{% endwith %}

{% with beautiful=True %}
<p>Is she beautiful? {{beautiful}}</p>
{% endwith %}


{% with 1.5 as tail %}
<p>Your tail is {{tail}} m</p>{% endwith %}

{% with hello as h %}
<p>{{h}}</p>
{% endwith %}
````

Note that the last example is also a syntax of the with tag.

### Transfer data from view to template

We can transfer variables from view to template

### Example: Variables transfer

````py
class SyntaxView(TemplateView):
    template_name='syntax.html'

    def get(self,request):
        context={'hello':"Hello world",
                'how':"How are you?",
                'age':25,
                'fruits':['orange','mango','pineapple','apple']}
        return render(request,self.template_name,context)
````

* ````get``` is the methods that make the transfer
* ````context```` variable is a dictionary that contains as values the identifiers of all the variables to transfer and as key the identifiers they'll be refered to inside the template file.

Now we can refer these variables in our template file(tempates/syntax.html)

````django
<p>{{hello}}</p>
<p>{{how}} Fine I hope!</p>
<p>{{fruits}}</p>
{% with hello as h %}
<p>{{h}}</p>
{% endwith %}
````

### for loop

for and endfor template tags are used toitarate ovr objects

````django
<ul>My prefered fruits are:
    {% for fruit in fruits %}
    <li>{{fruit}}</li>
    {% endfor %}
</ul>
````

### if, elif and else

* if and endif tags are used to perform a task for certain condition

````py
{% if age == 25 %}
<p>age is 25</p>
{% endif %}
````

* elif and/else tags can be used inside if block

````django
{% if age == 25 %}
<p>age is 25</p>
{% endif %}

{% if age == 18 %}
<p>Of course. You're {{age}} years old</p>
{% else %}
<p>Not at all. You're {{age}} years old</p>

{% endif %}

{% if  age < 18 %}
<p>You're not alowed to watch that film</p>

{% elif age == 18 %}
<p>You're just major</p>

{% else %}
<p>Okay you can!</p>

{% endif %}

{% if  1 == 1 or  2 == 3 %}
<p>Yeah</p>
{% endif %}
````

## Url with parameter

We'll create a template. It's content will depend on th or note value of an url integer parameter (greater than )

* create a template file param.html
* link that an url with integer parameter inside the pages/urls.py:

````py
urlpatterns = [
path('about/',AboutPageView.as_view(),name='about'),
path('', HomePageView.as_view(), name='home'),
path('syntax/',SyntaxView.as_view(),name='syntax'),
path('param/<int:id>',ParamView.asView(),name="param"),
]
````

## 404 template

When an user requests a non-existing URL, the server responds by returning 404 as response status code.An error, called 404 error occured.

You can access a non-existing url for example 127.0.0.1/8000/gghhk. You'll get the following result

or the following one.

The first result is obtained in debug mode and the second one, which is the standard 404 error page, in production mode.

We can change the development mode by updated the DEBUG variable inside the congig/settings.py file.

````py
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG =False
````

When DEBUG is False, the ALLOWED_HOSTS variable should be setled

````py
ALLOWED_HOSTS = ['*']
````

If the DEBUG variable is set to False, the standard 404 page is displayed in case of incorrect URL request.

Moreover,we can edit a custom 404 error page. That is done by creating the template file 404.html. Then, this page will be displayed in case of 404 error.

````bash
touch templates/404.html
````

Add the following content to that file:

````html
<h1>Page not found</h1>
<h1><b>404</b>:The URL requested doesn't exist</h1>
````

Then run the server and access an non-existing URL. The previous web page should be the one displayed.

Overall, in case of 404 error,

* In case of debug mode(DEBUG is True) , the first 404 error page is displayed
* . Django looks:
 for the 404.html inside the templates directory:

* in case debug mode is turned off mode(DEBOG is False), Django looks for the 404.html file in the templates directory.
  * If it exists, it's displayed.
  * else, the standard 404 error page is displayed

## Database app

* create a directory named study
* create a django project inside that directory
* run the server to confirm everything works
* access 127.0.0.1/8000 for preview
* create an app named pages and declare it insie the config/settings.py file

### Django site administration

Django provides a graphic user interface for website administration, concerning databases and users for examples.

It can be used to create users(site adminers), update users password, manage website databases.
Access the django site administration interface via 127.0.0.1/8000/admin

You'll need account informations(username and password) for login.

As there is no user for now, we need to create one.

An user is created using the sub-command createsuperuser

````bash
python3 migrate.py createsuperuser
````

That command helps to create a superuser(adminer) interactively.

You need to provide firstly your username, secondly an email address, then the password and finally the password again for confirmation.

You can validate the first step to use the same username as the one on the computer.

Now an user account is created.

Access 127.0.0.1/8000/admin once again and provide the account informations of the user that's just created, for login.

In Django, a model is a python class that represents a database table.That allows the developer to manage easily a database regardless the database management system(DMS) choosed.
Django supports DMS such as SQLite, MySQL, PostgreSQL, MariaDB and  Oracle.

SQLite is the default used for local development.

To create models we need to edit the file pages/models.py

Let's create a model named Course.

````py
from django.db import models

# Create your models here.

#Course model
class Course(models.Model):
    name=models.CharField()# the name of the course
    lastUpdate=models.DateField()# the date of last update
    isGiven=models.BooleanField()# if the course is already given or not
````

Now we have to create migration file using makemigrations.

* Migration files create reference to the database model. That allows to track the database model changes.
* Migration files are available in the directory pages/migration.

````bash
python3 manage.py makemigrations pages
````

That command makes migrations for database relative to pages app only.
It gives the following output:

````output
Migrations for 'pages':
  pages/migrations/0001_initial.py
    - Create model Course
````

* 0001 represent the name of the migration
* 0001_initial.py is the migation file.  That file contains the code for creating the model pages. As field it contains aditional 'id' which is added by default by Django as a primary key. THat file can be modified; for example the id field can be remoded.

To make migrations for database(s) of all apps of the project use:

````bash
python3 manage.py makemigrations pages
````

After migation and eventual modification of the migration file(s), we need to apply migrations using the migrate subcommand.

We can specify an app for migration. Otherwise, all migrations made will be applied.

````bash
python3 manage.py migrate pages
````

That command apply the previous migration on pages app to the database. Then, the concerned table(s)will be created(or updated)

output:

````output
Operations to perform:
  Apply all migrations: pages
Running migrations:
  Applying pages.0001_initial... OK
````

To preview the SQL code executed by a migration, use the sqlmigrate subcommand specifying the app label an the name of the migration:

````bash
python3 manage.py sqlitemigrate pages 0001
````

Output:

````SQL
BEGIN;
--
-- Create model Course
--
CREATE TABLE "pages_course" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(100) NOT NULL, "lastUpdate" date NOT NULL, "isGiven" bool NOT NULL);
COMMIT;
````

To manage our database table we've just created, using the gui, we need to register it's model, Course inside the pages/admin.py file.

````py
from django.contrib import admin
from .models import Course
# Register your models here.

admin.site.register(Course)
````

Now access the admin url and you'll see the database is creared with the Course table.

Add a course with name Maths

Now define the following method insidetheCourse class in the pages/models.py file.

````py
def __str__(self):
    return self.name[:10]
````

With that approach,if we print a Course object, the 10 first chars of the name of the concerned course will be printed. Same on the Gui.

We can also update and delete course using the GUI.

Create templates/ directory

````bash
mkdir templates
````

Declare the templates directory in the coonfig/settings.py file

````py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR.joinpath('templates')],#new
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
````

create the home template file

````bash
touch templates/home.html
````

Add this content to it:

````html
<h1>Database with Django</h1>
````

Create the home view in pages/view.py

````py
from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Course
# Create your views here.

# homepageview
class HomePageView(TemplateView):
    template_name='home.html'

    def get(self,request):
        x=Course.objects.count()
        objs=Course.objects.all()
        context=dict()# the dic of vars to pass to the template
        context['count']=x
        context['courses']=objs
        print("First course:",objs[0])
        return render(request,self.template_name,context)
````

Include the pages.urls in the config/urls.py file.

````py
"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include#new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('pages.urls'))#new
]
````

Create the file pages/urls.py

````bash
touch pages/urls.py
````

Link the home template to an URL in the file pages/url.py

````py
from django.urls import path
from .views import HomePageView
urlpatterns=[
path('',HomePageView.as_view(),name='home'),
]
````

Run the server for preview

Now we'll display informations about courses on the home page.

````django
<h1>Database with Django</h1>

<p>There are {{count}} courses registered</p>
<ul>There are:
    {% for course in courses  %}
    <li>{{course.name}}</li>
    {% endfor %}
</ul>
<p>Courses: {{courses}}</p>
<h2>Courses in a table</h2>
<table>
    <tr>
        <th>Name<th>
        <th>Already given?<th>
        <th>Last update<th>
        <th>id<th>
    </tr>
    {% for course in courses  %}
    <tr>
        <td>{{course.name}}<td>
        {% if course.isGiven %}
        <td>Yes<td>
        {% else %}
        <td>No<td>
        {% endif %}
        <td>{{course.lastUpdate}}<td>
        <td>{{course.id}}<td>
    </tr>
    {% endfor %}
</table>
````

### Insertion

We can insert data into database using Django. We can either use file or the Django shell for the code. Syntaxes are the same.

The Django shell is an enhanced version of the Python interpretor, adaptive for Django code.

Run the shell subcommand to use the Django shell:

````bash
python3 manage.py shell
````

Output:

````output
Python 3.10.6 (main, Mar 10 2023, 10:55:28) [GCC 11.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 7.31.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
````

courses=[
    ...: Course(name='Machine Learning', lastUpdate='2023-03-15',isGiven=True),
    ...: Course(name='Artificial Intelligence', lastUpdate='2023-03-15',isGiven=False),
    ...: Course(name='Data Science',isGiven=False, lastUpdate='2023-03-15'),
    ...: Course(name='Project Management', isGiven=True, lastUpdate='2023-03-15')
    ...: ]

courses

for course in courses:
    ...:     course.save()

For a model having Model as class, we have the following methods available on Model.object:

|Method|Description|Return type|
|----|-------|--------|
|````all````|Get all rows of the table|QuerySet|
|````first````|Get the first row of the table|Model|
|````last````|Get the last row of the table|Model|
|````count````|Get the number of rows in the table|int|
|````reverse````|Get all rows  of the table in reverse order|QuerySet|
|````exits````|Return False if the table is empty and True else|bool|
|````get````|Get the row of the table that has the provided value(s) for it's field(s). There must be exactly one match in the table;otherwise exception will be thrown|Model|
|````order_by````|Get the rows of the table in the ascendan or descendent order(if '-' precceeds the field name) order  of the provided field(s).|QuerySet|
|````filter````|Get the rows of the table which provided fields have the specified value(s)|QuerySet|
|````exclude````|The opposite of ````filter````|QuerySet|
|````get_or_create````|Similar to ````get``` but in case of no match, the data is inserted.|tuple(Model,bool); the boolean value is True if the object was inserted and False otherwise.|
|````update````|Update all the provided fields of all rows to the specified values|int(the number of rows updated)|
|````update_or_create````|Similar to ````update``` but in case of no match, the data is inserted.|tuple(Model,bool); the boolean value is True if an object was inserted and False otherwise.|
|````create````|Insert an object to the table. Not error will occur if a constraint  on fields is not respected.|Model(the model inserted)|

### Examples

Get all courses where name is Maths or id=5

````py
Course.objects.filter(name='Maths')| Course.objects.filter(id=5)
````

or use:

````py
from django.db.models import Q
Course.objects.filter(Q(name='Maths')|Q( id=5))
````

Get all courses where the name starts witn Ma

````py
Course.objects.all().filter(name__startswith='Ma')
````

Get all courses where the name ends with e

````py
Course.objects.all().filter(name__endswith='e')
````

Make insensitivesearch by precceding start or end by i

update_or_create(to review)

For a model object  x:

* we can access it's fields using the syntax:

````py
x.field#read
x.field=val#assignment
````

* To update x for example, we have to assign the fields to update and apply the  save method

````py
x.field1=val1
x.field2=val2
x.save()
````

* To delete x we just need to use the delete method

````py
x.delete()
````

It returns a tuple of two items, the first one is the number of object(s) delete and the second one, a dictionary with askeys, the model(s) concerned.

* To insert x into it's model, we'll use the save method:

````py
x.save()
````

The following methods can be applied to QuerySet

|Method|Description|Return type|
|----|-------|--------|
|````values_list````|Make the projection of the current QuerySet object to the fields, specified as strings.|QuerySet|
|````values````|Ruturn the current QuerySet object with dictionnary where keys are fields and values are the values of these fields|QuerySet|

## Model update-Model configuration

To update model, we just need to define or remove fields in our models.py file.

Let's update the course model by removing the lastUpdate field.

````py
from django.db import models
# Create your models here.

#Course model
class Course(models.Model):
    name=models.CharField(max_length=100)# the name of the course
    #lastUpdate=models.DateField()# the date of last update
    isGiven=models.BooleanField()# if the course is already given or not

    def __str__(self):
        return self.name[:10]
````

Then let's make migrations for the app

````bash
python3 manage.py makemigrations pages
````

Output:

````output
Migrations for 'pages':
  pages/migrations/0002_remove_course_lastupdate.py
    - Remove field lastUpdate from course
````

We can optinally preview the migration code:

````bash
python3 manage.py sqlmigrate pages 0002
````

OO02 is the name of our migration.

Output:

````sql
BEGIN;
--
-- Remove field lastUpdate from course
--
ALTER TABLE "pages_course" DROP COLUMN "lastUpdate";
COMMIT;
````

Until now, the lastUpdate field is stil not removed from our Course model:

````py
from pages.models import Course
Course.objects.first().lastUpdate
````

Now we'll apply the migrations and then the field will be effectivelyremoved from the model.

````bash
python3 manage.py migrate pages
````

Output:

````output
Operations to perform:
  Apply all migrations: pages
Running migrations:
  Applying pages.0002_remove_course_lastupdate... OK
````

Let's add a teacher name field to our Course model.

````py
from django.db import models
# Create your models here.

#Course model
class Course(models.Model):
    name=models.CharField(max_length=100)# the name of the course
    #lastUpdate=models.DateField()# the date of last update
    isGiven=models.BooleanField()# if the course is already given or not
    #aded field(s)
    teacher=models.TextField()#the name of the teacher
    def __str__(self):
        return self.name[:10]
````

Now let's make migration file.

```bash
python3 manage.py makemigrations pages
```

We get the following output:

Output:

````bash
It is impossible to add a non-nullable field 'teacher' to course without specifying a default. This is because the database needs something to populate existing rows.
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit and manually define a default value in models.py.
Select an option:
````

With Django, as  model fiels are not null by default, if there are existing rows inside a table and we want to ad one or many fields we have to either  specify a default value for the(option 1) concerned fields in the existing rows or set the fields nullable(option 2).

````bash
Select an option: 1
Please enter the default value as valid Python.
The datetime and django.utils.timezone modules are available, so it is possible to provide e.g. timezone.now as a value.
Type 'exit' to exit this prompt
>>> 'teacher_name'
Migrations for 'pages':
  pages/migrations/0003_course_teacher.py
    - Add field teacher to course
````

With that option, all old teachers rows will have 'teacher_name' as the value of the teacher field.

Now let's apply the migrations:

````bash
python3 manage.py migrate pages
````

Output:

````output
Operations to perform:
  Apply all migrations: pages
Running migrations:
  Applying pages.0003_course_teacher... OK
````

The second option(2) consists to exit. THen we can either speify a default value for the teacher field or set it nullable.

During model definition or update, we can set or change some property about fields. These properties are default arguments that can be passed to the method related to the concerned field.

The table bellow presents the common used.

|Property|Parameters|
|----|-------|
|primary key|````primary_key````|
|foreign key|````foreign_key````|
|unique|````unique````|
|nullable|````null````|
|editable|````editable````|
|index|````db_index````|
|blank|````blank````|
|Create automatically|````auto_create````|
|Check between|````choices````|
|auto increment|````serialize````|
|default value|````default````|

Both these parameters can be True or False except default which represents the default value of a field.

## Most common field method

|Type|Method|
|----|-------|
|Integer|IntgerField, PositiveInteger, BigIntegerField, BigAutoField, FloatField|
|Real number|DecimalField|
|String|CharField, TextField|
|Boolean|BooleanField|
|Date and time|DateField, TimeField, DateTimeFiled|
|Email|EmailField|
|Duration|DurationField   |
|IP address|IPAddressField|
|File|FileField, FilePathField|
|JSON|JSONField|
|Image|ImageField|
|Form|FormField|

## Include templates

With Django, we can include a template inside others, using the include template tag.

Let's have an about template named about.html, a header template named header.html and a footer template named footer.html

````bash
touch templates/about.html
````

````bash
touch templates/header.html
````

````bash
touch templates/footer.html
````

Let's create about pages view in pages/views

````py
class AboutPageView(TemplateView):
    template_name='about.html'
````

Add the URL patter in pages/urls.html

````py
from django.urls import path
from .views import HomePageView,AboutPageView#new
urlpatterns=[
    path('',HomePageView.as_view(),name='home'),
    path('about/',AboutPageView.as_view(),name='about')#new
]
````

Let's include the header and the footer templates in both the home and the about page. Then, the home page will have the following content now:

````html
<h1>Database with Django</h1>

{% include 'header.html' %}

<p>There are {{count}} courses registered</p>
<ul>There are:
    {% for course in courses  %}
    <li>{{course.name}}</li>
    {% endfor %}
</ul>
<p>Courses: {{courses}}</p>
<h2>Courses in a table</h2>
<table>
    <tr>
        <th>Name<th>
        <th>Already given?<th>
        <th>Last update<th>
        <th>id<th>
    </tr>
    {% for course in courses  %}
    <tr>
        <td>{{course.name}}<td>
        {% if course.isGiven %}
        <td>Yes<td>
        {% else %}
        <td>No<td>
        {% endif %}
        <td>{{course.lastUpdate}}<td>
        <td>{{course.id}}<td>
    </tr>
    {% endfor %}
</table>
{% include 'footer.html' %}

````

Let's the about page has the following content:

````html
<h1>About page</h1>
{% include 'header.html' %}
<p>The content of the about page</p>
{% include 'footer.html' %}
````

Now let's run the server

````bash
python3 manage.py runserver
````

Now access 127.0.0.1/8000 and 127.0.0.1/8000/about and confirm everything works properly.

## Static files

In our Django project we may need to add some files sucn as css, javascript images. We need to use what's called static files.

Static files(js,css,img) should be put in a folder called static at the same level as the tempates one.

Create a static folder:

````bash
mkdir static
````

Create a css file inside

````bash
touch static/style.css
````

Then we should specify the location of the static folder  in the config/settings.py file. We should have something looking like:

````py
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / "static",]
````

Add this content:

````css
body{
    background-color: blue;
    font-family: verdana;
}
````

Let's modify our about template to apply it the css property in our static/style.css file.

````django
{% load static %}
<!DOCTYPE html>
<html>
<head>
<link rel="stylesheet" href="{% static 'style.css' %}">
</head>
<body>

<h1>About page</h1>
{% include 'header.html' %}
<p>The content of the about page</p>
{% include 'footer.html' %}

</body>
</html>
````

* load template tag is used to load our static folder
* static template tag is used to load ourstyle.css that's in our static folder.

Now run the server and access 127.0.0.1/8000/about to preview.The CSS property should be applied.

### Static files in production mode

Let's pass to production.

````py
# SECURITY WARNING: don't run with debug turned on in production!
#for debug mode
DEBUG = True
ALLOWED_HOSTS = []
````

DEBUG is True so we are in debug mode for now.

To pass to production mode, modify and get something like:

````py
DEBUG = True
ALLOWED_HOSTS = ['*']
````

ALLOWED_HOSTS represents the list of hosts(computers) our domains that can be served by our server(that can access the server). For now, let it to ````'*'````, meaning any host can access.

Now start the server and you'll remark the style is applied tothe page, because the css file is not found.

To fix that's let's follow the following steps:

* Install whitenoise

Django doesn't provide any way to handle static files in production. In can be done using a third party libray like whitenoise.

Whitenoise is a python library that allows to handle static files. It's can be installed via pip using the following command line:

````bash
pip3 install whitenoise
````

* Now let Django know we need to use whitenoise for static files. To do this, modify the MIDDLEWARE list inside the config/settings.py file.

````py
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',#new
]
````

MIDDLEWARE is the list of the needed third part library.

* Add static root in the config/settings

````py
STATIC_ROOT=BASE_DIR/'production'
````

We can manally create the ./production directory or let it automatically created.

* Collect static files

Now we'll collect static files inside the production directory, using the createstatic sub-command:

````bash
python3 manage.py collectstatic
````

That command all static files, of our project into the production directory. The directory is automatically created if it doesn't exist.

OPen the production directory to prevew. THere are several css,js, images and fonts files inside. There is also our style.css file inside.

Nowrun the server and access 127.0.0.1.8000/about and the css properties should be applied.

The static files finally considered are those inside the production directory. So
static files need to be collected(using the previous command), everytime we create a new static file or update an existing file.

To delete an existing static file, we need to delete it from the static directory and the production one.

## References

### Template tags

| Tag         | Description                                              |
|-------------|----------------------------------------------------------|
| `autoescape`  | Specifies if autoescape mode is on or off                |
| `block`       | Specifies a block section                                 |
| `comment`     | Specifies a comment section                               |
| `csrf_token`  | Protects forms from Cross Site Request Forgeries          |
| `cycle`       | Specifies content to use in each cycle of a loop          |
| `debug`       | Specifies debugging information                           |
| `extends`     | Specifies a parent template                               |
| `filter`      | Filters content before returning it                       |
| `firstof`     | Returns the first not empty variable                      |
| `for`         | Specifies a for loop                                      |
| `if`          | Specifies an if statement                                 |
| `ifchanged`   | Used in for loops. Outputs a block only if a value has changed since the last iteration |
| `include`     | Specifies included content/template                       |
| `load`        | Loads template tags from another library                  |
| `lorem`       | Outputs random text                                       |
| `now`         | Outputs the current date/time                             |
| `regroup`     | Sorts an object by a group                                 |
| `resetcycle`  | Used in cycles. Resets the cycle                           |
| `spaceless`   | Removes whitespace between HTML tags                      |
| `templatetag` | Outputs a specified template tag                           |
| `url`         | Returns the absolute URL part of a URL                     |
| `verbatim`    | Specifies contents that should not be rendered by the template engine |
| `widthratio`  | Calculates a width value based on the ratio between a given value and a max value |
| `with`        | Specifies a variable to use in the block                   |

### Field lookups

| Keyword     | Description                                           |
|-------------|-------------------------------------------------------|
| `contains`    | Contains the phrase                                    |
| `icontains`   | Same as contains, but case-insensitive                 |
| `date`        | Matches a date                                         |
| `day`         | Matches a date (day of month, 1-31) (for dates)         |
| `endswith`    | Ends with                                              |
| `iendswith`   | Same as endswith, but case-insensitive                 |
| `exact`       | An exact match                                         |
| `iexact`      | Same as exact, but case-insensitive                     |
| `in`          | Matches one of the values                              |
| `isnull`      | Matches NULL values                                    |
| `gt`          | Greater than                                           |
| `gte`         | Greater than, or equal to                               |
| `hour`        | Matches an hour (for datetimes)                         |
| `lt`          | Less than                                              |
| `lte`         | Less than, or equal to                                  |
| `minute`      | Matches a minute (for datetimes)                        |
| `month`       | Matches a month (for dates)                             |
| `quarter`     | Matches a quarter of the year (1-4) (for dates)         |
| `range`       | Match between                                          |
| `regex`       | Matches a regular expression                            |
| `iregex`      | Same as regex, but case-insensitive                     |
| `second`      | Matches a second (for datetimes)                        |
| `startswith`  | Starts with                                            |
| `istartswith` | Same as startswith, but case-insensitive                |
| `time`        | Matches a time (for datetimes)                          |
| `week`        | Matches a week number (1-53) (for dates)                 |
| `week_day`    | Matches a day of week (1-7) 1 is sunday                  |
| `iso_week_day`| Matches a ISO 8601 day of week (1-7) 1 is monday         |
| `year`        | Matches a year (for dates)                              |
| `iso_year`    | Matches an ISO 8601 year (for dates)                     |

### Filter keywords

| Keyword            | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| `add`                | Adds a specified value.                                                                                       |
| `addslashes`        | Adds a slash before any quote characters, to escape strings.                                                  |
| `capfirst`           | Returns the first letter in uppercase.                                                                        |
| `center`             | Centers the value in the middle of a specified width.                                                         |
| `cut`                | Removes any specified character or phrases.                                                                   |
| `date`               | Returns dates in the specified format.                                                                        |
| `default`            | Returns a specified value if the value is False.                                                              |
| `default_if_none`    | Returns a specified value if the value is None.                                                               |
| `dictsort`           | Sorts a dictionary by the given value.                                                                        |
| `dictsortreversed`   | Sorts a dictionary reversed, by the given value.                                                              |
| `divisibleby`        | Returns True if the value can be divided by the specified number, otherwise it returns False.                |
| `escape`             | Escapes HTML code from a string.                                                                              |
| `escapejs`           | Escapes JavaScript code from a string.                                                                        |
| `filesizeformat`     | Returns a number into a file size format.                                                                     |
| `first`              | Returns the first item of an object (for Strings, the first character is returned).                           |
| `floatformat`        | Rounds floating numbers to a specified number of decimals, default one decimal.                              |
| `force_escape`       | Escapes HTML code from a string.                                                                              |
| `get_digit`          | Returns a specific digit of a number.                                                                         |
| `iriencode`          | Convert an IRI into a URL friendly string.                                                                    |
| `join`               | Returns the items of a list into a string.                                                                    |
| `json_script`        | Returns an object into a JSON object surrounded by \<script\>\</script\> tags.                                   |
| `last`               | Returns the last item of an object (for Strings, the last character is returned).                            |
| `length`             | Returns the number of items in an object, or the number of characters in a string.                           |
| `length_is`          | Returns True if the length is the same as the specified number                                                |
| `linebreaks`         | Returns the text with \<br> instead of line breaks, and \<p> instead of more than one line break.               |
| `linebreaksbr`       | Returns the text with \<br> instead of line breaks.                                                            |
| `linenumbers`        | Returns the text with line numbers for each line.                                                             |
| `ljust`              | Left aligns the value according to a specified width                                                           |
| `lower`              | Returns the text in lower case
| `make_list` | Converts a value into a list object. |
| `phone2numeric` | Converts phone numbers with letters into numeric phone numbers. |
| `pluralize` | Adds a 's' at the end of a value if the specified numeric value is not 1. |
| `pprint` |  |
| `random` | Returns a random item of an object. |
| `rjust` | Right aligns the value according to a specified width. |
| `safe` | Marks that this text is safe and should not be HTML escaped. |
| `safeseq` | Marks each item of an object as safe and the item should not be HTML escaped. |
| `slice` | Returns a specified slice of a text or object. |
| `slugify` | Converts text into one long alphanumeric-lower-case word. |
| `stringformat` | Converts the value into a specified format. |
| `striptags` | Removes HTML tags from a text. |
| `time` | Returns a time in the specified format. |
| `timesince` | Returns the difference between two datetimes. |
| `timeuntil` | Returns the difference between two datetimes. |
| `title` | Upper cases the first character of each word in a text, all other characters are converted to lower case. |
| `truncatechars` | Shortens a string into the specified number of characters. |
| `truncatechars_html` | Shortens a string into the specified number of characters, not considering the length of any HTML tags. |
| `truncatewords` | Shortens a string into the specified number of words. |
| `truncatewords_html` | Shortens a string into the specified number of words, not considering any HTML tags. |
| `unordered_list` | Returns the items of an object as an unordered HTML list. |
| `upper` | Returns the text in upper case letters. |
| `urlencode` | URL encodes a string. |
| `urlize` | Returns any URLs in a string as HTML links. |
| `urlizetrunc` | Returns any URLs in a string as HTML links, but shortens the links into the specified number of characters. |
| `wordcount` | Returns the number of words in a text. |
| `wordwrap` | Wrap words at a specified number of characters. |
| `yesno` | Converts Booleans values into specified values. |
| `i18n` | A template tag for internationalization. |
| `l10n` | A template tag for localization. |
| `tz` | A template tag for time zones. |
