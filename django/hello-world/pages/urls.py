#pages/urls.py
from django.urls import path
from .views import homePageView,exampleView#new
urlpatterns = [
path('',homePageView,name='home'),
path('example/',exampleView),#new
]
