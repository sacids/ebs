from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.utils import translation
from django.utils.translation import ugettext_lazy as _
from .utils import *

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

                # redirect
                if(is_respondent(user)):
                    return redirect('/questionnare')
                elif(is_reviewer(user)):
                    return redirect('/responses/countries/')
            else:
                messages.error(request, _('Username OR Password is incorectly'))

        context = {}
        return render(request, 'accounts/login.html', context)


# logout
def logoutUser(request):
    logout(request)
    messages.error(request, _('Log out successfully'))
    return redirect('/login')
