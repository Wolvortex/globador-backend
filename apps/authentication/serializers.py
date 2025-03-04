from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
from rest_framework.exceptions import AuthenticationFailed
from django.utils import timezone
from datetime import timedelta
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import exceptions
from django.contrib.auth.models import update_last_login
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            # fields = ['username','user_type','is_active','is_staff','is_superuser','is_director','password']
            # fields = '__all__'
            fields = ["id", "last_login", "first_name", "last_name", "email", "date_joined", "username", "user_type", "is_active", "is_staff", "is_superuser", "created", "modified", "groups", "user_permissions",]


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Decode the token to access the user information
        decoded_token = token_backend.decode(data['access'], verify=False)
        
        # Check if the user_type is 'admin'
        if decoded_token.get('user_type') == 'admin':
            data['user_type'] = 'admin'  # Add `user_type` to response
            
        try:
            user = User.objects.get(id=decoded_token['user_id'])
            update_last_login(User, user)
        except:
            raise AuthenticationFailed('No active account found with the given credentials')
        return data

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Include `user_type` in the token if the user is an admin
        if user.user_type == 'admin':
            token['user_type'] = user.user_type  # Add `user_type` to token
        
        update_last_login(User, user)
        
        return token

    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Add `user_type` to login response if the user is an admin
        if self.user.user_type == 'admin':
            data['user_type'] = self.user.user_type
        
        # Manage outstanding tokens: Keep only the last two tokens for the user
        outstanding_tokens = OutstandingToken.objects.filter(user=self.user).order_by('created_at')
        if outstanding_tokens.count() > 2:  # More than 2 tokens
            tokens_to_blacklist = outstanding_tokens[:outstanding_tokens.count() - 2]  # Keep the last two tokens
            for token in tokens_to_blacklist:
                try:
                    BlacklistedToken.objects.get_or_create(token=token)
                    token.delete()
                except Exception as e:
                    # Log the exception if needed
                    pass
                
        return data
    
    
                

# class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         # Get the default token data
#         data = super().validate(attrs)

#         # Add the `user_type` to the response if user_type is 'admin'
#         user = self.user
#         if user.user_type == 'admin':
#             data['user_type'] = 'admin'
        
#         return data


# class CustomTokenRefreshSerializer(TokenRefreshSerializer):
#     def validate(self, attrs):
#         token_payload = token_backend.decode(attrs['refresh'])

#         try:
#             user = get_user_model().objects.get(pk=token_payload['user_id'])
#         except get_user_model().DoesNotExist:
#             raise exceptions.AuthenticationFailed('No active account found with the given credentials')

#         # Add custom claim for user_type if it's "admin"
#         if user.user_type == "admin":
#             token_payload['user_type'] = user.user_type

#         # Perform validation for standard fields
#         return super().validate(attrs)