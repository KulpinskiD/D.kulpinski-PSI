from django.urls import path
from . import views

urlpatterns = [
    path('klienci/', views.Klient_list.as_view),
    path('klienciD/<int:pk>', views.Klient_list_detail.as_view ()),
    path('Danef', views.Dane_F),
    path('Prac', views.Pracownicy),
    path('Prac/<int:pk>', views.Pracownicy_detail),
    path('Zlecenia', views.Zlecenia_p),
    path('Obecn', views.Obecnosci),

]