# pages/urls.py
from django.urls import path
from .views import AboutPageView, BoolView, HomePageView, ParamView, SyntaxView,BoolView
urlpatterns = [
path('about/',AboutPageView.as_view(),name='about'),
path('', HomePageView.as_view(), name='home'),
path('syntax/',SyntaxView.as_view(),name='syntax'),
path('param/<int:id>',ParamView.as_view(),name="param"),
path('syntax/<int:val>',BoolView.as_view(),name='bool')
]