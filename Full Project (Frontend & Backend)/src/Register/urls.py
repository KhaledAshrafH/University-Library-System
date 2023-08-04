from django.urls import path
from. import views

urlpatterns = [
    path('', views.Register, name = 'Register'),
    path('profile/', views.Prof, name = 'profile'),
]