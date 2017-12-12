from django.contrib import admin

# Register your models here.
from .models import Owner,Pet

admin.site.register(Owner)
admin.site.register(Pet)
