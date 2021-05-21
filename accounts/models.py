from django.contrib.auth.base_user import BaseUserManager
from academy.models import  School, Level, Certification, Course, Unit, Department
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, User

# Create your models here.


class CustomAccountsManager(BaseUserManager):

    def create_superuser(self, email, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            return ValueError ('Superuser must be assigned to is_staff = True.')
        
        if other_fields.get('is_superuser') is not True:
            return ValueError ('Superuser must be assigned to is_superuser = True.')

        return self.create_user(email, first_name, last_name, password, **other_fields)


    def create_user(self, email, first_name, last_name, password, **other_fields):
        if not email:
            raise ValueError(_("You must provide an email address."))
        if not first_name:
            raise ValueError(_("You must provide a first name."))
        if not last_name:
            raise ValueError(_("You must provide a last name."))
        if not password:
            raise ValueError(_("You must provide a password."))
        email = self.normalize_email(email)
        user = self.model(first_name = first_name, last_name = last_name, email = email, **other_fields)
        user.set_password(password)
        user.save()
        return User

    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(_('email address'), unique = True)   
    Date_joined = models.DateTimeField(default = timezone.now)
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_staff = models.BooleanField(default = False)
    is_active  = models.BooleanField(default = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first-name, last_name']

    objects = CustomAccountsManager()


    def __str__(self):
        return self.first_name + " " + self.last_name

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    School = models.ForeignKey(School, on_delete = models.CASCADE)
    Level = models.ForeignKey(Level, on_delete = models.CASCADE)
    Certification = models.ForeignKey(Certification, on_delete = models.CASCADE)
    Course = models.ForeignKey(Course, on_delete = models.CASCADE)
    registration_number = models.CharField(max_length=50, primary_key = True,  unique = True, null=False, blank=False)

class Tutor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    Title = models.CharField(max_length=20)
    Department = models.ForeignKey(Department, on_delete = models.CASCADE)
    Units = models.ForeignKey(Unit, on_delete = models.CASCADE)
    About = models.TextField()
    payroll_no = models.CharField(max_length=50, unique = True, null=False, blank=False)
    email = models.EmailField(verbose_name="Email Address", max_length = 100, unique=True)

    




