from django.contrib import admin

# Register your models here.
from .models import User, Student, Tutor

#Admin site customizations
admin.site.site_header = 'Accounts'
admin.site.index_title = 'Accounts Admiistration'
admin.site.site_title = 'schooladministration'

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Tutor)