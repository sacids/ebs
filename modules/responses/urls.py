from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'responses'
urlpatterns = [
    # admin
    path('countries/', views.CountryList.as_view(), name='countries'),
    path("section_one/<int:country_id>", views.section_one, name="section_one"),
    path("section_two/<int:country_id>", views.section_two, name="section_two"),
    path("section_three/<int:country_id>", views.section_three, name="section_three"),
    path("section_four/<int:country_id>", views.section_four, name="section_four"),
    path("section_five/<int:country_id>", views.section_five, name="section_five"),
    path("section_six/<int:country_id>", views.section_six, name="section_six"),

    # alerts
    path('send_incomplete_submission_alert/<int:country_id>',
         views.send_incomplete_submission_alert, name="send_incomplete_submission_alert"),

    #export xls
    path("export_xls/<int:country_id>", views.export_xls, name="export_xls"),

]
