from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate

from .models import User

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
        user.first_name = self.cleaned_data.get('First Name')
        user.last_name = self.cleaned_data.get('Last Name')
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
        user.first_name = self.cleaned_data.get('First Name')
        user.last_name = self.cleaned_data.get('Last Name')
        user.save()
        Tutor = Tutor.objects.create(user=user)
        Tutor.Department = self.cleaned_data.get('Department')
        Tutor.Units = self.cleaned_data.get('Units')
        Tutor.email=self.cleaned_data.get('email')
        Tutor.password=self.cleaned_data.get('password')
        Tutor.save()
        return Tutor


class StudentLoginForm(forms.ModelForm):
    registration_number = forms.CharField(label = 'Registration Number', widget=forms.TextInput)
    password = forms.CharField(label ='Password', widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ('registration_number', 'password')

    def clean(self):
        if self.is_valid():
            registration_number = self.cleaned_data['registration_number']
            password = self.cleaned_data['password']

        if not authenticate(registration_number=registration_number, password = password):
            raise forms.ValidationError("Invalid registration number or password.")


class TutorLoginForm(forms.ModelForm):
    password = forms.CharField(label ='Password', widget=forms.PasswordInput)
        
    class Meta:
        model = User
        fields = ('email', 'password')

    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']

        if not authenticate(registration_number=email, password = password):
            raise forms.ValidationError("Invalid email or password.")

