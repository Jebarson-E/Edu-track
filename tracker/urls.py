from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.user_register, name='register'),
    path('', views.home, name='home'),
    path('add_student/', views.add_student, name='add_student'),
    path('record_attendance/', views.record_attendance, name='record_attendance'),
    path('record_marks/', views.record_marks, name='record_marks'),
    path('record_behavior/', views.record_behavior, name='record_behavior'),
    path('reports/', views.reports, name='reports'),
]
