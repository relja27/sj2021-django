from django.shortcuts import render
from .forms import *


def dash(request):
    student = Student.objects.all()
    vaccine = Vaccine.objects.all()
    return render(request, 'rafvaxx/dashboard.html', {'student': student, 'vaccine': vaccine})

def student(request):
    student = Student.objects.all()
    total_student = student.count()
    procenat = total_student / 50 * 100
    return render(request, 'rafvaxx/student.html', {'student': student, 'total_student': total_student, 'procenat': procenat})

def vaccine(request):
    vaccine = Vaccine.objects.all()
    student = Student.objects.all()
    increment = 0
    return render(request, 'rafvaxx/vaccine.html', {'vaccine': vaccine, 'student':student, 'increment':increment})

def user(request):
    user = User.objects.all()
    return render(request, 'rafvaxx/user.html', {'user': user})