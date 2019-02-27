from django.urls import path

from . import views

urlpatterns = [
    path('get_capabilities/', views.get_capabilities, name='get_capabilities'),
    path('get_services/', views.get_services, name='get_services')
]
