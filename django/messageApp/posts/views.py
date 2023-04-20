from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class homePageView(ListView):
    model=Post
    template_name='home.html'
    print('count:',Post.objects.count())
    #Post.objects.create(text='fine insertion')#insertion
    #print('selection:',Post.objects.select_related())
    x=Post.objects.select_related()
    y=list(x)
    print(y)
    print(type(y[0]))
    z=str(y[0])
    print(z)
    #print('projection:',Post.objects.select_related('text'))
    print('last post:',Post.objects.last())
    Post.objects.first()
    print(Post.objects.all())
    #print( str(Post.objects.db()))
    print(Post.objects.exists())
