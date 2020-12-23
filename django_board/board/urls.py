from django.urls import path
from . import views

app_name = "board"

urlpatterns = [
    path("", views.index, name="index"),
    path("board/", views.board, name="board"),
    path("board/new_post/", views.new_post, name="new_post"),
    path("board/<int:pk>/update/", views.update_post, name="update"),
    path("board/<int:pk>/remove/", views.remove_post, name="remove"),
    path("board/<int:pk>", views.posting, name="posting"),
]
