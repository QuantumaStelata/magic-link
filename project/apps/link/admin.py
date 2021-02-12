from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'number_visits', 'active')