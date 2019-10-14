from django.shortcuts import render
from rest_framework import viewsets
from App.models import  Book
from App.serializers import BookSerializers

# Create your views here.

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializers

