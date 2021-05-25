from django import forms

from .models import School, Level, Certification, Course, Unit, Department, Document

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('Name', 'About',)

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = ('Study_Level',)

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ('Certification', 'School',)

class CourseForm(forms.ModelForm):
    model = Course
    fields = ('Certification', 'Course_Title', 'School', 'Course_code',)

class UnitForm(forms.ModelForm):
    model = Unit
    fields = ('Course', 'Unit_Title', 'Unit_Code', 'About',)

class DepartmentForm(forms.ModelForm):
    model = Department
    fields = ('Department', 'About','Dept_code','School', 'Courses', 'Units',)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('name', 'description', 'unit',)