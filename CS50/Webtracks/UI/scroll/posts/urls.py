from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("start=<int:start>&end=<int:end>",views.posts, name="posts"),
]