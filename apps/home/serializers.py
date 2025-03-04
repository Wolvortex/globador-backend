from rest_framework import serializers
from .models import Product, Indication, Ingredient, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        
class IndicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indication
        fields = ['id', 'text']

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id', 'text']

class ProductSerializer(serializers.ModelSerializer):
    indications = IndicationSerializer(many=True, read_only=True)
    ingredients = IngredientSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'category', 'dosage', 'packaging', 'image', 'created', 'modified', 'indications', 'ingredients']
