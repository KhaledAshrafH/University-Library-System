from django.shortcuts import render,redirect
from django.contrib import auth
# Create your views here.


def Logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect('home')