from django.conf.urls import patterns, include, url
from shellsite import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^home/', views.home, name='home'),
    
                       )
