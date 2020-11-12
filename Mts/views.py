from django.shortcuts import render
from Mts.models import Health

# Create your views here.
def home(request):
    return render(request,'home.html',{})