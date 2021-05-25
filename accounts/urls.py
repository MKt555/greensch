from django.urls import path
from . import views

urlpatterns = [
    #path('', register, name = "registration"),
    path('register/', views.register , name = 'Register'),
    path('student_registration/', views.student_registration.as_view(), name = 'student_registration'),
    path('tutor_registration/', views.tutor_registration.as_view(), name = 'tutor_registration'),
]
