from django.urls import path
from .views import about, inicio

urlpatterns = [
    path('', inicio, name="blog-index"),
    path('about/', about, name="blog-about"),
]

