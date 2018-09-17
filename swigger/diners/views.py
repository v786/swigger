import requests

from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .models import Diner, Review, Visited, Comment, Rating
from .forms import PostForm, ReviewForm, CommentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
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
  paginator = Paginator(latest_diner_list, 5)
  page = request.GET.get('page')
  diners = paginator.get_page(page)
  context = {'latest_diner_list': diners}
  return render(request, 'diners/index.html', context)

def detail(request, diner_id):
    form = ReviewForm()
    comment_form = CommentForm()
    try:
        diner = Diner.objects.get(pk=diner_id)
        location = getCord(diner.location)
        comments = Comment.objects.all()
        visited = Visited.objects.filter(diner = diner, visiter = request.user)
        vote_p = len(Rating.objects.filter(diner = diner))
        if(len(visited) != 0):
            visited = visited[0]
        else:
            visited = 0
        reviews = Review.objects.filter(diner = diner)          
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    
    return render(request, 'diners/detail.html', {'diner': diner, 'form': form, 'visit_status': visited, 'reviews': reviews, 'comment': comment_form, 'comment_list': comments, 'rating_postive': vote_p, 'location': location})

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
    vote_p = len(Rating.objects.filter(diner = diner))
    form = ReviewForm()
    return render(request, 'diners/detail.html', {'diner': diner, 'form': form, 'visit_status': mark_visit, 'rating_postive': vote_p})

def rate_positive(request, diner_id):
    try:
        diner = Diner.objects.get(pk=diner_id)
    except Diner.DoesNotExist:
        raise Http404("Diner does not exist")
    vote = Rating.objects.update_or_create(diner = diner, author = request.user, rating_pos = 1)
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

def post_comment(request, review_id):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            review = Review.objects.get(pk=review_id)
            comment.review = review
            comment.published_date = timezone.now()
            comment.save()
            diner_id = review.diner.id
            p = '/diners/'+str(diner_id)+'/'
            return redirect(p, pk=diner_id)

def getCord(location):
    address = location
    api_key = "AIzaSyCmK4Y5QwyeU6TsrBVJxsJVyIYN7oZz14w"
    api_response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address={0}&key={1}'.format(address, api_key))
    api_response_dict = api_response.json()

    if api_response_dict['status'] == 'OK':
        latitude = api_response_dict['results'][0]['geometry']['location']['lat']
        longitude = api_response_dict['results'][0]['geometry']['location']['lng']
        key = [latitude, longitude]
        return key
    else:
        return "Error"
    