from django.db import models
# Create your models here.

class Contact_Form (models.Model):
    name = models.CharField(max_length=50)
    email =models.CharField(max_length=100)
    subject = models.CharField(max_length=120)
    message = models.TextField()

    def __str__(self):
        return self.subject