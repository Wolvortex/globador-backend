from django.shortcuts import render
from rest_framework import serializers, viewsets
from .models import Product, Indication, Ingredient
from .serializers import ProductSerializer, IndicationSerializer, IngredientSerializer
from rest_framework.permissions import AllowAny

# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class IndicationViewSet(viewsets.ModelViewSet):
    queryset = Indication.objects.all()
    serializer_class = IndicationSerializer
    permission_classes = [AllowAny]

class IngredientViewSet(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = [AllowAny]
