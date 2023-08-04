from django.urls import path
from. import views

urlpatterns = [
    path('', views.All_Books, name='shop'),
    path('<int:Book_id>/', views.One_Book, name='Book'),
    path('<int:Book_id>/Borrow/', views.BookBorrow, name = 'BookBorrow'),
    path('<int:Book_id>/Return/', views.Return_Book, name = 'Return_Book'),
]