from django.shortcuts import render, redirect, render_to_response
from .forms import BaseUserCreationForm, BaseUserUpdateForm, FarmerUpdateForm, FarmerCreationForm
from django.contrib import messages
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout, user_logged_in
from django.contrib.auth.decorators import login_required
from django.http import *
from users.models import *
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView

def test(request):
    return render(request, 'auth/test.html', {})

def home(request):
    return render(request, 'index2.html', {})

def register(request):
    form = BaseUserCreationForm()
    if request.method == 'POST':
        form = BaseUserCreationForm(request.POST)
        if form.is_valid():
            baseuser = form.save()
            if form.cleaned_data.get('user_type') == 'FMR':
                farmer = FarmerCreationForm().save(commit=False)
                farmer.baseuser = baseuser
                farmer.save()
            return redirect('login')
        else:
            messages.error(request, f'Error Faced {form.errors}')
    else:
        form = BaseUserCreationForm()
    return render(request, 'auth/register.html', {'form': form})



@login_required
def edit_profile(request):
    if request.method == 'POST':
        base_form = BaseUserUpdateForm(request.POST, instance=request.user)
        user_form = FarmerUpdateForm(request.POST, instance=request.user.farmer)
        if user_form.is_valid() and base_form.is_valid():
            user_form.save()
            base_form.save()
            messages.success(request, f'Your Profile Has Been Updated')
            return redirect('profile')
    else:
        base_form = BaseUserUpdateForm(instance=request.user)
        user_form = FarmerUpdateForm(instance=request.user.farmer)
    context = {
        'form': base_form,
        'form_farmer': user_form
    }
    return render(request, 'profile/farmer_edit.html', context)

@login_required
def profile(request):
    if request.user.user_type == "FMR":
        return render(request, 'profile/farmer.html', {})
    elif request.user.user_type == "RTL":
        return render(request, 'profile/retailer_edit.html', {})
    elif request.user.user_type == "SPL":
        return render(request, 'profile/supplier_edit.html', {})
    else:
        messages.error(request, request.user.is_farmer)
        return render(request, 'auth/test.html', {})

def login_user(request):
    return render(request, 'auth/login_user.html', context)