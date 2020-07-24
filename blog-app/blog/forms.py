from django import forms
from .models import Blog
from tinymce.widgets import TinyMCE


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

        widget = {
            'description': TinyMCE(attrs={'cols': 80, 'rows': 30}),
        }