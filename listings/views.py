from django.shortcuts import render


# def index(request):
#     return render(request, 'listings/listings.html')

def listing(request, listing_id):
    return render(request, 'listings/listing.html')

def search(request):
    return render(request, 'listings/search.html')


#---------------------------------------------------------------

# Reading the data from the database

# import listings model

from .models import Listing

def index(request):
    listings = Listing.objects.all()

    # incase of an error install (pip install pylint-django)

    # and add this to the settings using ctrl + , ({"python.linting.pylintArgs": [
    #  "--load-plugins=pylint_django"
# ],})

# https://stackoverflow.com/questions/45135263/class-has-no-objects-member

    context = {
        'listings': listings
    }

    return render(request, 'listings/listings.html', context)

