from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import User
from .forms import (
    StudentSignUpForm, 
    TutorSignUpForm,
) 

from django.views.generic import CreateView
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
def register(request):
    if request.method == "POST":
        form  = UserCreationForm(request.POST)
        if form.is_valid():
            User = form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f"New Account Created:{first_name, last_name}")
            login(request, User)
            return redirect("academy.html")

        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg} : {form.error_messages[msg]}")

    form = UserCreationForm
    return render(request, 
                  "register.html",
                  {"form":form})#references home.html
#context is used to get some values or variables from the database

class student_registration(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = './student_registration.html'


class tutor_registration(CreateView):
    model = User
    form_class = TutorSignUpForm
    template_name = './tutor_registration.html'
