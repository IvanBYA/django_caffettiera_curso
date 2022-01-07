from django.contrib import admin
from .models import Page


class PageAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "updated")
    list_display = ('title', 'order')

# Register your models here.

admin.site.register(Page, PageAdmin)