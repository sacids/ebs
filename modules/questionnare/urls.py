from django.urls import path
from . import views
from .views import (default, get_countries, show_question, success)

app_name = 'questionnare'
urlpatterns = [
    path("", default, name="index"),
    path("questions/<int:pk>", views.QuestionnareCreateView.as_view(), name="questionnare"),
    path('success/', success, name='success'),

    # filters
    path('get_countries/', get_countries, name='get_countries'),
    path('show_question/', show_question, name='show_question'),
]
