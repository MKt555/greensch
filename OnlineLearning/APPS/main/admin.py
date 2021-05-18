from django.contrib import admin
from .models import News

#Admin site customizations
admin.site.site_header = 'School Administration'
admin.site.index_title = 'Main Admiistration'
admin.site.site_title = 'schooladministration'

admin.site.register(News)

