from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

from .forms import EstateForm

def estate_new(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/estate_created/')
    else:
        form = EstateForm()

    return render(request, '/templates/estateNew.html', {'form': form})

def estate_details(request, estateid):
    if request.method == 'GET':
        return render_to_response('/templates/estateDetails.html')
