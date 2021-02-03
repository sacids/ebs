import csv

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views import generic
from ..questionnare.models import *
from ..profiles.models import Profiles
from django.db.models.query import Prefetch
from ..notification.views import send_notification
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from datetime import datetime
from datetime import timedelta


# Create your views here.
class CountryList(LoginRequiredMixin, generic.ListView):
    login_url = '/login'
    redirect_field_name = 'redirect_to'
    model = Country
    context_object_name = 'countries'
    template_name = "lists.html"

    def get_context_data(self, **kwargs):
        context = super(CountryList, self).get_context_data(**kwargs)
        last_update = AnsBank.objects.all().order_by(
            'country', '-created_at').distinct('country').values()
        context['countries'] = Country.objects.all().order_by('title').values()

        tmp = [0] * 100
        for update in last_update:
            tmp[update['country_id']] = update['created_at']

        context['last_update'] = tmp
        return context


# section one
@login_required(login_url='/login')
def section_one(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
        user = profile.user
    except:
        profile = []
        user = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=1)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": user
    }

    # render view
    return render(request, "sections/one.html", context)


# section two
@login_required(login_url='/login')
def section_two(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
    except:
        profile = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=2)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/two.html", context)


# section three
@login_required(login_url='/login')
def section_three(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
    except:
        profile = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=3)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/three.html", context)


# section four
@login_required(login_url='/login')
def section_four(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
    except:
        profile = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=4)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/four.html", context)


# section five
@login_required(login_url='/login')
def section_five(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
    except:
        profile = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=5)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/five.html", context)


# section six
@login_required(login_url='/login')
def section_six(request, **kwargs):
    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
    except:
        profile = []
        pass

   # questions
    questions = QuestionList.objects.filter(section_id=6)

    # context
    context = {
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/six.html", context)


# send incomplete submission alert
@login_required(login_url='/login')
def send_incomplete_submission_alert(request, **kwargs):
    # check for incomplete submission
    try:
        country = Country.objects.get(pk=kwargs['country_id'])

        # profile
        profile = Profiles.objects.get(country_id=country.id)

        if profile is not None:
            if(country.status == 'NO'):
                subject = 'Incomplete Submission Alert: Situation analysis of EBS implementation in Africa'

                message = '<p>Dear <b>' + profile.user.last_name + '</b>, </p>'
                message += '<p>Data for <b>' + country.title + \
                    '</b> are incomplete, please find sometime to complete the form.</p>'

                message += '<p>To continue where you left off  please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

                # send email notification
                send_notification(subject, message, from_email="chris@ecsahc.org",
                                  to_email=[profile.user.email])

                # message
                messages.add_message(
                    request, messages.SUCCESS, 'Email notification sent')
    except:
        pass

    # redirect
    return redirect('/responses/countries')


# export xls
def export_xls(request, **kwargs):
    country = Country.objects.get(pk=kwargs['country_id'])

    # response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + \
        country.title + '-Response.csv'

    writer = csv.writer(response)
    writer.writerow(['Questions', 'Answers', 'Remarks'])

    # query questions
    questions = QuestionList.objects.order_by('section', 'code', 'sort_order')

    for qn in questions:
        # ansbank
        ansbank = AnsBank.objects.filter(
            question=qn.id, country=country.id).first()

        if ansbank:
            writer.writerow([qn.title, ansbank.answer, ansbank.remarks])
        else:
            writer.writerow([qn.title, '', ''])

    return response
