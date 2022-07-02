from dataclasses import field
from pyexpat import model
from django import forms
from .models import LinkApp

class LinkAppForm(forms):
    
    class Meta:
        model = LinkApp
        
        fields = [
            "target_url",
            "description",
        ]