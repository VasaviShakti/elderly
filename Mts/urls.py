from django.urls import path
from . import views
urlpatterns = [
    path('homepage-customer/',views.homecus,name="homecus")
]