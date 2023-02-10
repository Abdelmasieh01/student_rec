from django.shortcuts import render
from .models import Student

def index(request):
    return render(request, 'main/index.html',)

def student_list(request):
    students = Student.objects.all()
    return render(request, 'main/tables.html', {'items': students})



