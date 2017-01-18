from django.http import HttpResponse

def main_page(request):
    html = "<html><body>Welcome to AgileEstate: the world's largest estate auctions agency!</body></html>"
    return HttpResponse(html)
