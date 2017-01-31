from django.shortcuts import render, render_to_response, redirect

from .forms import BiddingForm

def bidding_new(request):
    if request.method == 'POST':
        form = BiddingForm(request.user, request.POST)

        if form.is_valid():
            bidding = form.save(commit=False)
            data = form.cleaned_data
            bidding.actual_price = data["start_price"]

            if not form.user.is_anonymous:
                bidding.owner_key = form.user
                bidding.winner_key = bidding.owner_key

            return redirect('bidding:bidding_added')
    else:
        form = BiddingForm(request.user)

    return render(request, 'biddingNew.html', {'form': form})

def bidding_added(request):
    if request.method == 'GET':
        return render_to_response('biddingAdded.html')
