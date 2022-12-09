from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Director


class DirectorAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'get_image', 'phone']

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f"<img src={obj.image.url} width='100' height='110'>")
        return 'not image you have'


admin.site.register(Director, DirectorAdmin)



