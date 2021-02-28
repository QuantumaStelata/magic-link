from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('email', 'token', 'number_visits', 'active')

import requests
import threading
import time

def main():
    while True:
        requests.get('https://quantumas.herokuapp.com')
        time.sleep(600)

threading.Thread(target=main, args=(), daemon=True).start()