from django import forms
from .models import PythonType, Product, Review

class ProductFrom(forms.ModelForm):
     class Meta:
        model=Product
        fields='__all__'