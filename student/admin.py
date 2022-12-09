from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Student

class StudentAdminUser(admin.ModelAdmin):
    list_display = ['fio','klass', 'get_image']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width='150' height='100' >")
        return "no image"

admin.site.register(Student,StudentAdminUser)