from django.http import HttpResponse
from django.shortcuts import get_list_or_404, get_object_or_404
import datetime
from .models import PropertyModel

def current_datetime(request):
    now = datetime.datetime.now()
    # country = get_list_or_404(PropertyModel, pk=country_id)
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
