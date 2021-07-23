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
# =====================================================
# SURVEYS
# =====================================================
# surveys
@login_required(login_url='/login')
def surveys(request):
    # get all survey
    surveys = Survey.objects.all().order_by('id')

    context = {
        'surveys': surveys
    }

    # render view
    return render(request, "surveys.html", context)


# countries
@login_required(login_url='/login')
def countries(request, **kwargs):
    # survey
    try:
        survey = Survey.objects.get(pk=kwargs['survey_id'])

        # countries
        countries = Country.objects.all().order_by('id')

        # context
        context = {
            "survey": survey,
            "countries": countries
        }
        # render view
        return render(request, "lists.html", context)
    except:
        pass


# ===========================================================
# SURVEY 1
# ===========================================================
# section one
@login_required(login_url='/login')
def section_one(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
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
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
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
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
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
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
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
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
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
    # survey
    survey = Survey.objects.get(pk=1)

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
        "survey": survey,
        "questions": questions,
        "country": country,
        "profile": profile,
        "user": profile.user
    }
    # render view
    return render(request, "sections/six.html", context)

# ===========================================================
# SURVEY 2
# ===========================================================
# general information


@login_required(login_url='/login')
def general_info(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=2)

    # section
    section = Section.objects.get(pk=10)

    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # attachments
    attachments = Attachments.objects.select_related(
        'ansbank', 'ansbank__question', 'ansbank__question__section').filter(ansbank__question__section__survey_id=2, ansbank__country_id=country.id)

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
        user = profile.user
    except:
        profile = []
        user = []
        pass

    # context
    context = {
        "survey": survey,
        "section": section,
        "country": country,
        "profile": profile,
        "user": user, 
        "attachments" : attachments
    }
    # render view
    return render(request, "sections/p_general_info.html", context)


# download attachments
# def download_attachments(request):


# metrics
@login_required(login_url='/login')
def metrics(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=2)

    # section
    section = Section.objects.get(pk=7)

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

    # context
    context = {
        "survey": survey,
        "section": section,
        "country": country,
        "profile": profile,
        "user": user
    }
    # render view
    return render(request, "sections/p_metrics.html", context)

# preference


@login_required(login_url='/login')
def preference(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=2)

    # section
    section = Section.objects.get(pk=8)

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

    # context
    context = {
        "survey": survey,
        "section": section,
        "country": country,
        "profile": profile,
        "user": user
    }
    # render view
    return render(request, "sections/p_preference.html", context)


# information
@login_required(login_url='/login')
def information(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=2)

    # section
    section = Section.objects.get(pk=9)

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

    # context
    context = {
        "survey": survey,
        "section": section,
        "country": country,
        "profile": profile,
        "user": user
    }
    # render view
    return render(request, "sections/p_information.html", context)

# ==========================================================
# MANAGEMENT CALLBACK FUNCTIONS
# ==========================================================
# send incomplete submission alert


@login_required(login_url='/login')
def send_incomplete_submission_alert(request, **kwargs):
    # check for incomplete submission
    try:
        # survey
        survey = Survey.objects.get(pk=kwargs['survey_id'])

        # country
        country = Country.objects.get(pk=kwargs['country_id'])

        # profile
        profile = Profiles.objects.get(country_id=country.id)

        if profile is not None:
            subject = 'Incomplete Submission Alert: ' + survey.title

            message = '<p>Dear <b>' + profile.user.last_name + '</b>, </p>'
            message += '<p>Data for <b>' + country.title + \
                '</b> are incomplete, please find sometime to complete the form.</p>'

            message += '<p>To continue where you left off please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

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


# export csv
def export_csv(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=kwargs['survey_id'])

    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + \
        country.title + '-Response.csv'

    writer = csv.writer(response)

    # column
    # deals with title row
    columns = ['Name of the Country', 'RCC', 'Respondent Name', ]

    # query questions
    questions = QuestionList.objects.select_related("section").filter(
        section__survey=survey.id).order_by('sections.id', 'code', 'sort_order')

    for qn in questions:
        columns.append(qn.code + ':' + qn.title)
        columns.append('Remarks')
        columns.append('Attachments')

    # write to row
    writer.writerow(columns)

    # profile
    profile = Profiles.objects.get(country_id=country.id)

    # deals with row 2
    column2 = [country.title, country.council.title,
               profile.user.get_full_name(), ]

    for qn in questions:
        # ansbank
        ansbank = AnsBank.objects.filter(
            question=qn.id, country=country.id).first()

        if ansbank:
            column2.append(ansbank.answer)
            column2.append(ansbank.remarks)

            # check for attachment
            attachments = Attachments.objects.filter(ansbank_id=ansbank.id)
            if attachments:
                column2.append('YES')
            else:
                column2.append('NO')
        else:
            column2.append('')
            column2.append('')
            column2.append('')

    # write to column2
    writer.writerow(column2)

    return response

# export csv


def export_xls(request, **kwargs):
    # survey
    survey = Survey.objects.get(pk=kwargs['survey_id'])

    # country
    country = Country.objects.get(pk=kwargs['country_id'])

    # # response
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=' + \
        country.title + '-Response.csv'

    #encoding
    response.write(u'\ufeff'.encode('utf8'))  
    writer = csv.writer(response)

    # profile
    profile = Profiles.objects.get(country_id=country.id)

    # first row
    writer.writerow([])
    writer.writerow(['Name of the Country', country.title])
    writer.writerow(
        ['Supporting Regional Cordinating Centre (RCC)', country.council.title])
    writer.writerow(['Respondent Name', profile.user.get_full_name()])
    writer.writerow(['Respondent Institution', profile.institution])
    writer.writerow(['Respondent designation', profile.designation])
    writer.writerow([])

    # column
    # deals with title row
    rows = ['Code', 'Question', 'Answer', 'Remarks', 'Attachments']

    # write to row
    writer.writerow(rows)

    # query questions
    questions = QuestionList.objects.select_related("section").filter(
        section__survey=survey.id).order_by('sections.code', 'sort_order', 'code')

    rows2 = []
    for qn in questions:
        # ansbank
        ansbank = AnsBank.objects.filter(
            question=qn.id, country=country.id).first()

        answer = ''
        remarks = ''
        arr_attachments = []
        if ansbank:
            answer = ansbank.answer
            remarks = ansbank.remarks

            # check for attachment
            attachments = Attachments.objects.filter(ansbank_id=ansbank.id)
            if attachments:
                for attachment in attachments:
                    arr_attachments.append(
                        str(attachment.uploads).rsplit('/', 1)[-1])

        str_attach = ''
        if arr_attachments is not None:
            str_attach = ', '.join(arr_attachments)
        # rows
        rows2 = [qn.code, qn.title, answer, remarks, str_attach]

        # write to column2
        writer.writerow(rows2)

    return response
