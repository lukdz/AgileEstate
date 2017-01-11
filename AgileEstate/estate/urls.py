from django.conf.urls import url
from . import views

app_name = "estate"

urlpatterns = [
    url(r'^add_estate/$', views.estate_form, name='estate_form'),
]