from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required

from .forms import EstateForm
from .models import EstateModel

#@login_required(login_url='users:login_user')
def estate_new(request):
    if request.method == 'POST':
        form = EstateForm(request.user, request.POST)

        if form.is_valid():
            estate = form.save(commit=False)
            data = form.cleaned_data
            estate.set_longitude(data["lng_degrees"], data["lng_minutes"], data["lng_seconds"])
            estate.set_latitude(data["lat_degrees"], data["lat_minutes"], data["lat_seconds"])

            if not form.user.is_anonymous:
                estate.owner_key = form.user

            form.save(commit=True)

            return redirect('estate:estate_created')
    else:
        form = EstateForm(request.user)

    return render(request, 'estateNew.html', {'form': form})

def estate_created(request):
    if request.method == 'GET':
        return render_to_response('estateCreated.html')

def estate_all(request):
    estates = EstateModel.objects.order_by('rooms')
    if request.method == 'GET':
        return render_to_response('estateAll.html', {'estates': estates})

def estate_selected(request, selected_id):
    estates = EstateModel.objects.order_by('rooms')
    data = int('0' + selected_id)
    if request.method == 'GET':
        return render_to_response('estateSelected.html', {'estates': estates, 'data': data})
