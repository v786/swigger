from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Diner, Review, Visited
from .forms import PostForm, ReviewForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        return redirect('/diners/')
    else:
        # Return an 'invalid login' error message.
        return redirect('/diners/')

def signout(request):
    logout(request)
    # Redirect to a success page.
    return redirect('/diners/')

def index(request):
  latest_diner_list = Diner.objects.order_by('-published_date')
  context = {'latest_diner_list': latest_diner_list}
  return render(request, 'diners/index.html', context)

def detail(request, diner_id):
    form = ReviewForm()
    try:
        diner = Diner.objects.get(pk=diner_id)
        
        visited = Visited.objects.filter(diner = diner, visiter = request.user)
        if(len(visited) != 0):
            visited = visited[0]
        else:
            visited = 0
        reviews = Review.objects.filter(diner = diner)          
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    
    return render(request, 'diners/detail.html', {'diner': diner, 'form': form, 'visit_status': visited, 'reviews': reviews})

def results(request, diner_id):
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    try:
        reviews = Review.objects.filter(diner = diner)  
    except Review.DoesNotExist:
        raise Http404("Diner does not exist")
    return render(request, 'diners/results.html', {'diner': diner ,'reviews': reviews})

def mark_visited(request, diner_id):
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    mark_visit = Visited.objects.get_or_create(diner = diner, visiter = request.user)
    form = ReviewForm()
    return render(request, 'diners/detail.html', {'diner': diner, 'form': form, 'visit_status': mark_visit})


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
            diner.author = request.user
            diner.published_date = timezone.now()
            diner.save()
            p = '/diners/'+str(diner.pk)+'/'
            return redirect(p, pk=diner.pk)
    else:
        form = PostForm()
    return render(request, 'diners/post_edit.html', {'form': form})

def post_review(request, diner_id):
    form = ReviewForm()
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.diner = Diner.objects.get(pk=diner_id)
            review.published_date = timezone.now()
            review.save()
            p = '/diners/'+str(diner_id)+'/'
            return redirect(p, pk=diner_id)