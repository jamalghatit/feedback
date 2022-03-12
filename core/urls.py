from django.urls import path

from core.views import feedback_view, sobre_view

urlpatterns = [
    path('', feedback_view, name='feedback'),
    path('sobre', sobre_view, name='sobre')
]
