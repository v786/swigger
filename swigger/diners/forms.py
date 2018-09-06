from django import forms

from .models import Diner

class PostForm(forms.ModelForm):

    class Meta:
        model = Diner
        fields = ('diner_name', 'location',)