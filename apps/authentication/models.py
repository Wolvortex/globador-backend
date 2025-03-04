from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractUser
from .managers import CustomUserManager
from django.utils.translation import gettext as _
from django.core.exceptions import ValidationError  
from .choices import User_Type #, User_Department

# # Create your models here.
# def ProfileImage_Upload(instance, filename):
#     imagename, extension = filename.split(".")
#     return "User/Images/%s/%s.jpg" % (instance.user.email, instance.user.id)

    
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(unique=True, max_length=100, null=False, blank=False)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    # is_manager = models.BooleanField(default=False)
    # department = models.ForeignKey(Department, on_delete = models.CASCADE, related_name = 'department')
    # user_department = models.CharField(_("User Department"), max_length=20, choices=User_Department.choices, blank=False, default=User_Department.IT)
    
    user_type = models.CharField(_("User Type"), max_length=20, choices=User_Type.choices, blank=False, default='supervisor')
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    # is_director = models.BooleanField(default=False)
    
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True)
    
    objects = CustomUserManager()
    
    USERNAME_FIELD = 'username'
    # USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']
    
    # ordering = ('created',)
    class Meta:
        verbose_name = _("Platform User")
        verbose_name_plural = _("Platform Users")
        
        indexes = [
            models.Index(fields=['id', 'username']),
            models.Index(fields=['user_type']),
        ]

    def __str__(self):
        return str(self.username)

    def save(self, *args, **kwargs):
        # email = self.email.split('@')
        # username = email[0]
        # self.username = username
        
        # self.username = f'{self.first_name} {self.last_name}'
        super(User, self).save(*args, **kwargs)