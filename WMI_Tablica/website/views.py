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
    

def index(request):
    all_entries = Ogloszenie.objects.all().order_by('-id')
    return render_to_response('index.html',{'pubb':all_entries})

def edit_personal_data(request):
    return render_to_response('edit_personal_data.html')


def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        ogloszenia=Ogloszenie.objects.filter(tresc__icontains=q)
        return render(request, 'search_result.html',
            {'ogloszenia': ogloszenia, 'query': q})
    else:
        return render(request, 'search_error.html')

def search_by_title(request):
        q = request.GET['q']
        ogloszenia=Ogloszenie.objects.filter(tytul__icontains=q)
        return render(request, 'search_result_by_title.html',
            {'ogloszenia': ogloszenia, 'query': q})
    
def watching_ads(request):
    return render_to_response('watching_ads.html')

def published_ads(request):
    return render_to_response('watching_ads.html')
    
def edit_password(request):
    return render_to_response('edit_password.html')

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

def edit_password(request):
    if request.POST:
        edit = EditPasswordForm(request.POST)
    else:
        edit = EditPasswordForm()
        return render(request, 'edit_password.html', {'form' : edit})
