from django.contrib import admin
from music import views
import snapify.settings as settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path("home/", views.album_page),
]
