from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Diner

# Create your views here.

def index(request):
  latest_diner_list = Diner.objects.order_by('-published_date')[:5]
  context = {'latest_diner_list': latest_diner_list}
  return render(request, 'diners/index.html', context)
def detail(request, diner_id):
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    return render(request, 'diners/detail.html', {'diner': diner})

def results(request, diner_id):
    response = "You're looking at the results of diner %s."
    return HttpResponse(response % question_id)

def vote(request, diner_id):
    return HttpResponse("You're voting on diner %s." % diner_id)
