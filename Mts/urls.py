from django.urls import path
from . import views

urlpatterns = [
    path( 'homepage-customer/', views.homecus, name="homecus")
    path( 'profile/', views.Profile, name="profile")
    path( 'editpro/<name_id>', views.editpro, name="edpro")
    path( 'cross/<name_id>', views.cross, name="cross")
    path( 'license/<name_id>', views.license, name="license")
]