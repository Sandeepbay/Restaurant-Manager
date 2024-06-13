from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("<int:restaurant_id>" , views.restaurant , name="restaurant")
]