from django.shortcuts import render
from django.http import HttpResponse

from realtors.models import Realtor
from listings.models import Listing

def index(request):
    listings = Listing.objects.order_by('list_date')
    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    realtors = Realtor.objects.order_by('-hire_date')

    # Gte MVP

    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtor
    }
    return render(request, 'pages/about.html', context)

    
