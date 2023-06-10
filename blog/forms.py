from django import forms
from django.core.exceptions import ValidationError

from blog.services import get_blogs


class BlogForm(forms.Form):
    blog_id = forms.IntegerField(label="Blog number (id):", min_value=1)

    def clean_blog_id(self):
        blog_id = self.cleaned_data["blog_id"]
        if str(blog_id) not in get_blogs():
            raise ValidationError("This blog does not exist. Available numbers below")
        return blog_id
