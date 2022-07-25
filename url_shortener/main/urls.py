from django.urls import path
from . import views

urlpatterns = [
    path(route="", view=views.home, name="home"),
    path(route="<str:shortened_part>", view=views.redirect_url, name="redirect_url"),
]