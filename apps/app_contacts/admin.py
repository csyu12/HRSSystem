from django.contrib import admin
from django.utils.html import format_html
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    pass
