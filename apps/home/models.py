from django.db import models
from django.contrib.postgres.fields import ArrayField  # Import ArrayField for list fields
from django.core.validators import FileExtensionValidator  # Validator for image files
from django.utils.translation import gettext as _
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

def ProductImage_Upload(instance, filename):
    return f'products/{instance.name}/{filename}'

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
        # Check if there is an image being saved
        if self.image:
            # Open the uploaded image
            img = Image.open(self.image)
            
            # Convert to RGB if image has transparency (PNG)
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Calculate the new dimensions while preserving aspect ratio
            max_size = (500, 500)  # You can adjust this to your preferred maximum size
            img.thumbnail(max_size, Image.BICUBIC)  # BICUBIC is a good balance between quality and performance
            
            # Create an in-memory file
            output = io.BytesIO()
            
            # Save the image to the in-memory file with optimized quality
            img.save(output, format='JPEG', quality=85, optimize=True)  # Adjust quality as needed (85 is a good balance)
            output.seek(0)
            
            # Replace the image field with the processed image
            self.image = InMemoryUploadedFile(
                output,
                'ImageField',
                f"{self.image.name.split('.')[0]}.jpg",
                'image/jpeg',
                sys.getsizeof(output),
                None
            )
            
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