from django.shortcuts import render
from rest_framework import generics
from .serializer import RoomSerializers
from .models import Room

# Create your views here.
class RoomView(generics.ListAPIView):
    query = Room.objects.all()
    serializer_class = RoomSerializers
