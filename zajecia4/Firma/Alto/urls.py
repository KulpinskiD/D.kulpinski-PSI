from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.Klient_list),
    path('Danef', views.Dane_F),
    path('Zajecia', views.Plan_Z),
    path('Zlecenia', views.Zlecenia_p),
    path('zespoly', views.Grupa),
]