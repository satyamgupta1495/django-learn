from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'students', views.StudentsViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('student-table/', views.student_table, name='student_table'),

]
