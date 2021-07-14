from django import forms

from .models import School, Level, Certification, Course, Unit, Department, Document

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = ('Name', 'About', 'School_acronym', 'Certifications',
                  'Departments', 'Courses', 'Units')
