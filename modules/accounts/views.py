from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from .utils import *
from ..profiles.models import Profiles

# Create your views here.

# change language


def change_language(request, **kwargs):
    # language code
    language_code = kwargs['lang']

    language = "en-us"  # default language

    # check language code
    if language_code == 'en_us':
        language = "en-us"
    elif language_code == 'fr':
        language = "fr"
    elif language_code == 'pt':
        language = "pt"
    elif language_code == 'ar':
        language = "ar"    

    # response
    response = HttpResponseRedirect('/')
    if language:
        redirect_path = '/'

        translation.activate(language)
        response = HttpResponseRedirect(redirect_path)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


# login
def loginPage(request):
    print("current language => " + translation.get_language())

    if request.user.is_authenticated:
        if(request.user.profiles.first_login == 1):
            # redirect to change password
            return redirect('/change_password')
        else:
            # redirect
            if(is_respondent(request.user)):
                return redirect('/questionnare')
            elif(is_reviewer(request.user)):
                return redirect('/responses/surveys/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            # user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                if(user.profiles.first_login == 1):
                    # redirect to change password
                    return redirect('/change_password')
                else:
                    # redirect
                    if(is_respondent(user)):
                        return redirect('/questionnare')
                    elif(is_reviewer(user)):
                        return redirect('/responses/surveys/')
            else:
                messages.error(request, _(
                    'Username OR Password is incorectly'))

        context = {}
        return render(request, 'accounts/login.html', context)


# change password
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!

            #update profile
            profile = Profiles.objects.get(user=user.id)
            profile.first_login = 2
            profile.save()

            messages.success(request, 'Password successfully updated!')
            return redirect('/login')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})


# logout
def logoutUser(request):
    logout(request)
    messages.error(request, _('Log out successfully'))
    return redirect('/login')
