from django.urls import path

from . import views

urlpatterns = [
    path('get_social/', views.get_social, name='get_social')
]
