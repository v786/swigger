from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
  return HttpResponse("Hello world ! You are at Diners.")

def detail(request, diner_id):
    return HttpResponse("You're looking at diner %s." % diner_id)

def results(request, diner_id):
    response = "You're looking at the results of diner %s."
    return HttpResponse(response % question_id)

def vote(request, diner_id):
    return HttpResponse("You're voting on diner %s." % diner_id)
