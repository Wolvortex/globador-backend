from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, IndicationViewSet, IngredientViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'indications', IndicationViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
