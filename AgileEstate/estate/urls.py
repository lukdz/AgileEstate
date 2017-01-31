from django.conf.urls import url
from . import views

app_name = "estate"

urlpatterns = [
    url(r'^$', views.estate_all, name='estate_all'),
    url(r'^new/$', views.estate_new, name='estate_new'),
    url(r'^created/$', views.estate_created, name='estate_created'),
    url(r'^selected/(\d+)/$', views.estate_selected, name='estate_selected'),
]
