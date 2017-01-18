from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EstateForm
from .models import EstateModel

def estate_new(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)

        if form.is_valid():
            estate = form.save(commit=False)
            data = form.cleaned_data
            estate.longitude = data["lng_degrees"]*3600+data["lng_minutes"]*60+data["lng_seconds"]
            estate.latitude = data["lat_degrees"]*3600+data["lat_minutes"]*60+data["lat_seconds"]
            return HttpResponseRedirect('/estate_created/')
    else:
        form = EstateForm()

    return render(request, 'estateNew.html', {'form': form})

def estate_details(request, estateid):
    if request.method == 'GET':
        return render_to_response('estateDetails.html')

def estate_all(request):
    estates = EstateModel.objects.order_by('rooms')
    if request.method == 'GET':
        return render_to_response('estateAll.html', {'estates': estates})
