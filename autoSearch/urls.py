"""autoSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from carros import views, models, urls
from carros.views import car_list, car_detail, CarCreateView, CarUpdateView, CArDeleteView, CarListView


urlpatterns = [

    url(r'^carros/', include('carros.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^',include('carros.urls', namespace = "templates")),

    url(r'^create$', CarCreateView.as_view(), name='CarCreateView'),

    #url(r'^cars/list/$', CarListView.as_view(), name='car_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$', car_detail.as_view(),name='CarDetail'),

    url(r'^update/(?P<pk>[0-9]+)/edit/$', CarUpdateView.as_view(), name='CarUpdate'),

    url(r'^delete/(?P<pk>[0-9]+)/delete/$', CArDeleteView.as_view(), name='CarDelete'),

    url(r'^lists$', CarListView.as_view(), name ='CarLists'),
    #(r'^carros/', include('carros.urls', namespace ='carros', app_name='auto')),
    #url(r'^carros/',include('.carros.urls', namespace = "carros"))
    url(r'^list$', car_list.as_view(), name='CarList'),


    #url(r'^basic/list$',car_list.as_view(), name='car_list'),)\


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
