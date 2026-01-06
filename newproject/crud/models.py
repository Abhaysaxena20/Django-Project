from django.db import models

# Create your models here.
class Student(models.Model):
    id = models.AutoField(primary_key=True)
    roll = models.CharField(max_length=10, unique=True)
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=150)
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=10)
    