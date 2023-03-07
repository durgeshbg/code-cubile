from django import forms
from .models import *


class ListForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ["title", "description", "bid", "img_url", "category"]
        labels = {
            "title": "Title", 
            "description": "Description", 
            "bid": "Bid", 
            "img_url": "Image Url", 
            "category": "Category"
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control", "placeholder": "Title of the listing"}),
            "description": forms.Textarea(attrs={"class": "form-control","rows":"9" ,"placeholder": "Describe your listing"}),
            "bid": forms.NumberInput(attrs={"class": "form-control", "placeholder": "In USD"}),
            "img_url": forms.URLInput(attrs={"class": "form-control", "placeholder": "Paste image url (if any)"}),
            "category": forms.Select(
                attrs={"class": "form-control"},
                choices=[
                    ("Fashion", "Fashion"),
                    ("Toys", "Toys"),
                    ("Electronics", "Electronics"),
                    ("Home", "Home"),
                    ("Others", "Others"),
                ],
            ),
        }
