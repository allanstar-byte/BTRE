from django.contrib import admin

# Importing listings model from the admin

from .models import Listing

# Adding more content data to the admin area 

class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    # This will make the title clickable
    list_display_links = ('title', )
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    # for pagination purposes
    list_per_page = 25

# Registering the model to appear in the admin

admin.site.register(Listing, ListingAdmin)


