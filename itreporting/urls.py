from django.urls import path
from . import views

# Code to map the function home

app_name = 'itreporting'

urlpatterns = [
    path ('',views.home,name='home'),
    path ('about',views.about,name='about'),
    path ('contact',views.contact,name='contact'),
]