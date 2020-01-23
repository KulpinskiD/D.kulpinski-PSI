from django.db import models

# Create your models here.
class Klient(models.Model):
    Imie= models.CharField(max_length=45)
    Nazwisko=models.CharField(max_length=45)
    Telefon=models.CharField(max_length=9)
    Kod_pocztowy = models.CharField(max_length=6)
    Adres = models.CharField(max_length=45)
    Miasto = models.CharField(max_length=45)


class Dane_firmy(models.Model):
    Nip = models.CharField(max_length=11)
    Nazwa_firmy = models.CharField(max_length=45)
    Kod_pocztowy = models.CharField(max_length=6)
    Adres = models.CharField(max_length=45)
    Miasto= models.CharField(max_length=45)
    klient=models.ForeignKey(Klient, on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='Firma', on_delete=models.CASCADE)

class Personel(models.Model):
    Imie = models.CharField(max_length=45)
    Nazwisko = models.CharField(max_length=45)
    Pesel = models.CharField(max_length=11)
    Grupa=models.IntegerField()


class Zlecenia(models.Model):
    Zlecenie=models.TextField(max_length=300)
    Zaplacone= models.BooleanField()
    klient = models.ForeignKey(Klient, on_delete=models.CASCADE)



class Obecnosc(models.Model):
    Dzien=models.DateTimeField(auto_now_add = True)
    Obecnosc = models.BooleanField()
    osoba = models.ForeignKey(Personel, on_delete=models.CASCADE)

