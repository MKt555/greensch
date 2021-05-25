from django import forms

from django.contrib.auth.forms import UserCreationForm
from .models import User, Student, Tutor
from django.db import transaction

class StudentSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    School = forms.CharField(required = True)
    Level = forms.CharField(required = True)
    Certification = forms.CharField(required = True)
    Course = forms.CharField(required = True)
    registration_number = forms.CharField(required = True)

    class Meta(UserCreationForm):
        model = User
        fields = ('School','Level','Certification', 'Course')
   
    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_student = True
        user.is_staff = False
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Student = Student.objects.create(user=user)
        student.School = self.cleaned_data.get('School')
        student.Level = self.cleaned_data.get('Level')
        student.Certification =self.cleaned_data.get('Certification')
        student.Course = self.cleaned_data.get('Course')
        student.registration_number = self.cleaned_data.get('registration_number')
        student.save()
        return Student


class TutorSignUpForm(UserCreationForm):
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required = True)
    Title = forms.CharField(required = True)
    Department = forms.CharField(required = True)
    Units = forms.CharField(required = True)
    About = forms.CharField(required = True)
    #payroll_no = forms.CharField(required = True)

    class Meta(UserCreationForm):
        model = User
        fields = ('Department', 'Units')

    @transaction.atomic
    def save(self):
        user = super().save(commit = False)
        user.is_tutor = True
        user.is_tutor = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        Tutor = Tutor.objects.create(user=user)
        Tutor.Department = self.cleaned_data.get('Department')
        Tutor.Units = self.cleaned_data.get('Units')
        Tutor.save()
        return Tutor