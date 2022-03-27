""" Admin Page settings for alumni."""

from django.contrib import admin

from . import models


class AlumniAdmin(admin.ModelAdmin):
    ''' Admin class for Alumni model'''

    list_display = ['email', 'first_name', 'last_name', 'batch', 'department','phone1', 'gender', 'profile_pic']
    readonly_fields = ('added_by', 'add_date', 'last_modified', 'modified_by')
    fieldsets = (
        ('Academic', {
            'fields':(('batch', 'department'),)
        }),
        ('Personal Details', {
            'fields':(('first_name', 'last_name'), ('phone1', 'phone2'),('email', 'gender'), ('social_site_url', 'profile_pic'),'current_location')
        }),
        ('Admin Action', {
            'fields':(('status','added_by', 'add_date'),('last_modified', 'modified_by'))
        })
    )
    date_hierarchy = 'last_modified'
    list_filter = ('batch', 'department', 'gender', 'status')
    

    def save_model(self, request, obj, form, change):
        if getattr(obj, 'added_by', None) is None:
            obj.added_by = request.user
        obj.modified_by = request.user
        obj.save()

admin.site.register(models.Alumni, AlumniAdmin)