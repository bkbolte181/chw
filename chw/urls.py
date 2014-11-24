from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView

from chw import views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Redirect to the calendar view
    url(r'^$', RedirectView.as_view(url='calendar/', permanent=False), name='index'),
    
    url(r'^login/$', views.auth_login, name='login'),
    url(r'^signup/$', views.auth_signup, name='signup'),
    
    # urls.py in cal app
    url(r'^calendar/', include('cal.urls', namespace='cal')),
                       
    # Admin view
    url(r'^admin/', include(admin.site.urls)),
)
