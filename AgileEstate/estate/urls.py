from django.conf.urls import url
from . import views

app_name = "estate"

urlpatterns = [
    url(r'^new/$', views.estate_new, name='estate_new'),
    url(r'estate/(?P<estateid>[0-9]+)$', views.estate_details),
]