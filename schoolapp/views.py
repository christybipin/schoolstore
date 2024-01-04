from django.contrib import messages, auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from schoolapp.forms import RegisterForm, LoginForm


# Create your views here.
def store(request):
    context = { }
    return render(request, 'Main.html', context)


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            try:
                return redirect('click_view')
            except:
                pass
    else:
        form = LoginForm()
    return render(request, 'login.html', { 'form': form })


def click_view(request):
    return render(request, 'button.html')


def add_form(request):
    return render(request, 'form.html')


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            try:
                return redirect('login')
            except:
                pass
    else:
        form = RegisterForm()
    return render(request, 'register.html', { 'form': form })


def logout(request):
    auth.logout(request)
    return redirect('/')
