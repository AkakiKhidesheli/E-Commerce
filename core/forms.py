from django import forms

from . import models
from .models import Product, ProductImage


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('image',)

ProductImageFormSet = forms.modelformset_factory(ProductImage, form=ProductImageForm, extra=5)