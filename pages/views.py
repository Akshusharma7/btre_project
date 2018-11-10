from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices,state_choices,bedroom_choices

# Create your views here.
def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]
    context = {
        'listings':listings,
        'price_choices': price_choices,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
    }
    return render(request,'pages/index.html',context)

def about(request):
    #Get all realtor from realtors database
    realtors = Realtor.objects.order_by('-hire_date')

    #Get mvp 
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtor': mvp_realtor
    }
    return render(request,'pages/about.html',context)