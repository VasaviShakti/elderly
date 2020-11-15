from django.shortcuts import render
from Mts.models import Health

# Create your views here.
def homecus(request):
    return render(request,"homepage-customer.html")