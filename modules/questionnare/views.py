from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
from django.contrib import messages
from .models import *

# Create your views here.
class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'questions'
    template_name = "questionnare/index.html"

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        context['countries'] = Country.objects.all()
        context['institutions'] = Institution.objects.all()
        categories = Category.objects.prefetch_related("questions").all()
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
                    qn_answer.answer   = answer
                    qn_answer.remarks  = remarks
                    qn_answer.save() #save    
                messages.add_message(request, messages.SUCCESS,'Success! Saved Successfully!')  
            return redirect("/")
