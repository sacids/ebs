from django.urls import path
from . import views
from .views import *

app_name = 'questionnare'
urlpatterns = [
    path("", views.QuestionListView.as_view(), name="questionnare"),
]
