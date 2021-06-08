from django.db import models
from accounts.models import User
from multiselectfield import MultiSelectField

import datetime
import random

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length= 50, blank = True, null = True)
    About = models.TextField()
    School_acronym = models.CharField(max_length = 5, unique = True, blank = True, null = True)
     
    def __str__(self):
        return self.Name

class Level(models.Model):
    Study_Level = models.CharField(max_length = 300, unique = True, blank = True, null = True) 


class Certification(models.Model):
    Certification = models.CharField(max_length = 300, unique = True, blank = True, null = True)
    School = models.ForeignKey(School, verbose_name = "College", on_delete=models.CASCADE)
    Study_level = models.ForeignKey(Level, verbose_name = "Study Level", on_delete=models.CASCADE)

    def __str__(self):
        return self.Certification + self .School

    
class Course(models.Model):
    Certification = models.ForeignKey(Certification, verbose_name = "Certification", on_delete=models.CASCADE)
    Course_Title = models.CharField(max_length = 30, unique = True,  blank = True, null = True)
    School = models.ForeignKey(School, verbose_name = "School", on_delete=models.CASCADE)
    Course_code = models.CharField(max_length = 30, unique = True,  blank = True, null = True)

    def __str__(self): 
        return self.Course_Title + self.School + self.Certification

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
    Course = models.ForeignKey(Course, verbose_name = "Course", on_delete=models.CASCADE)
    Unit_Title = models.CharField(max_length = 30, unique = True,  blank = True, null = True) 
    Unit_Code = models.CharField(max_length = 30, unique = True,  blank = True, null = True)
    About = models.TextField()
    Classes = models.IntegerField(blank = True, null = True)
    Day_Time = models.DateTimeField(verbose_name = "Date/Time", name=None, auto_now = False, auto_now_add=False)


class Department(models.Model):
    Department = models.CharField(max_length = 300, unique = True, blank = True, null = True)
    About = models.TextField()
    Dept_code = models.CharField(max_length = 300, unique = True, blank = True, null = True)
    School = models.ForeignKey(School, verbose_name = "School", on_delete=models.CASCADE)
    Courses = models.ForeignKey(Course, verbose_name = "Courses", on_delete=models.CASCADE)
    Units = models.ForeignKey(Unit, verbose_name = "Units", on_delete=models.CASCADE)

class Document(models.Model):
    Document_CHOICES = (
        ('Student Complete Assignment', 'Student Complete Assignment'),
        ('Tutor Issued Assignment', 'Tutor Issued Assignment'),
        ('Student Learning Resourse', 'Student Learning Resourse' )
    )

    Document_type = MultiSelectField(choices = Document_CHOICES)
    name = models.CharField(max_length = 100, unique = True,  blank = True, null = True)
    description = models.CharField(max_length=255, blank=True)
    file = models.FileField(upload_to='document/%Y/%m/%d/', null=True, verbose_name="")
    unit = models.ForeignKey(Unit,verbose_name = "Course",  on_delete=models.CASCADE)
    uploaded_by = models.ForeignKey(User,verbose_name = "User", on_delete=models.CASCADE)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Assignment(models.Model):
    Assignment_Document =  models.ForeignKey(Document, max_length = 100)
    file = models.FileField(upload_to='assignment/%Y/%m/%d/', null=True, verbose_name="")


