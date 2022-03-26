""" Admin Page settings for alumni."""

from django.contrib import admin

from . import models

class DepartmentAdmin(admin.ModelAdmin):

    ''' Admin class for Department model.'''

    list_display = ['name']
    search_fields = ['name']

class AlumniAdmin(admin.ModelAdmin):
    ''' Admin class for Alumni model'''

    list_display = ['batch', 'department', 'first_name', 'last_name', 'gender', 'email']

admin.site.register(models.Department, DepartmentAdmin)
admin.site.register(models.Alumni, AlumniAdmin)