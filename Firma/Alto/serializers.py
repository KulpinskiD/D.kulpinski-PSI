from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class KlientS(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['Imie', 'Nazwisko', 'Telefon','Kod_pocztowy', 'Adres', 'Miasto']
class Dane_firmyS(serializers.ModelSerializer):
    class Meta:
        model = Dane_firmy
        fields = ['Nip','Nazwa_firmy', 'Kod_pocztowy', 'Adres', 'Miasto', 'klient',]
class PersonelS(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ['Imie', 'Nazwisko', 'Pesel','Grupa']
class ZleceniaS(serializers.ModelSerializer):
    class Meta:
        model = Zlecenia
        fields = [ 'Zlecenie', 'Zaplacone', 'klient']
class ObecnoscS(serializers.ModelSerializer):
    class Meta:
        model = Obecnosc
        fields = ['Dzien', 'Obecnosc', 'osoba']
class UserSerializer(serializers.ModelSerializer):
    Klient = serializers.PrimaryKeyRelatedField(many=True, queryset=Klient.objects.all())
class Meta:
    model = User
    fields = ['id', 'username', 'Klient']