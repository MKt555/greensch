from django.db import models
from accounts.models import User

from multiselectfield.db.fields import MultiSelectField

from django.utils import timezone
import datetime
import random

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length= 50, default= '')
    About = models.TextField()
    School_acronym = models.CharField(max_length = 5, unique = True, default= '')
    School_slug = models.CharField(max_length=200, default=1)

    class Meta:
        verbose_name_plural = "School"

    def __str__(self):
        return self.School

class Level(models.Model):
    Study_Level = models.CharField(max_length = 300, unique = True, default= '') 

    class Meta:
        verbose_name_plural = "Study Levels"

    def __str__(self):
        return self.Level


class Certification(models.Model):
    Certification = models.CharField(max_length = 300, unique = True, default= '')
    School = models.ForeignKey(School, verbose_name = "College", on_delete=models.CASCADE, default= '')
    Study_level = models.ForeignKey(Level, verbose_name = "Study Level", on_delete=models.CASCADE, default= '')

    class Meta:
        verbose_name_plural = "Certifications"

    def __str__(self):
        return self.Certification 


class Course(models.Model):
    Certification = models.ForeignKey(Certification, verbose_name = "Certification", on_delete=models.CASCADE, default= '')
    Course_Title = models.CharField(max_length = 30, unique = True,  default= '')
    Course_code = models.CharField(max_length = 30, unique = True,  default= '')

    class Meta:
        verbose_name_plural = "Courses"

    def __str__(self): 
        return self.Course_Title

    def generate_registration_number(self,code,digit,time):
        time_now = datetime.datetime.now()
        code = self.Course_code
        time = str(time_now.year)
        numbers = {}
        digit = str(random.randrange(0000, 51000, 1))
        numbers.add(digit)
        registration_number = code + "/"+digit+"/"+time

        return registration_number
        

class Unit(models.Model):
    Course = models.ForeignKey(Course, verbose_name = "Course", on_delete=models.CASCADE, default= '')
    Unit_Title = models.CharField(max_length = 30, unique = True, default= '') 
    Unit_Code = models.CharField(max_length = 30, unique = True, default= '')
    About = models.TextField()
    Classes = models.IntegerField(default= '')
    Day_Time = models.DateTimeField(verbose_name = "Date/Time", name=None, auto_now = False, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Units"

    def __str__(self):
        return self.Unit

class Department(models.Model):
    Department = models.CharField(max_length = 300, unique = True, default= '')
    About = models.TextField(blank = True, null = True)
    Dept_code = models.CharField(max_length = 300, unique = True, default= '')
    Units = models.ForeignKey(Unit, verbose_name = "Units", on_delete=models.CASCADE, default= '')

    class Meta:
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.Department 


class Document(models.Model):
    Document_CHOICES = (
        ('Student Complete Assignment', 'Student Complete Assignment'),
        ('Tutor Issued Assignment', 'Tutor Issued Assignment'),
        ('Student Learning Resourse', 'Student Learning Resourse' )
    )

    Document_type = MultiSelectField(choices = Document_CHOICES)
    name = models.CharField(max_length = 100, unique = True, default= '')
    description = models.CharField(max_length=255, default= '')
    file = models.FileField(upload_to='document/%Y/%m/%d/', default= '', verbose_name="")
    unit = models.ForeignKey(Unit,verbose_name = "Course",  on_delete=models.CASCADE, default= '')
    uploaded_by = models.ForeignKey(User,verbose_name = "User", on_delete=models.CASCADE, default= '')
    uploaded_at = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name_plural = "Documents"

    def __str__(self):
        return self.Document

class Assignment(models.Model):
    Assignment_Document =  models.ForeignKey(Document, max_length = 100, on_delete=models.CASCADE)
    file = models.FileField(upload_to='assignment/%Y/%m/%d/', null=True, verbose_name="")

    class Meta:
        verbose_name_plural = "Assignments"

    def __str__(self):
        return self.Assignment

