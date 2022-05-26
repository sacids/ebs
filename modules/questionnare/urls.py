from django.urls import path
from . import views

app_name = 'questionnare'

urlpatterns = [
    path("", views.surveys, name="index"),
    path("introduction/", views.introduction, name="introduction"),
    path("questions/", views.questions, name="questions"),
    path('success/', views.success, name='success'),

    # filters
    path('get_countries/', views.get_countries, name='get_countries'),
]
