from django.contrib import admin
from .models import menu_lang, menu_items

# Register your models here.
admin.site.register(menu_items)
admin.site.register(menu_lang)
