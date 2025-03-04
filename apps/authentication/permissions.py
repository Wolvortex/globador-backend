# from rest_framework.exceptions import AuthenticationFailed
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework_simplejwt.token_blacklist.models import OutstandingToken, BlacklistedToken
# from django.utils import timezone
# from datetime import timedelta


# class CustomJWTAuthentication(JWTAuthentication):
#     def decode_handler(self, token):
#         decoded_token = super().decode_handler(token)
        
#         # Attempt to retrieve the OutstandingToken
#         outstanding_token = OutstandingToken.objects.filter(token=token).first()
        
#         if not outstanding_token:
#             # If token is not found in OutstandingToken, raise an Authentication error
#             raise AuthenticationFailed("Token is invalid or not found.")
        
#         # Continue with other checks for expiration or blacklisting
#         if outstanding_token.expires_at and outstanding_token.expires_at < timezone.now():
#             raise AuthenticationFailed("Token has expired.")
        
#         if BlacklistedToken.objects.filter(token=outstanding_token).exists():
#             raise AuthenticationFailed("Token has been blacklisted.")
        
#         return decoded_token