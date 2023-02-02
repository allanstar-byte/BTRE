from django.contrib import admin

# Importing listings model from the admin

from .models import Listing

# Registering the model to appear in the admin

admin.site.register(Listing)
