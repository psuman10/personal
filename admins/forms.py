from ecommerce.models import Product
from django import forms


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "category", "product_image", "selling_price",
                  "discounted_price", "description", "brand"]
        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter the product title here..."
            }),
           
            "category": forms.Select(attrs={
                "class": "form-control"
            }),
            "product_image": forms.ClearableFileInput(attrs={
                "class": "form-control"
            }),
            "selling_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "Markedselling  price of the product..."
            }),
            "discounted_price": forms.NumberInput(attrs={
                "class": "form-control",
                "placeholder": "dis price of the product..."
            }),
            "description": forms.Textarea(attrs={
                "class": "form-control",
                "placeholder": "Description of the product...",
                "rows": 5
            })

        }