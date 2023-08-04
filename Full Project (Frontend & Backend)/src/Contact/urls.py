from django.urls import path
from. import views

urlpatterns = [
    path('', views.Contact, name='contact'),
    path('message_send/', views.Contact_, name='contactus'),
]