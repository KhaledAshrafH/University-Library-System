from django.shortcuts import render,redirect
from .models import Contact_Form
# Create your views here.

def Contact(request):
    print('firstssssss')
    return render(request,'contact.html')


def Contact_ (request):
    print('____first____')
    #user = get_object_or_404(User)
    if request.method == 'POST':
        name=None
        email=None
        subject=None
        message=None

        print('second')

        name =request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        print('second')

        contact =Contact_Form.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message,
        )

        print('second')
        contact.save()
        return redirect('home')
    return render(request, 'contact.html')
