from django.shortcuts import render

# Create your views here.

def Profile(request):
    return render(request,'Profile/Profile.html')