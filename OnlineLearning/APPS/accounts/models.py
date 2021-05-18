from django.contrib.auth.base_user import BaseUserManager
from ..academy.models import  School, Level, Certification, Course
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

    
class NewUser(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=200, blank=True)
    last_name = models.CharField(max_length=200, blank=True)
    email = models.EmailField(_('email address'), unique = True)
    School = models.ForeignKey(School)
    Level = models.ForeignKey(Level)
    Certification = models.ForeignKey(Certification)
    Course = models.ForeignKey(Course)
    Date_joined = models.DateTimeField(default = timezone.now)
    is_student = models.BooleanField(deafult=False)
    is_teacher = models.BooleanField(deafult=False)
    is_staff = models.BooleanField(default = False)
    is_active  = models.BooleanField(deafult = False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = 'first-name, last_name'

    objects = CustomAccountsManager()


    def __str__(self):
        return self.first_name + " " + self.last_name


    




