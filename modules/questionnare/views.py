import json

from django.core.mail import message
from modules.notification.views import send_notification
from modules.profiles.models import Profiles
from modules.dashboard.views import dashboard
from modules.questionnare.forms import RespondentForm
from django.db.models.query import Prefetch
from django.http import request, HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import generic
from ..dashboard import *
from django.contrib import messages
from django.db.models import Q
from .models import *
from .utils import render_to_pdf
from .forms import RespondentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ..notification.views import send_notification


@login_required(login_url='/login')
def surveys(request):
    if request.user.is_authenticated:

        # get all survey
        surveys = Survey.objects.all().order_by('id')

        # country
        country = Country.objects.get(pk=request.user.profiles.country_id)

        context = {
            'country': country,
            'surveys': surveys
        }

        # render view
        return render(request, "questionnare/surveys.html", context)


@login_required(login_url='/login')
def introduction(request, **kwargs):
    # survey
    survey_id = kwargs['pk']
    survey = Survey.objects.get(pk=survey_id)

    context = {
        "survey": survey,
    }

    # render view
    return render(request, "questionnare/introduction.html", context)

@login_required(login_url='/login')
def sections(request, **kwargs):
    # survey
    survey_id = kwargs['pk']
    survey = Survey.objects.get(pk=survey_id) 

    sections = Section.objects.filter(survey_id=survey_id).order_by("code")

    # context
    context = {
        "survey": survey,
        "sections": sections
    }  

    # post data
    if request.method == "POST":
        for section in sections:
            questions = QuestionList.objects.filter(
                section_id=section.id).order_by('sort_order', 'code')

            for question in questions:
                answer = request.POST.get('answer[' + str(question.id) + ']')
                remarks = request.POST.get('remarks[' + str(question.id) + ']')

                if answer is not None:
                    # save or update
                    obj, created = AnsBank.objects.update_or_create(
                        question_id=question.id, country_id=request.user.profiles.country_id,
                        defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                                'question_id': question.id, 'answer': answer, 'remarks': remarks},)

                    # check for attachment and upload
                    if request.FILES is not None:
                        attachment_files = request.FILES.getlist(
                            'attachments[' + str(question.id) + ']')
                        for f in attachment_files:
                            newAttachment = Attachments()
                            newAttachment.ansbank_id = obj.id
                            newAttachment.uploads = f
                            newAttachment.save()

            if(request.POST.get('post_exit')):
                return redirect('/questionnare/success')
            elif(request.POST.get('post_next')):
                # validate questions
                required_questions = QuestionList.objects.filter((Q(section=section.id)) & Q(required='YES')).order_by('sort_order', 'code')

                j = 0
                for req_qn in required_questions:
                    # query in answer bank
                    try:
                        ans_bank = AnsBank.objects.get(
                            question_id=req_qn.id, country_id=request.user.profiles.country_id)
                    except:
                        messages.add_message(
                            request, messages.ERROR, 'Question number ' + req_qn.code + ' required')
                        j = j + 1

                # check if there no required question
                if(j == 0):
                    # change country survey survey
                    country_survey = CountrySurvey.objects.get(
                        country=request.user.profiles.country_id, survey=1)
                    country_survey.status = "COMPLETE"
                    country_survey.save()

                    # country
                    country = Country.objects.get(
                        pk=request.user.profiles.country_id)

                    # send message
                    subject = 'Submission Alert: Situation analysis of EBS implementation in Africa'

                    message = '<p>Dear Reviewers,</p>'
                    message += '<p>Data for <b>' + country.title + '</b>' + \
                        ' has been Submitted.</p>'
                    message += '<p>For review and approval please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

                    # send email notification
                    send_notification(subject, message, from_email=request.user.email,
                                    to_email=['renfrid.ngolongolo@sacids.org', 'eric.beda@sacids.org'])

                    # redirect to success
                    return redirect('/questionnare/success')

    # render view
    return render(request, "questionnare/sections.html", context)


@login_required(login_url='/login')
def success(request):

    # country
    country = Country.objects.get(pk=request.user.profiles.country_id)

    return render(None, "questionnare/success.html", {})



# =================================================================
# Others callback functions
#================================================================#
def get_countries(request):
    if request.method == 'GET':
        council_id = request.GET.get('council_id')
        countries = Country.objects.filter(council_id=council_id)

        # return response.
        return render(None, 'questionnare/countries.html', {'countries': countries})
