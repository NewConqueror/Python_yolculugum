from django.shortcuts import render
from . models import film
# Create your views here.

# fonksiyonları oluşturduk

def index(request):
    #return render(request, "movies/list.html")
    # içerik verdik ve movies diye film nesnelerini aldık
    movies = film.objects.all()

    context = {
        "movies": movies
    }
    # context = {
    #     "ad": "fatih yeni"
    # }
    return render(request, "movies/list.html",context)
# ders 26.11 movie list


def detail(request):
    return render(request, "movies/detail.html")

def search(request):
    return render(request, "movies/search.html")