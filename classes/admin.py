from django.contrib import admin

from .models import Classes


class ClassesAdmin(admin.ModelAdmin):
    list_display = ['number', 'title', 'curator']



admin.site.register(Classes, ClassesAdmin)