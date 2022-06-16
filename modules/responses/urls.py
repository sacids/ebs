from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'responses'
urlpatterns = [
    # admin
    path('surveys/', views.surveys, name='surveys'),
    path('countries/', views.countries, name='countries'),
    path('questions/', views.questions, name='questions'),

    # alerts
    path('send_incomplete_submission_alert/<int:survey_id>/<int:country_id>',
         views.send_incomplete_submission_alert, name="send_incomplete_submission_alert"),

    #export xls and csv
    path("export_csv/<int:survey_id>/<int:country_id>", views.export_csv, name="export_csv"),
    path("export_xls/<int:survey_id>/<int:country_id>", views.export_xls, name="export_xls"),

]
