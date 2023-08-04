from django.urls import path
from. import views

urlpatterns = [
    path('', views.Logout, name='Logout'),
]