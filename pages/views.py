from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from learn.models import *
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages



def index(request):
    return render(request=request,
                  template_name='pages/index.html')

@login_required
def home(request):
    object_list = Question.objects.all()
    images =["11995","34611","228","39049"]
    object_list= [ (obj,images[i]) for i, obj in enumerate(object_list)]
    print (object_list)
    return render(request=request,
                  template_name='pages/home.html',
                  context={
                      "object_list":object_list,
                        })

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("login")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="registration/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="registration/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login")

