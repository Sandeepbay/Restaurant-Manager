from django.shortcuts import render
from .models import Restaurant , People
from django.http import HttpResponseRedirect
from django.urls import reverse
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

def book(request , restaurant_id):
    if request.method == "POST":
        restaurant = Restaurant.objects.get(pk=restaurant_id)
        name = request.POST["name"]
        order = request.POST["order"]
        review = request.POST["review"]
        people = People.objects.create(name=name , order=order , review=review)
        people.conneection.add(restaurant)
        return HttpResponseRedirect(reverse("restaurant" , args=(restaurant_id,)))