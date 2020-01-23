from django.urls import path
from . import views

urlpatterns = [
    path('klienci', views.Klient_list.as_view()),
    path('klienciD/<int:pk>', views.Klient_list_detail.as_view()),
    path('Danef', views.Dane_F.as_view()),
    path('Dane_f_D/<int:pk>', views.Dane_F_detail.as_view()),
    path('Prac', views.Pracownicy.as_view()),
    path('PracD/<int:pk>', views.Pracownicy_detail.as_view()),
    path('Zlecenia', views.Zlecenia_p.as_view()),
    path('ZleceniaD/<int:pk>', views.Zlecenia_p_detail.as_view()),
    path('Obecn', views.Obecnosci.as_view()),
    path('ZleceniaD/<int:pk>', views.Obecnosci_detail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]