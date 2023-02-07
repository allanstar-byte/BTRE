from django.contrib import admin

# Importing Realtor model from the admin

from .models import Realtor

# Adding more content data to the admin area 

class RealtorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'hire_date')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 25

# Registering the model to appear in the admin

admin.site.register(Realtor, RealtorAdmin)
