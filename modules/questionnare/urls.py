from django.urls import path
from . import views

app_name = 'questionnare'

urlpatterns = [
    path("", views.surveys, name="index"),
    path("introduction/<int:pk>/", views.introduction, name="introduction"),
    path("sections/<int:pk>/", views.sections, name="sections"),
    path('success/', views.success, name='success'),

    # filters
    path('get_countries/', views.get_countries, name='get_countries'),
]
