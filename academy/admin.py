from django.contrib import admin
from .models import School, Level, Certification, Course, Unit, Department, Document

#Admin site customizations
admin.site.site_header = 'Academics'
admin.site.index_title = 'Academics Admin'
admin.site.site_title = 'Schools'

admin.site.register(School)
admin.site.register(Level)
admin.site.register(Certification)
admin.site.register(Course)
admin.site.register(Unit)
admin.site.register(Department)
admin.site.register(Document)