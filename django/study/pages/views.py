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

class AboutPageView(TemplateView):
    template_name='about.html'