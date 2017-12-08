
from django.conf.urls import url, include
from .views import prueba
from carros import views
#from autoSearch import urls




urlpatterns = [
    url(r'^$',prueba, name='index'),
    #url(r'^car_list/', views.car_list, name='car_list'),
]
