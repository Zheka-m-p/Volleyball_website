from django.shortcuts import redirect, render
from django.http import HttpResponse, Http404, HttpResponseNotFound
from django.urls import reverse
from django.template.defaultfilters import slugify, slice_filter


menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Дмитрий Мусэрский',
     'content': 'Центральный блокирующий, рост 218 см. Олимпийский чемпион 2012.',
     'is_published': True, 'category': 'Блокирующие'},
    
    {'id': 2, 'title': 'Максим Михайлов',
     'content': 'Диагональный, капитан сборной России. Олимпийский чемпион 2012.',
     'is_published': True, 'category': 'Диагональные'},
    
    {'id': 3, 'title': 'Сергей Тетюхин',
     'content': 'Доигровщик, легенда российского волейбола. Четырёхкратный призёр Олимпиад.',
     'is_published': True, 'category': 'Доигровщики'},
]


def index(request):
    data = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
    }
    return render(request, "volleyball_players/index.html", context=data)


def about(request):
    data = {'title': 'О сайте', 'menu': menu}
    return render(request, "volleyball_players/about.html", data)


def add_page(request):
    return HttpResponse(f'Добавление статьи')


def contact(request):
    return HttpResponse('Обратная связь')


def login(request):
    return HttpResponse('Авторизация')


def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id = {post_id}')


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
