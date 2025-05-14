from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_krishok, name='register_krishok'),
    path('search/', views.search_krishok, name='search_krishok'),
]
