from django.urls import path
from. import views


urlpatterns = [
    path('', views.Home, name='home'),
    path('admin_Controller', views.admin_Controller, name='admin_Controller'),
    path('admin_Controller/<int:id>/', views.edit, name='edit')
]