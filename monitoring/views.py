from django.shortcuts import render
from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'home.html')

def home(request):
    return render(request,'home.html')

def page2(request):
    return render(request,'page2.html')

def page3(request):
    return render(request,'page3.html')

def report(request):
    return render(request,'report.html')

def login(request):
    return render(request,'home.html')
