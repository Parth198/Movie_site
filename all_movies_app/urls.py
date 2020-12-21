from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('sort_by_name/', views.sort_by_name, name='sort_by_name'),
    path('sort_by_popularity/', views.sort_by_popularity, name='sort_by_popularity'),
]