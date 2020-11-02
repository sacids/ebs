from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'respondents'
urlpatterns = [
    path("lists", views.RespondentsListView.as_view(), name="lists"),
    path('<int:pk>', views.RespondentDetailView.as_view(), name='details'),
    path('delete/<int:pk>', views.RespondentDeleteView.as_view(), name='delete'),
]
