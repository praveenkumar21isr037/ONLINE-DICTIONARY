from django.urls import path
from . import views

urlpatterns = [
    path('', views.alphabet_index, name='alphabet_index'),
    path('<str:letter>/', views.words_starting_with, name='words_starting_with'),
]
