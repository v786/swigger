from django import forms

from .models import Diner, Review, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Diner
        fields = ('diner_name', 'location',)
        widgets = {'diner_name': forms.TextInput(attrs={'class': 'form-control'}),
        'location': forms.Textarea(attrs={'class': 'form-control'}),
        }
      

class ReviewForm(forms.ModelForm):
  """docstring for ReviewForm"""
  class Meta:
    model = Review
    fields = ('review_title', 'review_text',)
    widgets = {'review_title': forms.TextInput(attrs={'class': 'form-control'}),
     'review_text': forms.Textarea(attrs={'class': 'form-control'}),
    }

class CommentForm(forms.ModelForm):
  """docstring for ReviewForm"""
  class Meta:
    model = Comment
    fields = ('comment_text',)
    widgets = {'comment_text': forms.Textarea(attrs={'class': 'form-control'}),}
      
    