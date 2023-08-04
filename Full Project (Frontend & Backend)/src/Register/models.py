import sys
sys.path.append("..")
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile (models.Model):

    select = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=25, null=False, choices=select)
    date_of_login = models.CharField(max_length=50)
    phone = models.CharField(max_length=11)
    city = models.CharField(max_length=50)
    userprofile = models.ImageField(upload_to = "photoes/%y/%m/%d", null=False)

    def __str__(self):
        return self.user.username
