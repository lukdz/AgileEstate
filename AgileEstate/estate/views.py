from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import EstateForm

def estate_form(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/success/')
    else:
        form = EstateForm()

    return render(request, 'EstateForm.html', {'form': form})

def estate_form(request):
    if request.method == 'POST':
        form = EstateForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/display/')
    else:
        form = EstateForm()

    return render(request, '/templates/base.html', {'form': form})
