from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("<int:restaurant_id>" , views.restaurant , name="restaurant"),
    path("<int:restaurant_id>/book" , views.book , name="book")
]