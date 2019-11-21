from rest_framework import serializers
from .models import Klient
from .models import Dane_firmy
from .models import Plan_zajec
from .models import Zlecenia
from .models import Grupy
from .models import Personel
from .models import Stanowisko
from .models import Obecnosc
class Klient(serializers.ModelSerializer):
    class Meta:
        model = Klient
        fields = ['Id_klienta', 'Imie', 'Nazwisko', 'Telefon','Kod_pocztowy', 'Adres', 'Miasto', 'Nip']
class Dane_firmy(serializers.ModelSerializer):
    class Meta:
        model = Dane_firmy
        fields = ['Dane_firmy', 'Nazwa_firmy', 'Kod_pocztowy', 'Adres', 'Miasto', 'Id_klienta']
class Plan_zajec(serializers.ModelSerializer):
    class Meta:
        model = Plan_zajec
        fields = ['Id_zajecia', 'Co_zrobic', 'Czy_zrobione']
class Zlecenia(serializers.ModelSerializer):
    class Meta:
        model = Zlecenia
        fields = ['Id_zlecenia', 'Zlecenie', 'Zaplacone', 'Id_klienta', 'Id_zajecia']
class Grupy(serializers.ModelSerializer):
    class Meta:
        model = Grupy
        fields = ['Id_grupy', 'Id_zajecia']
class Personel(serializers.ModelSerializer):
    class Meta:
        model = Personel
        fields = ['Id_osoby', 'Imie', 'Nazwisko', 'Pesel']
class Stanowisko(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['Id', 'Stanowisko', 'Id_grupy', 'Id_osoby']
class Obecnosc(serializers.ModelSerializer):
    class Meta:
        model = Obecnosc
        fields = ['Id_osoby', 'Dzien', 'Godziny_pracy', 'Obecnosc','Id_osoby']
