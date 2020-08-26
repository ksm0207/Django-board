from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("board/", views.board, name="board"),
    path("board/new_post/", views.new_post, name="new_post"),
    path("board/<int:pk>", views.posting, name="posting"),
]
