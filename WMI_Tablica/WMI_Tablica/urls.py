from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
from website import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WMI_Tablica.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^edit_personal_data$', views.edit_personal_data, name='edit_personal_data'),
    url(r'^watching_ads$', views.watching_ads, name='watching_ads'),
    url(r'^published_ads$', views.published_ads, name='published_ads'),
    url(r'^new_ad$', views.new_ad, name='new_ad'),
)
