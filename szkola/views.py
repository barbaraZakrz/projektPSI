from django.shortcuts import render
from szkola.models import *
from szkola.serializers import *
from rest_framework import generics
from rest_framework import permissions
from django.conf.urls import url, include


class NauczycielDetail(generics.RetrieveAPIView):
    queryset = Nauczyciel.objects.all()
    serializer_class = NauczycielSerializer


class NauczycielList(generics.ListCreateAPIView):
    queryset = Nauczyciel.objects.all()
    serializer_class = NauczycielSerializer


class KursDetail(generics.RetrieveAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class KursList(generics.ListCreateAPIView):
    queryset = Kurs.objects.all()
    serializer_class = KursSerializer


class UczenDetail(generics.RetrieveAPIView):
    queryset = Uczen.objects.all()
    serializer_class = UczenSerializer

class UczenList(generics.ListCreateAPIView):
    queryset = Uczen.objects.all()
    serializer_class = UczenSerializer


class DzienDetail(generics.RetrieveAPIView):
    queryset = Dzien.objects.all()
    serializer_class = DzienSerializer

class DzienList(generics.ListCreateAPIView):
    queryset = Dzien.objects.all()
    serializer_class = DzienSerializer


class RodzajDetail(generics.RetrieveAPIView):
    queryset = Rodzaj.objects.all()
    serializer_class = RodzajSerializer

class RodzajList(generics.ListCreateAPIView):
    queryset = Rodzaj.objects.all()
    serializer_class = RodzajSerializer


class Nauczyciel_RodzajDetail(generics.RetrieveAPIView):
    queryset = Nauczyciel_Rodzaj.objects.all()
    serializer_class = Nauczyciel_Rodzaj

class Nauczyciel_RodzajList(generics.ListCreateAPIView):
    queryset = Nauczyciel_Rodzaj.objects.all()
    serializer_class = Nauczyciel_RodzajSerializer
