from django.http import request
from django.shortcuts import redirect, render
from django.views import generic
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

        question_arr = []
        for category in categories:
            questions = category.questions.all()
            for qn in questions:
                qn_info = {"id": qn.id, "title": qn.title,
                           "code": qn.code, "qn_type": qn.qn_type}
                question_arr.append(qn_info)

        context['categories'] = categories
        context['questions'] = question_arr
        return context

    def post(self, request, *args, **kwargs):
        if request.method == "POST":
            return redirect("/")
