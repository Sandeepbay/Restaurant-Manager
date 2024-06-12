from django.shortcuts import render

from .models import Restaurant

# Create your views here.

restaurant = Restaurant.objects.all()

def index(request):
    return render(request , "restaurant/index.html" , {
        "restaurants" : restaurant
    })