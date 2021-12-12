from django.shortcuts import render
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
#from rest_framework.decorators import list_route
from rest_framework.permissions import AllowAny
from .models import Contact
from .serializers import ContactSerializer
from .utils import login

class ContactViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

