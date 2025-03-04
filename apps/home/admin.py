from django.contrib import admin
from .models import Product, Indication, Ingredient, Category
from django.contrib.auth.models import Group
# Register your models here.

class IndicationInline(admin.TabularInline):
    model = Indication
    extra = 1  # Number of empty forms to display

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product

    list_display = ['id', 'name', 'category', 'dosage', 'packaging', 'created', 'modified']
    list_display_links = ('name',)

    readonly_fields = ('id', 'created', 'modified', )

    fieldsets = (
        ('Info', {'fields': ('name', 'category', 'dosage', 'packaging')}),
        ('Details', {'fields': ('image',)}),
        ('Dates', {'fields': ('created', 'modified',)}),
    )

    search_fields = ['name', 'dosage', 'packaging']
    ordering = ['-created',]

    inlines = [IndicationInline, IngredientInline]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

    list_display = ['id', 'name',]
    list_display_links = ('name',)

    readonly_fields = ('id',)

    fieldsets = (
        ('Info', {'fields': ('name',)}),
    )

    search_fields = ['name', ]


# admin.site.register(Department, DepartmentAdmin)

# Django Groups #
admin.site.unregister(Group)
