from django.urls import path
from . import views

urlpatterns = [
    path('ask/', views.ask_question, name='ask_question'),
    path('forum/', views.view_forum, name='view_forum'),
]
