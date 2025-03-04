from django.contrib.auth.models import BaseUserManager
from django.core.exceptions import ValidationError  
# from .models import Department
from django.apps import apps

class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, username, user_type,password=None,
                    **extra_fields):
        """
        Create and save a User with the given username and password.
        """
        if not username:
            raise ValidationError('username Must Be Set')
        if not user_type:
            raise ValidationError('Choices are [ ADMIN-DIRECTOR-SUPERVISOR ]')
        if not password:
            raise ValidationError('Password Must Be Set')
        
        user = self.model(
            username=username.lower(),
            user_type=user_type,
            password=password,
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, user_type='admin', password=None,**extra_fields):
        user = self.create_user(
            username=username.lower(),
            user_type=user_type,
            password=password,
        )
        user.set_password(password)
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user