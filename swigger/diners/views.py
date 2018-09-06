from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.http import Http404
from .models import Diner
from .models import Review
from .forms import PostForm
from django.shortcuts import redirect

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
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    try:
        reviews = Review.objects.all()  
    except Review.DoesNotExist:
        raise Http404("Diner does not exist")
    return render(request, 'diners/results.html', {'diner': diner ,'reviews': reviews})

def vote(request, diner_id):
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    return render(request, 'diners/comment_page.html', {'diner': diner})

def post_new(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            diner = form.save(commit=False)
            diner.published_date = timezone.now()
            diner.save()
            p = '/diners/'+str(diner.pk)+'/'
            return redirect(p, pk=diner.pk)
    else:
        form = PostForm()
    return render(request, 'diners/post_edit.html', {'form': form})