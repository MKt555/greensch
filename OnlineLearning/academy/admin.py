from django.contrib import admin
from .models import School, Level, Certification, Course, Unit, Department, Document

#Admin site customizations
admin.site.site_header = 'Academics'
admin.site.index_title = 'Academics Admin'
admin.site.site_title = 'Schools'


class SchoolAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Name", {'fields': ["tutorial_title", "tutorial_published"]}),
        ("URL", {'fields': ["school_slug"]}),
        ("Certifications", {'fields': ["Certifications"]}),
        ("Departments", {'fields': ["Departments"]}),
        ("Courses", {'fields': ["Courses"]}),
        ("Units", {'fields': ["Units"]}),
    ]



admin.site.register(Level)
admin.site.register(Certification)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Department)
admin.site.register(Document)
admin.site.register(School, SchoolAdmin)