from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import  Student, User, Tutor
from academy.models import Course
from django.db import transaction

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    School = forms.CharField(required = True)
    Level = forms.CharField(required = True)
    Certification = forms.CharField(required = True)
    Course = forms.CharField(required = True)
    registration_number = forms.CharField(required = True)
    email = forms.EmailField(required = True)


    class Meta(UserCreationForm):
        model = User
        fields = ('School','Level','Certification', 'Course', 'registration_number', 'email', 'password')


    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_student = True
        user.is_staff = False
        user.get_full_name = self.cleaned_data.get('Name')
        user.save()
        Student = Student.objects.create(user=user)
        Student.School = self.cleaned_data.get('School')
        Student.Level = self.cleaned_data.get('Level')
        Student.Certification =self.cleaned_data.get('Certification')
        Student.Course = self.cleaned_data.get('Course')
        Student.Course.generate_registration_number = self.cleaned_data.get('registration_number')
        Student.email=self.cleaned_data.get('email')
        Student.password = self.cleaned_data.get('password')
        Student.save()
        return Student


class TutorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    Title = forms.CharField(required = True)
    Department = forms.CharField(required = True)
    Units = forms.CharField(required = True)
    About = forms.CharField(required = True)
    Academic_credentials = forms.CharField(required = True)
    email = forms.EmailField(required = True)
    #payroll_no = forms.CharField(required = True)

    class Meta(UserCreationForm):
        model = User
        fields = ('Department', 'Units', 'Academic_credentials', 'password')

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_tutor = True
        user.is_tutor = True
        user.get_full_name = self.cleaned_data.get('Name')
        user.save()
        Tutor = Tutor.objects.create(user=user)
        Tutor.Department = self.cleaned_data.get('Department')
        Tutor.Units = self.cleaned_data.get('Units')
        Tutor.email=self.cleaned_data.get('email')
        Tutor.password=self.cleaned_data.get('password')
        Tutor.save()
        return Tutor