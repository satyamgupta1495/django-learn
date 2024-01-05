from django.shortcuts import render
from myclassroom.models import Student
from rest_framework import viewsets
from myclassroom.serializers import StudentSerializer
import requests

# Create your views here.

class StudentsViewSet(viewsets.ModelViewSet):   
    queryset= Student.objects.all()
    serializer_class = StudentSerializer

def student_table(request):
    api_url = 'http://127.0.0.1:8000/api/v1/students/'
    response = requests.get(api_url)
    students = response.json()

    return render(request, 'Student.html', {'students': students})
# def home(request):    
#     rooms = ClassRoom.objects.all()
#     context = {'rooms': rooms}
#     return render(request, 'Home.html', context)

# def students(request):   
#     student = Student.objects.all() 
#     context = {'students': student}
#     return render(request, 'Student.html', context)


# def room(request, pk):
#     room = None
#     for i in rooms:
#         if i.id == int(pk):
#             room = i
    
#     context = {'room': room}

#     return render(request, 'Room.html', context)

# def contact(request):
#     return render(request, 'Contact us page')
