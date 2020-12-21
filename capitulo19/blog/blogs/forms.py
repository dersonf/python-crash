from django import forms

from .models import BlogPost


class BlogPostForm(forms.ModelForm):
    class <eta:
        model = BlogPost
        fields = ['title', 'text']
        labels = {'text': ''}
