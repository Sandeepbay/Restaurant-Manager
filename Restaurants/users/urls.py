from django.urls import path

from . import views

urlpatterns = [
    path("" , views.index , name="index"),
    path("login" , views.login_form , name="login"),
    path("logout" , views.logout_form , name="logout")
]