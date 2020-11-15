from django.shortcuts import render
from Mts.models import Health

# Create your views here.


def homecus(request):
    if request.method == "POST":
        content = { 'homepage': request.POST:['homepage'] }
        return render(request, "homepage-customer.html", content)

def profile(request):
    if request.method == "POST":
        content = { 'profile': request.POST:['profile'] }
        return render(request, "profile.html", content)

def editpro(request, name_id):
   
    if request.method == "POST":
        if request.method['edited'] == '':
            content = { 'information': Health.objects.all(), 'Warning': 'Please input content!'}
            return render(request, "system_full/edit.html", content)
        else:
            int(name_id)['waiting'] = request.POST['already']
            return redirect("profile")
    elif request.method == "GET":
        content = { 'waiting': int(name_id)]['profile'] }
        return render(request, "system_full/edit.html", content)

def cross(request, name_id):
    if request.POST['status'] == 'finished':
        a = Health.objects.get(id=name_id)
        a.done = True
        return redirect("profile")
    else:
        a = Health.objects.get(id=name_id)
        a.done = False
        return redirect("edit")
