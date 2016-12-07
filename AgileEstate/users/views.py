from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from .forms import UserForm
# Create your views here.

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'profile/base.html')
    return render(request, 'profile/index.html')


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'profile/profile.html')
    context = {
        "form": form,
    }
    return render(request, 'profile/register.html', context)

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'profile/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, passwsord=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'profile/profile.html')
            else:
                return render(request, 'profile/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'profile/login.html', {'error_message': 'Invalid login'})
    return render(request, 'profile/login.html')

from django.shortcuts import render
