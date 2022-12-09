from django.contrib import admin
from django.utils.safestring import mark_safe


from .models import Lessons


class LessonsAdmin(admin.ModelAdmin):
    list_display = ['name_lessons', 'teacher']



admin.site.register(Lessons, LessonsAdmin)
