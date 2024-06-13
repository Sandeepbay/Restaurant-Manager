from django.shortcuts import render
from .models import Restaurant

# Create your views here.

def index(request):
    return render(request , "restaurant/index.html" , {
        "restaurants" :  Restaurant.objects.all()
    })

def restaurant(request , restaurant_id):
    restaurant = Restaurant.objects.get(pk=restaurant_id)
    return render(request , 'restaurant/diner.html' , {
        "restaurant": restaurant,
        "peoples" : restaurant.people.all()
    })