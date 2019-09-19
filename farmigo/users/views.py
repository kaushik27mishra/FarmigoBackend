from django.shortcuts import render, redirect, render_to_response
from .forms import BaseUserCreationForm
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.http import *
from users.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def test(request):
    return render(request, 'auth/test.html', {})

def register_user(request):
    if request.method == 'POST':
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! Please Log in')
            return redirect('login')
    else:
        form = BaseUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def login_user(request):
    return render(request, 'auth/login_user.html', {})