from django.urls import path
from . import views
from .views import (get_countries, success)

app_name = 'questionnare'
urlpatterns = [
    path("", views.QuestionnareCreateView.as_view(), name="questionnare"),
    path('success/', success, name='success'),

    #filters
    path('get_countries/', get_countries, name='get_countries'),
]
