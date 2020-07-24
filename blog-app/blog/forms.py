from django import forms
from .models import Blog


class BlogAddForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [
            'title',
            'description',
            'meta_description',
            'featured_image',
            'image_url',
            'category',
            'tags'
        ]