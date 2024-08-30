from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html',context={})
def contact(request):
    return render(request, 'contact.html',context={})
def login(request):
    return render(request, 'login.html',context={})
def mission(request):
    return render(request,'mission.html',context={})
def help(request):
    return render(request,'help.html',context={})
def news(request):
    return render(request,'news.html',context={})