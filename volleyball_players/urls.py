from django.urls import path, register_converter, re_path
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path("", views.index, name='home'),
    path('about/', views.about, name='about'),
    path("categories/<int:cat_id>/", views.categories, name='cats_id'),
    path("categories/<slug:cat_slug>/", views.categories_by_slug, name='cats_slug'),

    path("archive/<year4:year>/", views.archive, name='archive'),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', views.archive), # если регулярка

]
