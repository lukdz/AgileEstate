from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EstateForm
from .models import EstateModel

def estate_new(request):
    if request.method == 'POST':
        form = EstateForm(request.user, request.POST)

        if form.is_valid():
            estate = form.save(commit=False)
            data = form.cleaned_data
            estate.longitude = estate.count_longitude(data["lng_degrees"], data["lng_minutes"],
                                                      data["lng_seconds"])
            estate.latitude = estate.count_latitude(data["lat_degrees"], data["lat_minutes"],
                                                    data["lat_seconds"])

            if not form.user.is_anonymous:
                estate.owner_key

            return HttpResponseRedirect('created/')
    else:
        form = EstateForm(request.user)

    return render(request, 'estateNew.html', {'form': form})

def estate_created(request):
    return render_to_response('estateCreated.html')

def estate_details(request, estateid):
    if request.method == 'GET':
        return render_to_response('estateDetails.html')

def estate_all(request):
    estates = EstateModel.objects.order_by('rooms')
    if request.method == 'GET':
        return render_to_response('estateAll.html', {'estates': estates})
