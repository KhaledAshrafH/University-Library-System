from django.contrib import messages,auth
from django.shortcuts import render,get_object_or_404,redirect
from .models import Profile
from django.contrib.auth.models import User
from django.http import HttpResponse
from Book.models import Book

# Create your views here.

def Register(request):
    if request.method == 'POST':

        firstName = None,
        lastname = None,
        Email = None,
        UserName = None,
        gender=None,
        date_of_login=None,
        phone=None,
        city=None,
        Kind=None,
        userprofile=None

        password =request.POST['password']
        firstName = request.POST['firstName']
        lastname = request.POST['lastname']
        UserName = request.POST['Username']
        gender = request.POST['gender']
        Email = request.POST['Email']
        phone = request.POST['phone']
        city = request.POST['city']

        if User.objects.filter(username = UserName).exists():
            messages.error(request, "error")

        else:
            user = User.objects.create_user(
                first_name=firstName,
                last_name=lastname,
                email=Email,
                username=UserName,
                password=password,
            )
            user.save()
            p = Profile(
                user=user,
                gender=gender,
                phone=phone,
                city=city,
          )
            p.save()
            return redirect('../')
    return render(request, 'Register.html')





def Prof (request):
    if request.method =='POST' and 'btn' in request.POST:
        if request.user is not None and request.user.id !=None:
            p = Profile.objects.get(user = request.user)
            
            if request.POST['firstName'] and request.POST['lastname'] and request.POST['password'] and request.POST['city']and request.POST['phone']:
                request.user.first_name = request.POST['firstName']
                request.user.last_name = request.POST['lastname']

                p.phone=request.POST['phone']
                p.city=request.POST['city']

                if not request.POST['password'].startswith('pbkdf2_sha256$'):
                    request.user.set_password(request.POST['password'])
                request.user.save()
                p.save()
                
                auth.login(request, request.user)
                return redirect('home')
        return redirect('profile')
    else:
        if request.user.is_anonymous: return redirect('home')
        if request.user is not None:
            p = Profile.objects.get( user = request.user)
            x ={
                'firstName':request.user.first_name,
                'lastname':request.user.last_name,
                'user':request.user.username,
                'password':request.user.password,
                'city': p.city,
                'phone': p.phone
            }
            return render(request, 'profile.html',x)
        else:return redirect('profile')
