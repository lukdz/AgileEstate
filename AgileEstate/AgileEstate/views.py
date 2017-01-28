from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect

def main_page(request):
    if request.method == 'GET':
        return render_to_response('main.html')

