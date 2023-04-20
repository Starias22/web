from django.shortcuts import render

# Create your views here.
# pages/views.py
from django.views.generic import TemplateView
class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name='about.html'

class SyntaxView(TemplateView):
    template_name='syntax.html'

    def get(self,request):
        context={'hello':"Hello world",
                'how':"How are you?",
                'age':25,
                'fruits':['orange','mango','pineapple','apple']}
        return render(request,self.template_name,context)

class ParamView(TemplateView):
    template_name='param.html'
    def get(self,request,val):
        context=dict()
        if id<18:
            context['content']='Your are not authorized!'
        else:
            context['content']='Congratulations!'
        return  render(request,self.template_name,context)

class BoolView(TemplateView):
    template_name='bool.html'
    def get(self,request,val):
        context=dict()
        context['val']=val
        return  render(request,self.template_name,context)
