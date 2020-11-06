import json
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

# default


def default(request):
    if request.method == 'POST':
        inputEmail = request.POST.get('email')

        try:
            respondent = Respondent.objects.get(email=inputEmail)
        except ObjectDoesNotExist:
            messages.add_message(request, messages.ERROR,
                                 'Email address does not exist')
        else:
            # redirect
            return redirect('questions/%s' % respondent.id)

    # render view
    return render(request, 'questionnare/index.html', {})


# question create view
class QuestionnareCreateView(generic.CreateView):
    context_object_name = 'questions'
    template_name = "questionnare/questions.html"
    success_url = reverse_lazy('questionnare:success')

    def get(self, request, **kwargs):
        # if request.user.is_authenticated:
        #     return redirect("")
        # else:

        # # sections
        sections = Section.objects.prefetch_related(
            Prefetch('question_banks', queryset=QuestionBank.objects.order_by('sort_order'))).all()

        return render(request, self.template_name, {'sections': sections})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Verify form is valid
        if form.is_valid():

            # respondent
            user_id = kwargs['pk']

            # todo: query user

            # if post next => save
            if request.POST.get('post_next'):
                question_ids = request.POST.getlist('question_id', '')
                answers = request.POST.getlist('answer', '')
                remarks = request.POST.getlist('remarks', '')

                # zipped
                zipped = zip(question_ids, answers, remarks)

                for question_id, answer, remark in zipped:
                    #create or update
                    AnsBank.objects.update_or_create(
                        created_by_id=user_id, question_id=question_id, answer=answer, remarks=remark
                    )

            # Redirect to to a page after save and exit
            if request.POST.get('post_exit'):
                return redirect('success/')
        # Form is invalid
        # Set object to None, since class-based view expects model record object
        self.object = None
        # Return class-based view form_invalid to generate form with errors
        return self.form_invalid(form)


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
    model               = Country
    context_object_name = 'countries'
    template_name       = "manage/country_response.html"
    
    def get_context_data(self, **kwargs):
        context                 = super(CountryList, self).get_context_data(**kwargs)
        last_update             = AnsBank.objects.all().order_by('country', '-created_at').distinct('country').values()
        context['countries']    = Country.objects.all().order_by('title').values()

        tmp     = [0] * 100
        for update in last_update:
            tmp[update['country_id']]  = update['created_at']
        
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
