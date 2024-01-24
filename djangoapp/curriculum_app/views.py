from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request,'site/home.html')

def skills(request):
    return render(request,'site/skills.html')

def projects(request):
    return render(request,'site/projects.html')

def about_me(request):
    return render(request,'site/about_me.html')

def contact(request):
    return render(request,'site/contact.html')

