from urllib import request
from django.urls import path

from . import views

urlpatterns = [
    path("", views.hello_rekruto, name="hello"),
]
