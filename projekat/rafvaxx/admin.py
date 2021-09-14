from django.contrib import admin

# Register your models here.
from .models import Student,Vaccine

admin.site.register(Student)
admin.site.register(Vaccine)