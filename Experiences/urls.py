from django.urls import path

from . import views

urlpatterns = [
    path('get_experiences/', views.get_experiences, name='get_experiences')
]
