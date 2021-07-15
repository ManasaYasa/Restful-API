from django.shortcuts import render
from rest_framework import viewsets
from .serializers import MovieSerializer
from .models import MovieData
# Create your views here.

class Movieviewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieSerializer


class Actionviewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='Action')
    serializer_class = MovieSerializer


class Comedyviewset(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='comedy')
    serializer_class = MovieSerializer