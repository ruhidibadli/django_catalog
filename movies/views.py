from django.shortcuts import render,get_object_or_404
from .models import Movie

# Create your views here.


def index(request):
    movies = Movie.objects.all() 

    contexts={
        "movies":movies
    }

    return render(request,"movies/list.html",contexts)

def detail(request,movies_id):
    movie = get_object_or_404(Movie, pk=movies_id)

    context={
        "movie":movie
    }

    return render(request,"movies/detail.html",context)

def search(request):
    return render(request,"movies/search.html")