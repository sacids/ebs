from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path("login/", views.loginPage, name="login"),
]