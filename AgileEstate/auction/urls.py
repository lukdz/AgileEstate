from django.conf.urls import url
from . import views

app_name = "auction"

urlpatterns = [
    url(r'^new/$', views.bidding_new, name='bidding_new'),
]