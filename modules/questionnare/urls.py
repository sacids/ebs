from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'questionnare'
urlpatterns = [
    path("", views.default, name="index"),
    path("questions/", views.QuestionnareCreateView.as_view(), name="questions"),
    path('success/', views.success, name='success'),

    # filters
    path('get_countries/', views.get_countries, name='get_countries'),
    path('show_question/', views.show_question, name='show_question'),

    # admin
    path('respondents/', views.CountryList.as_view(), name='country_list'),
]
