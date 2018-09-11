from django.db import models

from django.utils import timezone

# Create your models here.

class Diner(models.Model):
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  diner_name = models.CharField(max_length = 200)
  location = models.TextField()
  visted = models.TextField(default="No")
  published_date = models.DateTimeField(default = timezone.now)

  def __str__(self):
        return self.diner_name

class Visited(models.Model):
  diner = models.ForeignKey(Diner, on_delete=models.CASCADE)
  visiter = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  visit_date = models.DateTimeField(default = timezone.now)

class Rating(models.Model):
  """docstring for Rating"""
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  diner = models.ForeignKey(Diner, on_delete=models.CASCADE)
  rating_pos = models.IntegerField(default=0)
  rating_neg = models.IntegerField(default=0)
  author = models.TextField()
  
  def __str__(self):
        return self.rating_pos

class Review(models.Model):
  """docstring for Rating"""
  diner = models.ForeignKey(Diner, on_delete=models.CASCADE)
  review_title = models.CharField(max_length = 200)
  review_text = models.TextField()
  author = models.TextField()
  published_date = models.DateTimeField(default = timezone.now)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)

  def __str__(self):
        return self.review_title

class Comment(models.Model):
  """docstring for Rating"""
  review = models.ForeignKey(Review, on_delete=models.CASCADE)
  comment_text = models.TextField()
  published_date = models.DateTimeField(default = timezone.now)
  author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  
  def __str__(self):
        return self.comment_text



