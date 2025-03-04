from django.db import models
from django.contrib.postgres.fields import ArrayField  # Import ArrayField for list fields
from django.core.validators import FileExtensionValidator  # Validator for image files
from django.utils.translation import gettext as _

def ProductImage_Upload(instance, filename):
    return "Product/Images/%s.jpg" % (instance.name)

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        super(Category, self).save(*args, **kwargs)

    

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    
    dosage = models.CharField(max_length=200)
    packaging = models.CharField(max_length=200)
    
    image = models.ImageField(upload_to=ProductImage_Upload, validators=[FileExtensionValidator(['jpg', 'png', 'jpeg'])], blank=True, null=True)
    
    created = models.DateTimeField('created', auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

        indexes = [
            models.Index(fields=['id', 'name', 'modified']),
        ]
        
    def __str__(self):
        return f"{self.name}"
    

    def save(self, *args, **kwargs):
        super(Product, self).save(*args, **kwargs)


class Ingredient(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ingredients')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text

# New model for Indications
class Indication(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='indications')
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text