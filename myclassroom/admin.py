from django.contrib import admin

# Register your models here.

from .models import ClassRoom, Student

admin.site.register(ClassRoom)
admin.site.register(Student)
