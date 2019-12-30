from django.contrib import admin
from .models import filmstudio_lang, filmstudio_img, filmstudio_inventory, filmstudio_vid

# Register your models here.
admin.site.register(filmstudio_lang)
admin.site.register(filmstudio_img)
admin.site.register(filmstudio_inventory)
admin.site.register(filmstudio_vid)
