from django.shortcuts import render
from .models import Student
from .serializers import StudenSerializer
from rest_framework import viewsets

# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class =  StudenSerializer
    
    

