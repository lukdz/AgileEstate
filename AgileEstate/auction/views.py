from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import BiddingForm

def bidding_new(request):
    if request.method == 'POST':
        form = BiddingForm(request.POST)

        if form.is_valid():
            bidding = form.save(commit=False)
            data = form.cleaned_data
            bidding.actual_price = data["start_price"]
            return HttpResponseRedirect('/bidding_starts/')
    else:
        form = BiddingForm()

    return render(request, 'biddingNew.html', {'form': form})
