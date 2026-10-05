from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.urls import reverse


menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]


class Myclass:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_info(self):
        return self.first_name + " " + self.last_name


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'float': 28.56,
        'lst': [1, 2, 'abc', True],
        'set': {1, 2, 3, 2, 5},
        'dict': {'key1': 'value1', 'key2': 'value2'},
        'obj': Myclass('Марь', 'Ивановна')
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
