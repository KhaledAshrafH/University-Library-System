from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from Book.models import Book
from .forms import FormsModel
# Create your views here.

def Home(request):
    return render(request, 'home.html',{'Books':  Book.objects.all().order_by('-time')})




def admin_Controller(request):
    if request.method=='POST':
        addBook =FormsModel(request.POST, request.FILES)
        if addBook.is_valid():
            addBook.save()

    context={
        'form':FormsModel()
    }
    return render(request, 'book.html',context)

def edit(request,id):
    Book_id=Book.objects.get(id=id)
    if request.method=='POST':
        Book_Save = FormsModel(request.POST,request.FILES,instance= Book_id)
        if Book_Save.is_valid():
            Book_Save.save()
    else:
        Book_Save =FormsModel(instance=Book_id)
    context ={
        'form':Book_Save,
    }
    
    return render(request, 'editBook.html', context)