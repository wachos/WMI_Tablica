# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from website.models import *
# Create your views here.


def login_page(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        
        if user:
            login(request, user)
            return redirect('/')
        else:
            form = UserForm()
            return render(request, 'login.html', {'form' : form})
    else:
        form = UserForm()
        return render(request, 'login.html', {'form' : form})

@login_required
def logout_page(request):
    logout(request)
    return redirect('')
    
@login_required
def index(request):
    all_entries = Ogloszenie.objects.all().order_by('-id')
    return render_to_response('index.html',{'pubb':all_entries})

def edit_personal_data(request):
    return render_to_response('edit_personal_data.html')
    
def watching_ads(request):
    return render_to_response('watching_ads.html')

def published_ads(request):
    return render_to_response('watching_ads.html')

def new_ad(request):
	if request.POST:
	    ogloszenie_form = OgloszenieForm(request.POST)
	    if ogloszenie_form.is_valid():
	        ogloszenie_form.save()
	        return render(request, 'new_ad.html', {'form' : ogloszenie_form, 'message_true': 'Ogłoszenie dodano'})
	    else:
			ogloszenie_form = OgloszenieForm()
            return render('new_ad.html', {'form' : ogloszenie_form, 'message_error': 'Wypełnij poprawnie wszystkie pola'})
	else:
		ogloszenie_form = OgloszenieForm()
		return render(request, 'new_ad.html', {'form' : ogloszenie_form})
