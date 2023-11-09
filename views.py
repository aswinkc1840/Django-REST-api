from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Movie, Theater, Ticket
from .serializers import MovieSerializer, TheaterSerializer, TicketSerializer

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class TheaterViewSet(viewsets.ModelViewSet):
    queryset = Theater.objects.all()
    serializer_class = TheaterSerializer

class TicketViewSet(viewsets.ModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
