from django.urls import path
from django.conf.urls import url

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
    path("api_post_answers/", views.api_post_answers, name="api_post_answers"),
    path('success/', views.success, name='success'),

    # filters
    path('get_countries/', views.get_countries, name='get_countries'),
    path('show_question/', views.show_question, name='show_question'),

    # admin
    path('respondents/', views.CountryList.as_view(), name='country_list'),

    # error pages
    path('generate_pdf', views.pdf_section_one, name="generate_pdf")

]
