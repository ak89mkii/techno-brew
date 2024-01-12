from django.contrib import admin

from .models import Item, Theme

# Register your models here.
admin.site.register(Item)
admin.site.register(Theme)