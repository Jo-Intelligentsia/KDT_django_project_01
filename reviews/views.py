from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm
# Create your views here.

def index(request):
    reviews = Review.objects.all()
    context = {
        'reviews':reviews,
    }
    return render(request, 'reviews/index.html',context)

def detail(request, review_pk):
    review = Review.objects.get(pk=review_pk)

    context = {
        'review' : review,
    }
    return render(request, 'reviews/detail.html',context)


def create(request):
    if request.method == "POST":
        pass
    else:
        form = ReviewForm()
    context ={
        'form' : form,
    }
    return render(request, 'reviews/create.html', context)

def update(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    if request.method == "POST":
        pass
    else:
        form = ReviewForm(instance=review)
    context = {
        'review' : review,
        'form' : form,
    }
    return render(request, 'reviews/update.html', context)

def delete(request, review_pk):
    review = Review.objects.get(pk=review_pk)
    review.delete()
    return redirect('reviews:index')