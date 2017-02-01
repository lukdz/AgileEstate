from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.shortcuts import render
from estate.models import EstateModel
from .forms import UserForm, UserProfileForm
from .models import UserProfile



# Create your views here.

def index(request):
    return render(request, 'main.html')
    
def register(request):
    userForm = UserForm(request.POST or None)
    profileForm = UserProfileForm(request.POST or None)
    if userForm.is_valid():
        user = userForm.save(commit=False)
        username = userForm.cleaned_data['username']
        password = userForm.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if profileForm.is_valid():

            gender = profileForm.cleaned_data['gender']
            firstname = profileForm.cleaned_data['firstname']
            lastname = profileForm.cleaned_data['lastname']
            profile = UserProfile(user=user,gender=gender,firstname=firstname,lastname=lastname)
            profile.save()

        else:
            profile = None

        estates = EstateModel.objects.filter(owner_key=profile)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'profile/user_profile.html', {"user":user,"profile":profile,"estates":estates})
    context = {
        "userForm": userForm,
        "profileForm": profileForm
    }
    return render(request, 'profile/register.html', context)

def logout_user(request):
    logout(request)
    return render(request, 'main.html')

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        print('Tried to log on to:' + username + "; " + password)
        user = authenticate(username=username, password=password)
        profile = UserProfile.objects.get(user=user)
        estates = EstateModel.objects.filter(owner_key=profile)
        print(estates)
        print("okay")
        if user is not None:
            print("user found")
            if user.is_active:
                login(request, user)
                print("logged on")
                return render(request, 'profile/user_profile.html', {"user":user,"profile":profile,"estates":estates})
            else:
                return render(request, 'profile/login.html', {'error_message': 'Your account has been disabled'})
        else:
            print("user not found")
            return render(request, 'profile/login.html', {'error_message': 'Invalid login'})
    return render(request, 'profile/login.html')

def get_user_profile(request, username):
    user = User.objects.get(username=username)
    profile = UserProfile.objects.get(user=user)
    estates = EstateModel.objects.filter(owner_key=profile)
    print(estates)
    return render(request, 'profile/user_profile.html', {"user":user,"profile":profile,"estates":estates})

from django.shortcuts import render
