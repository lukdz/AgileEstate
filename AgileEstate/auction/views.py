from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import BiddingForm

def bidding_new(request):
    if request.method == 'POST':
        form = BiddingForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/bidding_starts/')
    else:
        form = BiddingForm()

    return render(request, 'templates/biddingNew.html', {'form': form})
