from django.db import models
# Create your models here.
from Register.models import Profile

class Book (models.Model):

    price = models.IntegerField(null=False)
    name_Book = models.CharField(max_length=100, null=False)
    author = models.CharField(max_length=150, null=False)
    ISBN = models.CharField(max_length=25, null=False)
    Image = models.ImageField(upload_to = "photoes/%y/%m/%d", null=False)
    pages = models.IntegerField(null=False)
    description = models.TextField(null=False)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    #time = models.DateField(auto_now=False, auto_now_add=False, blank=True, null=True)
    active = models.BooleanField(default=True)

    user = models.ForeignKey(Profile, on_delete = models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.ISBN
