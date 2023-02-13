from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("durgesh/", views.durgesh, name="durgesh"),
    path("<str:name>", views.greet, name="greet")
]
