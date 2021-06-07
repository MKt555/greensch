from django.urls import path
from . import views

urlpatterns = [
    #path('', register, name = "registration"),
    path('register/', views.register , name = 'Register'),
    path('student_registration/', views.student_registration.as_view(), name = 'student_registration'),
    path('tutor_registration/', views.tutor_registration.as_view(), name = 'tutor_registration'),
    #path('login/', views.login_view, name = 'login'),
    path('student_login/', views.student_login_request.as_view(), name = 'student_login'),
    path('tutor_login/', views.tutor_login_request.as_view(), name = 'tutor_login'),
    path('logout/', views.logout_request, name = 'logout'),
    #path('studentpage/', views.studentpageview, name = 'Student Page'),
    #path('tutorpage/', views.tutorpageView, name = 'Tutor Page'),
]
