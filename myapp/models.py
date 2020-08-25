from django.db import models

# Create your models here.
class Employee(models.Model):
    eid=models.CharField(max_length=50)
    ename=models.CharField(max_length=500)
    eemail=models.EmailField()
    econtact=models.CharField(max_length=200)

class Register(models.Model):
    Name=models.CharField(max_length=100)
    Roll=models.IntegerField(max_length=100)

class Group(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(max_length=50)
    group=models.CharField(max_length=50)
    contact=models.IntegerField(max_length=100)
    