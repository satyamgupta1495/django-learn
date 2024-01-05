from django.db import models

# Create your models here.
class ClassRoom(models.Model):
    name = models.CharField(max_length=200,null=False)
    desc = models.TextField(null=True, blank=True)
    no_of_students = models.IntegerField(null=False)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

class Student(models.Model):
    roll_no = models.IntegerField(null=False)
    first_name = models.CharField(max_length=20,null=False)
    last_name = models.CharField(max_length=20,null=False)
    className = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    email  = models.CharField(max_length=30,null=False)
    contact_number = models.CharField(max_length=15, null=True, blank=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    
