from django.conf.urls import url
from . import views          
urlpatterns = [
    #url(r'^$', views.index),   
    url(r'^quotes/$', views.index), 
    url(r'^makequote$', views.makequote),
   # url(r'^users/(?P<user_no>\d+)/$', views.dashboard),
    url(r'^addfav$', views.addfav),
    url(r'^remfav$', views.remfav),
    url(r'^users/(?P<user_no>\d+)/$', views.dashboard)
    #url(r'^register/$', views.register),
    #url(r'^login$', views.login),
    #url(r'^logout$', views.logout),
    ]
