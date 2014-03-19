# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from website.models import *
# Create your views here.

def index(request):
    ad = """
    <div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">Przykładowe ogłoszenie 1</h3>
  </div>
  <div class="panel-body">
    <div class="ad-text">
        <p>
            <a href="#" class="thumbnail">
                <img src="../static/images/1.jpg" alt="...">
            </a>
            Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
        </p>
    </div>
  </div>
  <div class="panel-footer">
    <div class="ad-date">Data dodania: <b>12-12-2012</b></div>
    <div class="btn-group pull-right">
      <button type="button" class="btn btn-default">Więcej</button>
      <button type="button" class="btn btn-default">Obserwuj</button>
    </div>
  </div>
</div>
    """
    ads_list = [ad, ad, ad]
    return render_to_response('index.html', {'ads_list' : ads_list})


def edit_personal_data(request):
    return render_to_response('edit_personal_data.html')
    
def watching_ads(request):
    return render_to_response('watching_ads.html')

def published_ads(request):
    return render_to_response('watching_ads.html')

def new_ad(request):
	if request.POST:
	    form = OgloszenieForm(request.POST)
	    if form.is_valid():
	        form.save()
	        return render(request, 'new_ad.html', {'form' : ogloszenie_form, 'message_true': 'Ogłoszenie dodano'})
	    else:
			ogloszenie_form = OgloszenieForm()
            return render_to_response('new_ad.html', {'form' : ogloszenie_form, 'message_error': 'Wypełnij poprawnie wszystkie pola'})
	else:
		ogloszenie_form = OgloszenieForm()
		return render(request, 'new_ad.html', {'form' : ogloszenie_form})
