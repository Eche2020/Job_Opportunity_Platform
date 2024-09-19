# jobs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('job_list/', views.job_list, name='job_list'),
    path('job/', views.job_detail, name='job_detail'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login, name='login'),
    path('signIn/', views.signIn, name='signIn'),
]
