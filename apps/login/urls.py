from django.conf.urls import url
from . import views          
urlpatterns = [
    url(r'^$', views.index),
    url(r'^main/$', views.index),    
    url(r'^users/$', views.index), 
    url(r'^create$', views.create),
    #url(r'^results$', views.results),
    url(r'^register/$', views.register),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    ]
