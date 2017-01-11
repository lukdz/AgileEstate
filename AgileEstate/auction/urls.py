from django.conf.urls import url
from . import views

app_name = "auction"

urlpatterns = [
    url(r'^add_to_bid/$', views.bidding_form, name='add_to_bid_form'),
]