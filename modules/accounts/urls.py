from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path("", views.loginPage, name="login"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]
