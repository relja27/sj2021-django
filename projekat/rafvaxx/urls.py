from django.urls import path

from . import views

app_name = 'rafvaxx'

urlpatterns = [
    path('', views.dash, name='dashboard'),
    path('dash', views.dash, name='dashboard'),
    path('student', views.student, name='student'),
    path('vaccine', views.vaccine, name='vaccine'),
    path('user', views.user, name='user'),
]