from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth

# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST['Username']
        password =request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
           # messages.success(request, "You are Successfully login")
        else:
            messages.error(request,"Username or Password not correct")
        return redirect('home')
    return render(request, 'login.html')