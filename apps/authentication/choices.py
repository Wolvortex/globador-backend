from django.db import models


# Create your models here.
class User_Type(models.TextChoices):
    ADMIN = 'admin', 'Admin'
    DIRECTOR = 'director','Director'
    SUPERVISOR = 'supervisor','Supervisor'
    
# class User_Department(models.TextChoices):
#     IT = 'it', 'It'
