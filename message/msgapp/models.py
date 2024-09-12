from django.db import models

# Create your models here.
class Message(models.Model):
    name=models.CharField(max_length=20) #charfiled is function inside models class
    mob=models.CharField(max_length=10)
    email=models.EmailField(max_length=100)
    msg=models.CharField(max_length=300)
