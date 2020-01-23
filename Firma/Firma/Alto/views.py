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
from django.contrib.auth.models import User
from .serializers import UserSerializer


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
        serializer = KlientS(Klie)
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


class Dane_F(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get(self, request, format=None):
        Firmy = Dane_firmy.objects.all()
        serializer = Dane_firmyS(Firmy, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Dane_firmyS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
class Dane_F_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Dane_firmy.objects.get(pk=pk)
        except Dane_firmy.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Firmy = self.get_object(pk)
        serializer = Dane_firmyS(Firmy)
        return Response(serializer.data)

    def post(self, request, format=None):
        Firmy = self.get_object(pk)
        serializer = Dane_firmyS(Firmy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Firmy = self.get_object(pk)
        Firmy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Pracownicy(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        Osoby = Personel.objects.all()
        serializer = PersonelS(Osoby, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PersonelS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
class Pracownicy_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Personel.objects.get(pk=pk)
        except Personel.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Osoby = self.get_object(pk)
        serializer = PersonelS(Osoby)
        return Response(serializer.data)

    def post(self, request, format=None):
        Osoby = self.get_object(pk)
        serializer = PersonelS(Osoby, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Osoby = self.get_object(pk)
        Osoby.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Zlecenia_p(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        Zlecenie = Zlecenia.objects.all()
        serializer = ZleceniaS(Zlecenie, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ZleceniaS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)

class Zlecenia_p_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Zlecenia.objects.get(pk=pk)
        except Zlecenia.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Zlecenie = self.get_object(pk)
        serializer = PersonelS(Zlecenie)
        return Response(serializer.data)

    def post(self, request, format=None):
        Zlecenie = self.get_object(pk)
        serializer = ZleceniaS(Zlecenie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Zlecenie = self.get_object(pk)
        Zlecenie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class Obecnosci(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, format=None):
        Jest = Obecnosc.objects.all()
        serializer = ObecnoscS(Jest, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ObecnoscS(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        return Response(serializer.data, status.HTTP_400_BAD_REQUEST)
class Obecnosci_detail(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Obecnosc.objects.get(pk=pk)
        except Obecnosc.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        Jest = self.get_object(pk)
        serializer = ObecnoscS(Jest)
        return Response(serializer.data)

    def post(self, request, format=None):
        Jest = self.get_object(pk)
        serializer = ObecnoscS(Jest, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Jest = self.get_object(pk)
        Jest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class UserList(generics.ListAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
   queryset = User.objects.all()
   serializer_class = UserSerializer
