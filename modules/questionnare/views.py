from modules.questionnare.forms import RespondentForm
from django.db.models.query import Prefetch
from django.http import request
from django.urls import reverse_lazy
from django.shortcuts import redirect, render, HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from .models import *
from .forms import RespondentForm

# Create your views here.
class RespondentCreateView(generic.CreateView):
    models = Respondent
    form_class = RespondentForm
    context_object_name = 'questions'
    template_name = "questionnare/index.html"
    success_url = reverse_lazy('questionnare:success')

    def get_context_data(self, **kwargs):
        context = super(RespondentCreateView, self).get_context_data(**kwargs)

        categories = Category.objects.prefetch_related(
            Prefetch('questions', queryset=Question.objects.order_by('sort_order')),
            Prefetch('questions__sub_questions', queryset=SubQuestion.objects.order_by('sort_order'))).order_by('id').all()
        context['categories'] = categories

        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        # Verify form is valid
        if form.is_valid():
            # Call parent form_valid to create model record object
            # super(RespondentCreateView,self).form_valid(form)

            # model
            respondent = Respondent()
            respondent.name = form.cleaned_data['name']
            respondent.designation = form.cleaned_data['designation']
            respondent.council = form.cleaned_data['council']
            respondent.country = form.cleaned_data['country']
            respondent.institution = form.cleaned_data['institution']
            respondent.save()  # finaly save

            # insert answers
            if request.POST.get('question_id'):
                question_ids = request.POST.getlist('question_id', '')
                answers = request.POST.getlist('answer', '')
                remarks = request.POST.getlist('remarks', '')

                # zipped
                zipped = zip(question_ids, answers, remarks)

                for question_id, answer, remark in zipped:  
                    qn_object = Question.objects.get(pk = question_id)

                    qn_answer = Answer()
                    if(qn_object.has_sub == "NO"):
                        qn_answer.respondent_id = respondent.id
                        qn_answer.question_id = question_id
                        qn_answer.answer = answer
                        qn_answer.remarks = remark
                        qn_answer.save()  # save
                    elif(qn_object.has_sub == "YES"):
                        sub_question_ids = request.POST.getlist('sub_question_id', '')
                        sub_qn_answers = request.POST.getlist('sub_qn_answer', '')
                        sub_qn_remarks = request.POST.getlist('sub_qn_remarks', '')

                        #sub zipped
                        sub_zipped = zip(sub_question_ids, sub_qn_answers, sub_qn_remarks)

                        for sub_qn_id, sub_qn_answer, sub_qn_remark in sub_zipped:
                            qn_answer.respondent_id = respondent.id
                            qn_answer.question_id = question_id
                            qn_answer.sub_question_id = sub_qn_id
                            qn_answer.answer = sub_qn_answer
                            qn_answer.remarks = sub_qn_remark
                            qn_answer.save()  # save 

            # Redirect to success page
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

    def post(self, request, *args, **kwargs):
        if request.method == "POST":

            if request.POST.get('question_id'):
                question_id = request.POST.getlist('question_id', '')
                answer = request.POST.getlist('answer', '')
                remarks = request.POST.getlist('remarks', '')

                # zipped
                zipped = zip(question_id, answer, remarks)

                for question_id, answer, remarks in zipped:
                    qn_answer = Answer()
                    qn_answer.question_id = question_id
                    qn_answer.answer = answer
                    qn_answer.remarks = remarks
                    qn_answer.save()  # save
                messages.add_message(
                    request, messages.SUCCESS, 'Success! Saved Successfully!')
            return redirect("/")
        else:
            form_class = RespondentForm
            return render(request, 'questionnare/index.html', {'form': form_class, })


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
