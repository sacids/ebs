from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name = 'accounts'
urlpatterns = [
    path("", views.loginPage, name="login"),
    path('change_language/<str:lang>', views.change_language, name='change_language'),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutUser, name="logout"),
]
