from django.db import models

# Create your models here.
class School(models.Model):
    Name = models.CharField(max_length= 50, blank = True, null = True)
    About = models.TextField()
    School_acronym = models.CharField(max_length = 5, unique = True, blank = True, null = True)
     
    def __str__(self):
        return self.Name

class Level(models.Model):
    Level = models.CharField(max_length = 300, unique = True, blank = True, null = True) 


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
    
class Unit(models.Model):
    Course = models.ForeignKey(Course, verbose_name = "Course", on_delete=models.CASCADE)
    Unit_Title = models.CharField(max_length = 30, unique = True,  blank = True, null = True) 
    Unit_Code = models.CharField(max_length = 30, unique = True,  blank = True, null = True)
    About = models.TextField()
    Classes = models.IntegerField(blank = True, null = True)
    Day_Time = models.DateTimeField(verbose_name = "Date/Time", name=None, auto_now = False, auto_now_add=False)

class Department(models.Model):
    Department = models.CharField(max_length = 300, unique = True, blank = True, null = True)
    Dept_code = models.CharField(max_length = 300, unique = True, blank = True, null = True)
    School = models.ForeignKey(School, verbose_name = "School", unique = True, on_delete=models.CASCADE)
    Courses = models.ForeignKey(Course, verbose_name = "Courses", unique = True, on_delete=models.CASCADE)
    Units = models.ForeignKey(Unit, verbose_name = "Units", unique = True, on_delete=models.CASCADE)
