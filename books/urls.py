from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('books', views.books, name='books'),
    path('book/<str:pk>/',views.book,name='book_page'),
]
