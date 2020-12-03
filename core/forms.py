from django import forms
from core.models import Gallery, Photo


class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = [
            'user',
            'title',
        ]

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = [
            'title',
            'description',
            'alt_text',
            'image',
            'default',
        ]
