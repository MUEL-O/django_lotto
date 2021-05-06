from django import forms
from .models import GuessNumbers

class PostForm(forms.ModelForm):

    class Meta:
        model = GuessNumbers
        fields = ('name', 'text')
        # class Meta, model, fields 모두 약속
