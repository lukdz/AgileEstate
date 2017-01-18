from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EstateForm
from .models import EstateModel
from .models import Places

def estate_new(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)

        if form.is_valid():
            estate = form.save(commit=False)
            data = form.cleaned_data
            estate.longitude = estate.count_longitude(data["lng_degrees"], data["lng_minutes"],
                                                      data["lng_seconds"])
            estate.latitude = estate.count_latitude(data["lat_degrees"], data["lat_minutes"],
                                                    data["lat_seconds"])
            return HttpResponseRedirect('/estate_created/')
    else:
        form = EstateForm()

    return render(request, 'estateNew.html', {'form': form})

def estate_details(request, estateid):
    if request.method == 'GET':
        return render_to_response('estateDetails.html')

def estate_all(request):
    estates = EstateModel.objects.order_by('rooms')
    places = Places
    if request.method == 'GET':
        return render_to_response('estateAll.html', {'estates': estates, 'places': places})
