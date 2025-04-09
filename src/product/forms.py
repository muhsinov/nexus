from django import forms
from .models import Product, ProductImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['user', 'status', 'created_at', 'updated_at']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Price'}),
            'price_on_call': forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'tg-priceoncall'}),
            'description': forms.Textarea(attrs={'id': 'summernote', 'placeholder': 'Description'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'brand': forms.Select(attrs={'class': 'form-select'}),
            'location': forms.Select(attrs={'class': 'form-select'}),
            'condition': forms.Select(attrs={'class': 'form-select'}),
        }
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image', 'is_main']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'placeholder': 'Image'}),
            'is_main': forms.CheckboxInput(attrs={'class': 'custom-control-input', 'id': 'tg-mainimage'}),
        }
