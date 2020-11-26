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
from .models import *
from .utils import render_to_pdf
from .forms import RespondentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ..notification.views import send_notification


@login_required
def default(request):
    if request.user.is_authenticated:
        # check last section and redirect to right section

        # redirect
        return redirect('/section_one/')


# section one
def section_one(request):
    # section_id
    section_id = 1

   # questions
    questions = QuestionList.objects.filter(section_id=1)

    # context
    context = {
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
                # todo: check for attachment and upload
                # print(request.FILES)
                # if request.FILES is not None:
                #     if request.FILES['attachments[73]'] is not None:
                #         print(request.FILES['attachments[73]'])
                # # if len(request.FILES['attachments['+ str(question.id) +']']) != 0:
                # #     print('here')

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_two')  # redirect to section two

    # render view
    return render(request, "questionnare/section_one.html", context)


# print section one
def pdf_section_one(request):
   # questions
    questions = QuestionList.objects.filter(section_id=1)

    # context
    context = {
        "questions": questions,
        "user": request.user
    }
    pdf = render_to_pdf('questionnare/pdf/pdf_section_one.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Section_One_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")


# section two
def section_two(request):
    # section_id
    section_id = 2

   # questions
    questions = QuestionList.objects.filter(section_id=2)

    # context
    context = {
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
                # todo: check for attachment and upload

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_three')  # redirect to section three

    # render view
    return render(request, "questionnare/section_two.html", context)


# section three
def section_three(request):
    # section
    section_id = 3

    # questions
    questions = QuestionList.objects.filter(section_id=3)

    # context
    context = {
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
                # todo: check for attachment and upload

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_four')  # redirect to section four

    # render view
    return render(request, "questionnare/section_three.html", context)


# section four
def section_four(request):
    # section
    section_id = 4

    # questions
    questions = QuestionList.objects.filter(section_id=4)

    # context
    context = {
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
                # todo: check for attachment and upload

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_five')  # redirect to section five

    # render view
    return render(request, "questionnare/section_four.html", context)


# section five
def section_five(request):
    # section
    section_id = 5

    # questions
    questions = QuestionList.objects.filter(section_id=5)

    # context
    context = {
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
                # todo: check for attachment and upload

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_six')  # redirect to section six

    # render view
    return render(request, "questionnare/section_five.html", context)


# section six
def section_six(request):
    # section
    section_id = 6

    # questions
    questions = QuestionList.objects.filter(section_id=6)

    # context
    context = {
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
                # todo: check for attachment and upload

                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                              'question_id': question.id, 'answer': answer, 'remarks': remarks},)

        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            # todo validate
            required_questions = QuestionList.objects.filter(
                required='YES').order_by('sort_order', 'code')

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
                # country
                country = Country.objects.get(
                    pk=request.user.profiles.country_id)

                # send message
                subject = 'Submission Alert: Situation analysis of EBS implementation in Africa'

                message = '<p>Dear XXX</p>'
                message += '<p>Data for ' + country.name + \
                    ' has been Submitted.</p>'
                message += '<p>For review and approval please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

                # send email notification
                send_notification(subject, message, from_email="chris@ecsahc.org",
                                  to_email=['chris@ecsahc.org', 'werew@ecsahc.org', 'eric.beda@sacids.org'])

                # redirect to success
                return redirect('/success')

    # render view
    return render(request, "questionnare/section_six.html", context)


def success(request):
    return render(None, "questionnare/success.html", {})


class CountryList(generic.ListView):
    model = Country
    context_object_name = 'countries'
    template_name = "manage/countries.html"

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


class ResponsesList(generic.ListView):
    model = QuestionList
    context_object_name = 'questions'
    template_name = "manage/country_response.html"

    def get_context_data(self, **kwargs):
        context = super(ResponsesList, self).get_context_data(**kwargs)
        country_id = self.kwargs['country_id']
        # country
        country = Country.objects.get(pk=country_id)
        context['country'] = country

        # profile
        try:
            profile = Profiles.objects.get(country_id=country_id)
            context['profile'] = profile
        except:
            context['profile'] = []
            pass

        return context


def send_incomplete_submission_alert(request, **kwargs):
    # check for incomplete submission
    try:
        country = Country.objects.get(pk=kwargs['country_id'])

        if(country.status == 'NO'):
            subject = 'Incomplete Submission Alert: Situation analysis of EBS implementation in Africa'

            message = '<p>Dear' + request.user.get_full_name + ', </p>'
            message += '<p>Data for ' + country.name + \
                ' are incomplete, please find sometime to complete the form.</p>'
            message += '<p>To continue where you left off  please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

            # send email notification
            send_notification(subject, message, from_email="chris@ecsahc.org",
                              to_email=[request.user.email])

            # message
            messages.add_message(
                request, messages.SUCCESS, 'Email notification sent')
    except:
        pass

    # redirect
    return redirect('/respondents')


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
