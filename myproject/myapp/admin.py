from django.contrib import admin
from .models import Target # Import your data models here

# Register your models here
admin.site.register(Target)  # Register your model(s) to make them available in the admin interface
