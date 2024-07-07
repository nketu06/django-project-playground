from django.db import models

# Create your models here.

class Student(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=30)
    isPass=models.BooleanField()
    comment= models.CharField(max_length=40,default="No Comment")
