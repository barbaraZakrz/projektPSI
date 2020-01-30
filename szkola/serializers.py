from rest_framework import serializers
from szkola.models import *


class NauczycielSerializer(serializers.ModelSerializer):
    class Meta:
        model: Nauczyciel
        fields = '__all__'


class KursSerializer(serializers.ModelSerializer):
    class Meta:
        model: Kurs
        fields = '__all__'


class UczenSerializer(serializers.ModelSerializer):
    class Meta:
        model: Uczen
        fields = '__all__'


class DzienSerializer(serializers.ModelSerializer):
    class Meta:
        model: Dzien
        fields: '__all__'


class RodzajSerializer(serializers.ModelSerializer):
    class Meta:
        model: Rodzaj
        fields: '__all__'


class Nauczyciel_RodzajSerializer(serializers.ModelSerializer):
    class Meta:
        model: Nauczyciel_Rodzaj
        fields = '__all__'

