# Create your views here.

from django.http import HttpResponse

def homePageView(request):
    #print("Hello bro")
    #print(request)
    #print(type(request))
    #print(dir(request))
    return HttpResponse('Hello world')

def exampleView(request):
    print('Just an example')
    return HttpResponse('This is another example')