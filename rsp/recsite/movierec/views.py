from django.shortcuts import get_object_or_404, render
from .models import Review, Movie

from .form import ReviewForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
import datetime

def review_list(request):
    latest_review_list = Review.objects.order_by('-pub_date')[:9]
    context = {'latest_review_list':latest_review_list}
    return render(request, 'review_list.html', context)

def review_detail(request, pk):
    review = get_object_or_404(Review, id=pk)
    return render(request, 'review_detail.html', {'review': review})

def movie_list(request):
    movie_list = Movie.objects.order_by('-title')[:20]
    context = {'movie_list':movie_list}
    return render(request, 'movie_list.html', context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    form = ReviewForm()
    return render(request, 'movie_detail.html', {'movie': movie})

def add_review(request, pk):
    movie = get_object_or_404(Movie, id=pk)
    form = ReviewForm(request.POST)
    if form.is_valid():
        rating = form.cleaned_data['rating']
        comment = form.cleaned_data['comment']
        user_name = form.cleaned_data['user_name']
        review = Review()
        review.movie = movie
        review.user_name = user_name
        review.rating = rating
        review.comment = comment
        review.pub_date = datetime.datetime.now()
        review.save()
        return HttpResponseRedirect(reverse('movie_detail', args=(movie.id,)))
    return render(request, 'movie_detail.html', {'movie':movie, 'form': form})
