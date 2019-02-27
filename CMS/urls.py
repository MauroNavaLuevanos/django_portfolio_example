from django.urls import path

from . import views

urlpatterns = [
    path('get_general', views.get_general, name="get_general")
]
