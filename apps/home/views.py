from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Product, Indication, Ingredient
from .serializers import ProductSerializer, IndicationSerializer, IngredientSerializer

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class IndicationViewSet(viewsets.ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
