from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework import permissions
from django.http import Http404


class Klient_list(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        Klienci = Klient.objects.all()
        serializer = KlientS(Klienci, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = KlientS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)


class Klient_list_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Klient.objects.get(pk=pk)
        except Klient.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Klie = self.get_object(pk)
        serializer = KlientSerializer(Klie)
        return Response(serializer.data)

    def post(self, request, format=None):
        Klie = self.get_object(pk)
        serializer = KlientS(Klie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Klie = self.get_object(pk)
        Klie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def Dane_F(request):
    if request.method == 'GET':
        Firmy = Dane_firmy.objects.all()
        serializer = Dane_firmyS(Firmy, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Dane_firmyS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def Pracownicy(request):
    if request.method == 'GET':
        Osoby = Personel.objects.all()
        serializer = PersonelS(Osoby, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonelS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
@api_view(['GET', 'POST','DELETE'])
def Pracownicy_detail(request,pk):
    try:
        Pers = Personel.objects.get(pk=pk)
    except Personel.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        Osoby= Personel.objects.all()
        serializer = PersonelS(Osoby, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ObecnoscS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        Pers.delete()
    return HttpResponse(status=204)


@api_view(['GET','POST'])
def Zlecenia_p(request):
    if request.method == 'GET':
        Zlecenie = Zlecenia.objects.all()
        serializer = ZleceniaS(Zlecenie, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ZleceniaS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
""""@api_view(['GET','POST','DELETE'])
def Zlecenia_p_detail(request,pk):
    try:
        zajecje = Zlecenia.objects.get(pk=pk)
    except Zlecenia.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        Zlecenie = Zlecenia.objects.all()
        serializer = ZleceniaS(Zlecenie, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ZleceniaS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        zajecje.delete()
    return HttpResponse(status=204)
"""
@api_view(['GET', 'POST'])
def Obecnosci(request,):
    if request.method == 'GET':
        Jest= Obecnosc.objects.all()
        serializer = ObecnoscS(Jest, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ObecnoscS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
""""@api_view(['GET', 'POST','DELETE'])
def Obecnosci_detail(request,pk):
    try:
        pot = Obecnosc.objects.get(pk=pk)
    except Obecnosc.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        Jest= Obecnosc.objects.all()
        serializer = ObecnoscS(Jest, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ObecnoscS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        pot.delete()
    return HttpResponse(status=204)"""