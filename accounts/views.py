from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from .models import User
from .forms import (
    StudentSignUpForm, 
    TutorSignUpForm,
) 

from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

from django.http import HttpResponse
# Create your views here.
def student_registration(request):#POST request
    if request.method == "POST":
        form  = StudentSignUpForm(request.POST)#UserCreationForm populated by POST request
        if form.is_valid():
            User = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            Level = form.cleaned_data.get('Level')
            Certification = form.cleaned_data.get('Certification')
            Course = form.cleaned_data.get('Course')
            registration_number = form.cleaned_data.get('registration_number')
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
                  "register.html",
                  {"form":form})#references register.html
#context is used to get some values or variables from the database

def tutor_registration(request):#POST request
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
                  "register.html",
                  {"form":form})#references register.html
#context is used to get some values or variables from the database
def login_view(request):
    print(request.headers)
    return render(request, "login.html", {})
#Attempting to build different login forms for each user type, i.e student and tutor
#Still working on this.
def student_login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            registration_number = form.cleaned_data.get('registration_number')
            password = form.cleaned_data.get('password')
            user = authenticate(registration_number=registration_number, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {registration_number}")
                return redirect('studentpage.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = ",/student_login.html",
                    context={"form":form})

def tutor_login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(email = email, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {email}")
                return redirect('tutorpage.html')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request = request,
                    template_name = "./tutor_login.html",
                    context={"form":form})


def logout_request(request):
    logout(request)
    messages.info(request, "Log Out Successfully!")
    return redirect("accounts/register.html")


class student_registration(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = './student_registration.html'


class tutor_registration(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = './tutor_registration.html'

class student_login_request(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = './student_login.html'

class student_login_request(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = './tutor_login.html'

#def tutorpageView(request)
#def studentpageview(request)