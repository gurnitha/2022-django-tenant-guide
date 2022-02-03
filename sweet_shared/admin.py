# sweet_shared/admin.py

# Django modules
from django.contrib import admin

# Locals
from .models import SweetType

# Register your models here.


admin.site.register(SweetType)