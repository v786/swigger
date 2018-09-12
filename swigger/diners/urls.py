#urls.py
from django.urls import path

from . import views

app_name = 'diners'

urlpatterns = [
  # ex: /diners/
  path('', views.index, name='index'),
  # ex: /diners/5/
  path('<int:diner_id>/', views.detail, name='detail'),
  # ex: /diners/5/results/
  path('<int:diner_id>/results/', views.results, name='results'),
  # ex: /diners/5/vote/
  path('<int:diner_id>/rate/', views.rate_positive, name='rate_positive'),

  path('<int:diner_id>/rate/', views.rate_positive, name='rate_positive'),

  path('new/', views.post_new, name='post_new'),

  path('new_comment/<int:review_id>/', views.post_comment, name='post_comment'),

  path('add/<int:diner_id>/', views.post_review, name='post_review'),

  path('logout/', views.signout, name='signout'),

  path('login/', views.signin, name='signin'),

  path('mark-visited/<int:diner_id>', views.mark_visited, name='mark_visited'),
]