from django.urls import path
from . import views

app_name = 'questionnare'

urlpatterns = [
    path("", views.default, name="index"),
    path("section_one/", views.section_one, name="section_one"),
    path("section_two/", views.section_two, name="section_two"),
    path("section_three/", views.section_three, name="section_three"),
    path("section_four/", views.section_four, name="section_four"),
    path("section_five/", views.section_five, name="section_five"),
    path("section_six/", views.section_six, name="section_six"),
    path('success/', views.success, name='success'),

    #new survey
    path("welcome/", views.welcome, name="welcome_note"),
    path("general_info/", views.general_info, name="general_info"),
    path("metrics/", views.metrics, name="metrics"),
    path("preference/", views.preference, name="preference"),
    path("information/", views.information, name="information"),

    # filters
    path('get_countries/', views.get_countries, name='get_countries'),
    path('show_question/', views.show_question, name='show_question'),
]
