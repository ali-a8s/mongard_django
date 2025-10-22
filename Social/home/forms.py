from django import forms 
from accounts.models import Post


class PostCreateUpdateForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields = ("body",)
