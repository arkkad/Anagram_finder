from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'load', views.AnagramDict.as_view()),
    path(r'get', views.AnagramShowView.as_view()),
    path(r'clear', views.AnagramDict.as_view())
]
