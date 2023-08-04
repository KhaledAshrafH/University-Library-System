from django.shortcuts import render, get_object_or_404, redirect,HttpResponse
from django.contrib import messages
from .models import Book
from Register.models import Profile
# Create your views here.

def One_Book (request, Book_id):
    #OneBook = Book.objects.get(pk=Book_id)
    OneBook = get_object_or_404(Book, pk = Book_id)
    #print(OneBook.name_Book)

    content = {'Name': OneBook.name_Book,
     'Image': OneBook.Image,
     'pages': OneBook.pages,
     'active':OneBook.active,
     'Author':OneBook.author,
     'description':OneBook.description,
     'time':OneBook.time,
     'price':OneBook.price,
      'id':OneBook.id,
     'user':str(OneBook.user)
             }

    print ('this is ')
    return render(request, 'bookUser.html', {'content': content})





def All_Books(request):
    I=Book.objects.all()
    ISBN = None
    author=None
    name_Book=None

    if 'search' in request.POST:

        rad_option = str(request.POST["searc"])
        if rad_option == 'BookName':
            print(rad_option)
            name_Book = request.POST['search']
            if name_Book:
                I = I.filter(name_Book__icontains=name_Book)

        if rad_option =='Author':
            print(rad_option)
            author = request.POST['search']
            if author:
                I = I.filter(author__icontains=author)

        if rad_option == 'ISBN':
            print(rad_option)
            ISBN = request.POST['search']
            if ISBN:
                I = I.filter(ISBN__icontains=ISBN)
    return render(request, 'shop.html', {'Books':  I.order_by('-time')})



'''
def Bookfavorite(request, Book_id):
    print(Book_id)
    print('ahmedsayedahmedsayedahmedsayed')
    if request.user.is_authenticated and not request.user.is_anonymous:
        book_fav = Book.objects.get(pk=Book_id)
        if Profile.objects.filter(user = request.user, Book_vaforite = book_fav).exists():
            messages.success(request,'already added recently')
            print('pppp')
            return HttpResponse(request,"already added recently ")

        else:
            p = Profile.objects.get(user=request.user)
            p.Book_vaforite.add(book_fav)
            messages.success(request,'added')
            print('ahmedsayed')
    else:
        print('here')
        return messages(request,"you must be login")
    return redirect('/Books/' + str(Book_id))
'''

def BookBorrow(request, Book_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        book_Borrow = Book.objects.get(pk=int(Book_id))
        userr = Profile.objects.get(user=request.user)
        print(userr)

        book_Borrow.user = userr
        book_Borrow.active = False
        book_Borrow.save()
        print(book_Borrow)

        return redirect('home')
    return render(request,'bookUser.html',)


def Return_Book(request,Book_id):
    if request.user.is_authenticated and not request.user.is_anonymous:
        book_Return = Book.objects.get(pk=int(Book_id))
        book_Return.active = True
        book_Return.save()
        print(book_Return)
        return redirect('home')
    return render(request,'bookUser.html',)