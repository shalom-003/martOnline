from django.contrib.auth.views import LoginView
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Member
from django.contrib import messages
def home(request):
    return render(request, "mart/home.html")

def products(request):
    return render(request,"mart/products.html")

def categories(request):
    return render(request,'mart/categories.html')

def about(request):
    return render(request,'mart/about.html')

def contact(request):
    return render(request,'mart/contact.html')

def dashboard(request):
    return render(request,'mart/dashboard.html')

class MyLoginView(LoginView):
    template_name = 'mart/dashboard.html'

def dashboard(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')

        #checking username if it exists in the database
        if Member.objects.filter(username=username).exists():    
            messages.error(request,"username already taken!")
            return render(request,'mart/dashboard.html')
       
         
         #check email if it exist in the database
        if Member.objects.filter(email=email).exists():
            messages.error(request,"email already taken")
            return render(request,'mart/dashboard.html')<  Member.objects.create(username = username,password = password,email = email)
    
        return render(request,'mart/home.html')
        
    return render(request,'mart/home.html')
        