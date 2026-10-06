from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.urls import reverse
from django.template.defaultfilters import slugify, slice_filter


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': 'Биография Анджелины Джоли', 'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулия Робертс', 'is_published': True},
]



def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, "volleyball_players/index.html", context=data)


def about(request):
    data = {'title': 'О сайте'}
    return render(request, "volleyball_players/about.html", data)


def categories(request, cat_id):
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>id: {cat_id}</p>")


def categories_by_slug(request, cat_slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Статьи по категориям</h1><p>slug: {cat_slug}</p>")


def archive(request, year):
    if year > 2025:
        # raise Http404()
        url = reverse("cats_slug", args=("music",))
        return redirect(url)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
