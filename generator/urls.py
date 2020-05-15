from django.urls import path
from . import views
app_name = 'generator'

urlpatterns = [

    path("",views.password_generator, name = "password_generator"),
    path("password/",views.password, name = "password"),
    path("about/",views.about, name = "about"),


]
