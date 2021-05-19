from django.db import models

# Create your models here.
class Contact(models.Model) :
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField()
    mobileNo = models.CharField(max_length=12)
    message = models.TextField()