from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

CATEGORY_CHOICES = [
    ('Home & Garden', _('Home & Garden')),
    ('Fashion', _('Fashion')),
    ('Electronics', _('Electronics')),
    ('Books', _('Books')),
    ('Music', _('Music')),
    ('Gaming', _('Gaming')),
    ('Stationary', _('Stationary')),
    ('Other', _('Other')),
]

SUBCATEGORY_CHOICES = [
    ('Kitchen', _('Kitchen')),
    ('Textile', _('Textile')),
    ('Organizers', _('Organizers')),
    ('Decor', _('Decor')),
    ('Lighting', _('Lighting')),
    ('Furniture', _('Furniture')),
    ('Bathroom', _('Bathroom')),
    ('Clothing', _('Clothing')),
    ('Footwear', _('Footwear')),
    ('Accessories', _('Fashion Accessories')),
    ('Jewelry', _('Jewelry')),
    ('Mobile Phones', _('Mobile Phones')),
    ('Laptops', _('Laptops')),
    ('Headphones', _('Headphones')),
    ('Cameras', _('Cameras')),
    ('TVs', _('TVs')),
    ('Instruments', _('Instruments')),
    ('Vinyl', _('Vinyl')),
    ('CDs', _('CDs')),
    ('Headphones', _('Headphones')),
    ('Consoles', _('Consoles')),
    ('PC Games', _('PC Games')),
    ('Gaming Accessories', _('Gaming Accessories')),
    ('Virtual Reality', _('Virtual Reality')),
    ('Pens & Pencils', _('Pens & Pencils')),
    ('Notebooks', _('Notebooks')),
    ('Art Supplies', _('Art Supplies')),
    ('Other', _('Other')),
]


# Create your models here.

class ProductAttribute(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'product_attributes'


class Product(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name=_('Name'))
    price = models.FloatField(null=False, blank=False, verbose_name=_('Price'))
    quantity = models.PositiveIntegerField(null=False, blank=False, verbose_name=_('Quantity'))
    category = models.CharField(null=False, blank=False, choices=CATEGORY_CHOICES, verbose_name=_("Category"))
    subcategory = models.CharField(null=True, blank=True, choices=SUBCATEGORY_CHOICES, verbose_name=_('Subcategory'))
    description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'products'

    def not_in_stock(self):
        if self.quantity <= 0:
            return True
        else:
            return False


class ProductAttributeValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='attribute_values')
    attribute = models.ForeignKey(ProductAttribute, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    class Meta:
        db_table = 'product_attribute_values'
        unique_together = ('product', 'attribute')


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)

    class Meta:
        db_table = 'product_images'
