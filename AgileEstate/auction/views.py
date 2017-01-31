from django.shortcuts import render, render_to_response, redirect
from django.contrib.auth.decorators import login_required

from .forms import BiddingForm
from .models import BiddingModel
from estate.models import EstateModel

#@login_required(login_url='users:login_user')
def bidding_new(request):
    if request.method == 'POST':
        form = BiddingForm(request.user, request.POST)

        if form.is_valid():
            bidding = form.save(commit=False)
            data = form.cleaned_data
            bidding.actual_price = data["start_price"]
            bidding.estate_key = EstateModel.objects.get( id=int(data["estate"]) )

            if not form.user.is_anonymous:
                bidding.owner_key = form.user
                bidding.winner_key = bidding.owner_key

            form.save(commit=True)

            return redirect('auction:bidding_added')
    else:
        form = BiddingForm(request.user)

    return render(request, 'biddingNew.html', {'form': form})

def bidding_added(request):
    if request.method == 'GET':
        return render_to_response('biddingAdded.html')

def bidding_all(request):
    biddings = BiddingModel.objects.order_by('end_time')
    if request.method == 'GET':
        return render_to_response('biddingAll.html', {'biddings': biddings})
