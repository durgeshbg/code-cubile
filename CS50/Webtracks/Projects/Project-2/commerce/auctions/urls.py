from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("categories", views.categories, name="categories"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("add_watchlist/<int:id>", views.add_watchlist, name="add_watchlist"),
    path("remove_watchlist/<int:id>", views.remove_watchlist, name="remove_watchlist"),
    path("create_listing", views.create_listing, name="create_listing"),
    path("listings/<int:n>", views.listings, name="listings"),
    path("comment", views.comment, name="comment"),
    path("deactivate/<int:id>", views.deactivate, name="deactivate")
]
