from django.forms import ModelForm, TextInput

from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['content']
        widgets = {
            'content': TextInput(attrs={'class': 'input', 'placeholder': 'say smth'})
        }
