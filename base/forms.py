from django import forms
from .models import Comments

class CommentClass(forms.ModelForm):
    class Meta:
        model=Comments
        fields=('name','email','body')
        