from django.contrib.auth import login
#from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.views.generic import TemplateView


from .models import User
from .forms import (
    StudentSignUpForm, 
    TutorSignUpForm, StudentLoginForm, TutorLoginForm
) 

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.


def register(request):
    if request.user.is_authenticated:
        if request.user.is_tutor:
            return redirect("tutor_registration.html")
        if request.user.is_student:
            return redirect("student_registration.html")
    return render(request, "register.html")



def student_registration(request):#POST request
    if request.method == "POST":
        form  = StudentSignUpForm(request.POST)#UserCreationForm populated by POST request
        if form.is_valid():
            User = form.save()
            Level = form.cleaned_data.get('Level')
            Certification = form.cleaned_data.get('Certification')
            Course = form.cleaned_data.get('Course')
            registration_number = form.cleaned_data.get('registration_number')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            messages.success(request, f"New Account Created:{first_name, last_name}")
            login(request, User)
            return redirect("academy.html")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")
#GET request
    form = StudentSignUpForm
    return render(request, 
            "student_registration.html",
            {"student_signup_form":form}) 



def tutor_registration(request):
    if request.method == "POST":
        form  = TutorSignUpForm(request.POST)#UserCreationForm populated by POST request
        if form.is_valid():
            User = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            Department = form.cleaned_data.get('Department')
            Units = form.cleaned_data.get('Units')
            About = form.cleaned_data.get('About')
            Academic_credentials = form.cleaned_data.get('Academic Credentials')
            messages.success(request, f"New Account Created:{first_name, last_name}")
            login(request, User)
            return redirect("academy.html")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")
#GET request
    form = TutorSignUpForm
    return render(request, 
            "tutor_registration.html",
            {"tutor_signup_form":form})


def login_view(request):
    print(request.headers)
    return render(request, "login.html", {})

def student_login_request(request):
    context = {}
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            registration_number = request.POST['registration_number']
            password = request.POST['password'] 
            user = authenticate(request, registration_number=registration_number, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {registration_number}")
                return redirect('studentpage.html')
            else:
                messages.error(request, "Invalid username or password.")
 #It's a GET request 
    else:
        form = StudentLoginForm()
        context={"student_login_form":form}
    return render(request, "student_login.html", context)


def tutor_login_request(request):
    context = {}
    if request.method == 'POST':
        form = TutorLoginForm(request.POST)
        if form.is_valid():
            email= request.POST['email']
            password = request.POST['password'] 
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}")
                return redirect('tutorpage.html')
        else:
            messages.error(request, "Invalid username or password.")
#It's a GET request   
    else:
            form = TutorLoginForm()
            context={"tutor_login_form":form}
    return render(request, "tutor_login.html", context)


def logout_request(request):
    logout(request)
    messages.info(request, "Log Out Successfully!")
    return redirect("accounts/register.html")



#def tutorpageView(request)
#def studentpageview(request)