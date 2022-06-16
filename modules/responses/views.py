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
from django.contrib import messages
from datetime import datetime
from datetime import timedelta
from django.shortcuts import get_object_or_404


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
    survey_id = request.GET.get('sv_id', -1)
    survey = get_object_or_404(Survey.objects.all(), pk=survey_id)

    countries = Country.objects.all().order_by('id')

    context = {
        "survey": survey,
        "countries": countries
    }

    # render view
    return render(request, "lists.html", context)


@login_required(login_url='/login')
def questions(request):
    # survey
    survey_id = request.GET.get('sv_id', -1)
    survey = get_object_or_404(Survey.objects.all(), pk=survey_id)

    #section_id
    section_id = request.GET.get('sc_id', -1)
    country_id = request.GET.get('c_id')

    if section_id == -1:
        section = Section.objects.filter(survey_id=survey_id).order_by("code")[0]
    else:
        section = get_object_or_404(Section.objects.all(), pk=section_id)

    #prev and next section
    prev_section_id = prev_section(survey.id, section.id)
    next_section_id = next_section(survey.id, section.id)    

    # country
    country = Country.objects.get(pk=country_id)

    # profile
    try:
        profile = Profiles.objects.get(country_id=country.id)
        user = profile.user
    except:
        profile = []
        user = []
        pass  

    #questions
    questions = QuestionList.objects.filter(section_id = section.id).order_by("code", "sort_order")  

     # context
    context = {
        "survey": survey,
        "section_id": section_id,
        "section": section,
        "prev_section_id": prev_section_id,
        "next_section_id": next_section_id,
        "profile": profile,
        "user": user,
        "country": country,
        "questions": questions
    } 

    # render view
    return render(request, "questions.html", context)


#calculate next section
def next_section(survey_id, section_id):
    #last id
    last_section = Section.objects.filter(survey_id = survey_id).order_by('-code')[:1]

    print(last_section)

    #section
    section = Section.objects.get(pk=section_id)

    if section.code < last_section[0].code:
        next_code = section.code + 1
        section = Section.objects.filter(survey_id=survey_id, code = next_code).first()
        return section.id

#calculate previous section
def prev_section(survey_id, section_id):
    #first id
    first_section = Section.objects.filter(survey_id = survey_id).order_by('code')[:1]

    print(first_section)

    #section
    section = Section.objects.get(pk=section_id)

    if section.code > first_section[0].code:
        prev_code = section.code - 1
        section = Section.objects.filter(survey_id=survey_id, code = prev_code).first()
        return section.id


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
