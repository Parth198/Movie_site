from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('searchbar/', views.searchbar, name='searchbar'),
    path('sort_by_name/<int:id>', views.sort_by_name, name='sort_by_name'),
    path('sort_by_popularity/<int:id>', views.sort_by_popularity, name='sort_by_popularity'),
]