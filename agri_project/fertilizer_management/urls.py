from django.urls import path
from . import views

urlpatterns = [
    path('', views.fertilizer_list, name='fertilizer_list'),
]
