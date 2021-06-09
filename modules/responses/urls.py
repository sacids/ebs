from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'responses'
urlpatterns = [
    # admin
    path('surveys/', views.surveys, name='surveys'),
    path('countries/<int:survey_id>', views.countries, name='countries'),

    #survey 1
    path("section_one/<int:country_id>", views.section_one, name="section_one"),
    path("section_two/<int:country_id>", views.section_two, name="section_two"),
    path("section_three/<int:country_id>", views.section_three, name="section_three"),
    path("section_four/<int:country_id>", views.section_four, name="section_four"),
    path("section_five/<int:country_id>", views.section_five, name="section_five"),
    path("section_six/<int:country_id>", views.section_six, name="section_six"),

    #survey 2
    path("general_info/<int:country_id>", views.general_info, name="general_info"),
    path("metrics/<int:country_id>", views.metrics, name="metrics"),
    path("preference/<int:country_id>", views.preference, name="preference"),
    path("information/<int:country_id>", views.information, name="information"),


    # alerts
    path('send_incomplete_submission_alert/<int:survey_id>/<int:country_id>',
         views.send_incomplete_submission_alert, name="send_incomplete_submission_alert"),

    #export xls and csv
    path("export_csv/<int:survey_id>/<int:country_id>", views.export_csv, name="export_csv"),
    path("export_xls/<int:survey_id>/<int:country_id>", views.export_xls, name="export_xls"),

]
