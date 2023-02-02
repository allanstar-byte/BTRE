from django.contrib import admin

# Importing Realtor model from the admin

from .models import Realtor

# Registering the model to appear in the admin

admin.site.register(Realtor)
