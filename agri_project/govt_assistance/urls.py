from django.urls import path
from . import views

urlpatterns = [
    path('apply/', views.apply_for_assistance, name='apply_for_assistance'),
    path('list/', views.view_applications, name='view_applications'),
]
