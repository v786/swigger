from django.db import models

from django.utils import timezone

# Create your models here.

class Diner(models.Model):
  diner_name = models.CharField(max_length = 200)
  location = models.TextField()
  published_date = models.DateTimeField(default = timezone.now)

  def __str__(self):
        return self.diner_name


class Rating(models.Model):
  """docstring for Rating"""
  diner = models.ForeignKey(Diner, on_delete=models.CASCADE)
  rating_pos = models.IntegerField(default=0)
  rating_neg = models.IntegerField(default=0)

  def __str__(self):
        return self.rating_pos

class Review(models.Model):
  """docstring for Rating"""
  diner = models.ForeignKey(Diner, on_delete=models.CASCADE)
  review_title = models.CharField(max_length = 200)
  review_text = models.TextField()
  published_date = models.DateTimeField(default = timezone.now)

  def __str__(self):
        return self.review_title

