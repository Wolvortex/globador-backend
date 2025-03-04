from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib import messages
User = get_user_model()


# Register your models here.
 
@admin.register(User)
class UserAdmin(UserAdmin):
    model = User

    def get_readonly_fields(self, request, obj=None):
        if obj: #This is the case when obj is already created i.e. it's an edit
            return ['id', 'username', 'created', 'modified', 'last_login']
        else:
            return ['id', 'created', 'modified', 'last_login']
    
    REQUIRED_FIELDS = ('username', 'user_type', 'password1', 'password2', )
    
    add_fieldsets = (
        (None, {
            # 'classes': ('wide',),
            'fields': ('username', 'user_type', 'password1', 'password2', ),
        }),
    )
    
    list_display = ['username', 'user_type', 'is_active', 'is_staff', 'is_superuser']
    
    list_display_links = ('username',)

    readonly_fields = ('id', 'username', 'created', 'modified', 'last_login')

    list_filter = ['user_type', 'is_staff']

    fieldsets = (
        ('Details', {'fields': ('username','first_name','last_name')}),
        # ('Personal info', {
        #  'fields': ('full_name','gender', 'date_joined', 'last_login',)}),
        ('States', {
            'fields': ('user_type',  'is_active', 'is_staff', 'is_superuser',)}),
        ('Dates', {
            'fields': ('last_login', 'created', 'modified',)}),
    )

    search_fields = ['username', 'user_type', 'created']

    ordering = ['-created',]
    filter_horizontal = ()


# admin.site.register(User, UserAdmin)
# admin.site.register(Department, DepartmentAdmin)

# Django Groups #
# admin.site.unregister(Group)
