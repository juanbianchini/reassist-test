from django.urls import path
from . import views

urlpatterns = [
    path('individuals/', views.chatbot_individuals, name='chatbot_individuals'),
    path('assistances/', views.chatbot_assistances, name='chatbot_assistances'),
]



