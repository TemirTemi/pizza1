from django.shortcuts import render
from .models import Pizza, Restaurant
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import RestaurantSerializer, PizzaSerializer
# Create your views here.


class PizzaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer
    #permission_classes = [permissions.IsAuthenticated]



class RestaurantViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    #permission_classes = [permissions.IsAuthenticated]

