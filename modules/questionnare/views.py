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
def default(request):
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
        return render(request, "questionnare/survey.html", context)

# =================================================================
# EBS Survey
#================================================================#


@login_required(login_url='/login')
def section_one(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section_id
    section_id = 1

    # section
    section = Section.objects.get(pk=section_id)

   # questions
    questions = QuestionList.objects.filter(section_id=1)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        # first save country survey status
        try:
            country_survey = CountrySurvey.objects.get(
                country_id=request.user.profiles.country_id, survey_id=1)
            # do nothing
        except:
            # save new country survey
            country_survey = CountrySurvey()
            country_survey.country_id = request.user.profiles.country_id
            country_survey.survey_id = 1
            country_survey.status = "INCOMPLETE"
            country_survey.save()

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        # redirect
        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # redirect to section two
            return redirect('/questionnare/section_two')

    # render view
    return render(request, "questionnare/section_one.html", context)


# section two
@login_required(login_url='/login')
def section_two(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section_id
    section_id = 2

    # section
    section = Section.objects.get(pk=section_id)

   # questions
    questions = QuestionList.objects.filter(section_id=2)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # redirect to section three
            return redirect('/questionnare/section_three')

    # render view
    return render(request, "questionnare/section_two.html", context)


# section three
@login_required(login_url='/login')
def section_three(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section
    section_id = 3

    # section
    section = Section.objects.get(pk=section_id)

    # questions
    questions = QuestionList.objects.filter(section_id=3)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # redirect to section four
            return redirect('/questionnare/section_four')

    # render view
    return render(request, "questionnare/section_three.html", context)


# section four
@login_required(login_url='/login')
def section_four(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section
    section_id = 4

    # section
    section = Section.objects.get(pk=section_id)

    # questions
    questions = QuestionList.objects.filter(section_id=4)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
       # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # redirect to section five
            return redirect('/questionnare/section_five')

    # render view
    return render(request, "questionnare/section_four.html", context)


# section five
@login_required(login_url='/login')
def section_five(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section
    section_id = 5

    # section
    section = Section.objects.get(pk=section_id)

    # questions
    questions = QuestionList.objects.filter(section_id=5)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # redirect to section six
            return redirect('/questionnare/section_six')

    # render view
    return render(request, "questionnare/section_five.html", context)


# section six
@login_required(login_url='/login')
def section_six(request):
    # survey
    survey = Survey.objects.get(pk=1)

    # section
    section_id = 6

    # section
    section = Section.objects.get(pk=section_id)

    # questions
    questions = QuestionList.objects.filter(section_id=6)

    # context
    context = {
        "survey": survey,
        "section": section,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # validate questions
            required_questions = QuestionList.objects.filter(
                (Q(section=1) | Q(section=2) | Q(section=3) | Q(section=4) | Q(section=5) | Q(section=6)) & Q(required='YES')).order_by('sort_order', 'code')

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
    return render(request, "questionnare/section_six.html", context)


@login_required(login_url='/login')
def success(request):

    # country
    country = Country.objects.get(pk=request.user.profiles.country_id)

    return render(None, "questionnare/success.html", {})


# =================================================================
# Preliminary Survey
#================================================================#
# section information
@login_required(login_url='/login')
def welcome(request):
    # survey
    survey = Survey.objects.get(pk=2)

    context = {
        "survey": survey,
    }

    # render view
    return render(request, "questionnare/p_welcome.html", context)


# general information
@login_required(login_url='/login')
def general_info(request):
    # survey
    survey = Survey.objects.get(pk=2)

    # metrics
    section_id = 10

    # section
    section = Section.objects.get(pk=section_id)

    # country
    country = Country.objects.get(pk=request.user.profiles.country_id)

    context = {
        "survey": survey,
        "section": section,
        "country": country
    }

    # post data
    if request.method == "POST":
        # first save country survey status
        try:
            country_survey = CountrySurvey.objects.get(
                country=request.user.profiles.country_id, survey=2)
            # do nothing
        except:
            # save new country survey
            country_survey = CountrySurvey()
            country_survey.country_id = request.user.profiles.country_id
            country_survey.survey_id = 2
            country_survey.status = "INCOMPLETE"
            country_survey.save()

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        # redirect
        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/questionnare/metrics')

    # render view
    return render(request, "questionnare/p_general_info.html", context)

# section one


@login_required(login_url='/login')
def metrics(request):
    # survey
    survey = Survey.objects.get(pk=2)

    # metrics
    section_id = 7

    # section
    section = Section.objects.get(pk=section_id)

    # context
    context = {
        "survey": survey,
        "section": section
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        # redirect
        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/questionnare/preference')

    # render view
    return render(request, "questionnare/p_metrics.html", context)


@login_required(login_url='/login')
def preference(request):
    # survey
    survey = Survey.objects.get(pk=2)

    # section_id
    section_id = 8

    # section
    section = Section.objects.get(pk=section_id)

    # context
    context = {
        "survey": survey,
        "section": section
    }

    # post data
    if request.method == "POST":
        # get answers
        answer446 = request.POST.get('answer[446]')
        answer450 = request.POST.get('answer[450]')
        answer454 = request.POST.get('answer[454]')
        answer458 = request.POST.get('answer[458]')
        answer462 = request.POST.get('answer[462]')
        answer466 = request.POST.get('answer[466]')
        answer470 = request.POST.get('answer[470]')

        if ((answer446 == answer450) or (answer446 == answer454) or (answer446 == answer458) or (answer446 == answer462) or (answer446 == answer466) or (answer446 == answer470)):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.1.i should not be the same with other answers.')

        elif ((answer450 == answer454) or (answer450 == answer458) or (answer450 == answer462) or (answer450 == answer466) or (answer450 == answer470)):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.2.i should not be the same with other answers.')

        elif((answer454 == answer458) or (answer454 == answer462) or (answer454 == answer466) or (answer454 == answer470)):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.3.i should not be the same with other answers.')

        elif ((answer458 == answer462) or (answer458 == answer466) or (answer458 == answer470)):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.4.i should not be the same with other answers.')

        elif ((answer462 == answer466) or (answer462 == answer470)):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.5.i should not be the same with other answers.')
                
        elif (answer466 == answer470):
            messages.add_message(
                request, messages.ERROR, 'Answer for question 2.6.i should not be the same with 2.7.i')
        else:
            # query questions
            questions = QuestionList.objects.filter(
                section_id=section_id).order_by('sort_order', 'code')

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
                            newAttachment.save()  # save

            # redirect
            if(request.POST.get('post_exit')):
                return redirect('/questionnare/success')  # return to exit page
            elif(request.POST.get('post_next')):
                return redirect('/questionnare/information')

    # render view
    return render(request, "questionnare/p_preference.html", context)


@login_required(login_url='/login')
def information(request):
    # survey
    survey = Survey.objects.get(pk=2)

    # section_id
    section_id = 9

    # section
    section = Section.objects.get(pk=section_id)

    # context
    context = {
        "survey": survey,
        "section": section
    }

    # post data
    if request.method == "POST":
        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

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
                        newAttachment.save()  # save

        # redirect
        if(request.POST.get('post_exit')):
            return redirect('/questionnare/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # validate questions
            required_questions = QuestionList.objects.filter(
                (Q(section=7) | Q(section=7) | Q(section=9)) & Q(required='YES')).order_by('sort_order', 'code')

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
                    country=request.user.profiles.country_id, survey=2)
                country_survey.status = "COMPLETE"
                country_survey.save()

                # country
                country = Country.objects.get(
                    pk=request.user.profiles.country_id)

                # send message
                subject = 'Submission Alert: Preliminary needs identification form'

                message = '<p>Dear Reviewers,</p>'
                message += '<p>Data for <b>' + country.title + '</b>' + \
                    ' has been Submitted.</p>'
                message += '<p>For review and approval please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

                # send email notification
                # send_notification(subject, message, from_email=request.user.email,
                # to_email=['chris@ecsahc.org', 'werew@ecsahc.org', 'eric.beda@sacids.org'])

                # redirect to success
                return redirect('/questionnare/success')

    # render view
    return render(request, "questionnare/p_information.html", context)


# =================================================================
# Others callback functions
#================================================================#
def get_countries(request):
    if request.method == 'GET':
        council_id = request.GET.get('council_id')
        countries = Country.objects.filter(council_id=council_id)

        # return response.
        return render(None, 'questionnare/countries.html', {'countries': countries})


def show_question(request):
    if request.method == 'GET':
        qn_id = request.GET.get('question_id')
        question = Question.objects.get(pk=qn_id)

        # return response
        return JsonResponse({'id': question.id, 'placeholder': question.placeholder})
