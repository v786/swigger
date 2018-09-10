from django import forms

from .models import Diner, Review, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Diner
        fields = ('diner_name', 'location',)

class ReviewForm(forms.ModelForm):
  """docstring for ReviewForm"""
  class Meta:
    model = Review
    fields = ('review_title', 'review_text',)

class CommentForm(forms.ModelForm):
  """docstring for ReviewForm"""
  class Meta:
    model = Comment
    fields = ('comment_text',)
      
    