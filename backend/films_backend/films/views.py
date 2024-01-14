from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from films.models import Film
from films.serializers import FilmSerializer
from rest_framework import viewsets


def home(request):
    return HttpResponse("Welcome to the Home Page! Go to 'http://localhost:8000/api/films/' to see data!")


class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer


# class FilmListAPIView(generics.ListAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer


# class FilmDetailAPIView(generics.RetrieveAPIView):
#     queryset = Film.objects.all()
#     serializer_class = FilmSerializer
