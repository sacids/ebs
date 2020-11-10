import json
from modules.profiles.models import Profiles
from modules.dashboard.views import dashboard
from modules.questionnare.forms import RespondentForm
from django.db.models.query import Prefetch
from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import generic
from ..dashboard import *
from django.contrib import messages
from .models import *
from .forms import RespondentForm
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

# default


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

    # user
    #user_profile = Profiles.objects.get(user_id=request.user.id)
    #user_profile = get_object_or_404(Profiles, user_id=request.user.id)

    # context
    context = {
        #"user": user_profile,
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

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=request.user.id,
                    country_id=request.user.profile.country_id,
                    question_id=question.id,
                    answer=answer,
                    remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_two')  # redirect to section two

    # render view
    return render(request, "questionnare/section_one.html", context)


# section two
def section_two(request):
    # section_id
    section_id = 2

   # questions
    questions = QuestionList.objects.filter(section_id=2)

    # user
    user_profile = Profiles.objects.get(user_id=request.user.id)

    # context
    context = {
        "user": user_profile,
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

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=request.user.id,
                    country_id=user_profile.country_id,
                    question_id=question.id,
                    answer=answer,
                    remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_three')  # redirect to section three

    # render view
    return render(request, "questionnare/section_two.html", context)


# section three
def section_three(request):
   # questions
    questions = QuestionList.objects.filter(section_id=3)

    # context
    context = {
        "user_id": request.user.id,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        country_id = request.POST.get('country_id')
        section_id = request.POST.get('section_id')

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                # todo: check for attachment and upload

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=user_id, country_id=country_id, question_id=question.id, answer=answer, remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_four')  # redirect to section four

    # render view
    return render(request, "questionnare/section_three.html", context)


# section four
def section_four(request):
   # questions
    questions = QuestionList.objects.filter(section_id=4)

    # context
    context = {
        "user_id": request.user.id,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        country_id = request.POST.get('country_id')
        section_id = request.POST.get('section_id')

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                # todo: check for attachment and upload

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=user_id, country_id=country_id, question_id=question.id, answer=answer, remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_five')  # redirect to section five

    # render view
    return render(request, "questionnare/section_four.html", context)


# section five
def section_five(request):
   # questions
    questions = QuestionList.objects.filter(section_id=5)

    # context
    context = {
        "user_id": request.user.id,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        country_id = request.POST.get('country_id')
        section_id = request.POST.get('section_id')

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                # todo: check for attachment and upload

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=user_id, country_id=country_id, question_id=question.id, answer=answer, remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/section_six')  # redirect to section six

    # render view
    return render(request, "questionnare/section_five.html", context)


# section six
def section_six(request):
   # questions
    questions = QuestionList.objects.filter(section_id=6)

    # context
    context = {
        "user": request.user.id,
        "questions": questions
    }

    # post data
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        country_id = request.POST.get('country_id')
        section_id = request.POST.get('section_id')

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                # todo: check for attachment and upload

                #save or update
                AnsBank.objects.update_or_create(
                    created_by_id=user_id, country_id=country_id, question_id=question.id, answer=answer, remarks=remarks
                )
        if(request.POST.get('post_exit')):
            return redirect('/success')  # return to exit page
        elif(request.POST.get('post_next')):
            return redirect('/success')  # redirect to success

    # render view
    return render(request, "questionnare/section_six.html", context)


# question create view
class QuestionnareCreateView(generic.CreateView):
    context_object_name = 'questions'
    template_name = "questionnare/questionsM.html"
    success_url = reverse_lazy('questionnare:success')

    def get(self, request, **kwargs):
        # questions lists
        questions = QuestionList.objects.all()

        # user
        user_id = request.user.id

        # render view
        return render(request, self.template_name, {'questions': questions, 'user_id': user_id})


# api to post answer
def api_post_answers(request):
    if request.method == "POST":
        user_id = request.POST.get('user_id')
        country_id = request.POST.get('country_id')
        section_id = request.POST.get('section_id')

        # query questions
        questions = QuestionList.objects.filter(
            section_id=section_id).order_by('sort_order', 'code')

        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']')

            if answer is not None:
                AnsBank.objects.update_or_create(
                    created_by_id=user_id, country_id=country_id, question_id=question.id, answer=answer, remarks=remarks
                )

        # return json with success message
        return JsonResponse({'error': False, 'message': 'Successfully inserted answers'})
    else:
        return JsonResponse({'error': True, 'message': 'Failed to inserted answers'})


class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = "questionnare/index.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['councils'] = Council.objects.all()
        context['countries'] = Country.objects.all()
        context['institutions'] = Institution.objects.all()

        categories = Category.objects.prefetch_related(
            Prefetch('questions', queryset=Question.objects.order_by('sort_order')),
            Prefetch('questions__sub_questions', queryset=SubQuestion.objects.order_by('sort_order'))).order_by('id').all()
        context['categories'] = categories
        return context


class CountryList(generic.ListView):
    model = Country
    context_object_name = 'countries'
    template_name = "manage/country_response.html"

    def get_context_data(self, **kwargs):
        context = super(CountryList, self).get_context_data(**kwargs)
        last_update = AnsBank.objects.all().order_by(
            'country', '-created_at').distinct('country').values()
        context['countries'] = Country.objects.all().order_by('title').values()

        tmp = [0] * 100
        for update in last_update:
            tmp[update['country_id']] = update['created_at']

        context['last_update'] = tmp
        print(context['countries'])
        return context


# success


def success(request):
    return render(None, "questionnare/success.html", {})

# get countries


def get_countries(request):
    if request.method == 'GET':
        council_id = request.GET.get('council_id')
        countries = Country.objects.filter(council_id=council_id)

        # return response.
        return render(None, 'questionnare/countries.html', {'countries': countries})

# get


def show_question(request):
    if request.method == 'GET':
        qn_id = request.GET.get('question_id')
        question = Question.objects.get(pk=qn_id)

        # return response
        return JsonResponse({'id': question.id, 'placeholder': question.placeholder})
