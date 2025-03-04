
from django.urls import path
from . import views
from .views import CustomTokenObtainPairView, CustomTokenRefreshView #,MyTokenObtainPairView

# from rest_framework_simplejwt.views import (
#     TokenRefreshView,
# )

urlpatterns = [
    path('profile/', views.get_profile),
    # path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
