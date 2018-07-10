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
  path('<int:diner_id>/vote/', views.vote, name='vote'),
]