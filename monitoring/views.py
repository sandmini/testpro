from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse
# Create your views here.
class HomePageView(TemplateView):
     def  get(self,request,**kwargs):
          return render(request, 'index.html', context=None)

def index(request):
    if request.method == 'POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       context = {
           'username':username,
           'password':password
       }
       template = loader.get_template('home.html')
       return HttpResponse(template.render(context,request))

    else:
        template = loader.get_template('index.html')
        return HttpResponse(template.render())

def home(request):
    return render(request,'home.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def report(request):
    return render(request,'report.html')