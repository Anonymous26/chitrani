from django.contrib import admin
from webapp.models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender')
    search_fields = ['name']

admin.site.register(Profile, ProfileAdmin)