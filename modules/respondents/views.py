from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from ..questionnare.models import *
from django.db.models.query import Prefetch
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


# Create your views here.

class RespondentsListView(LoginRequiredMixin, generic.ListView):
    model = Respondent
    context_object_name = 'respondents'
    template_name = "lists.html"
    paginate_by = 25

    def get_context_data(self, **kwargs):
        context = super(RespondentsListView, self).get_context_data(**kwargs)
        respondents = Respondent.objects.select_related(
            'council', 'country').all()

        page = self.request.GET.get('page')
        paginator = Paginator(respondents, self.paginate_by)
        try:
            respondents = paginator.page(page)
        except PageNotAnInteger:
            respondents = paginator.page(1)
        except EmptyPage:
            respondents = paginator.page(paginator.num_pages)
        context['respondents'] = respondents    

        return context


class RespondentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Respondent
    context_object_name = 'respondents'
    template_name = "details.html"

    def get_context_data(self, **kwargs):
        context = super(RespondentDetailView, self).get_context_data(**kwargs)
        respondent_id = self.kwargs['pk']
        context['respondent'] = Respondent.objects.select_related('country','council').get(pk=respondent_id)

        categories = Category.objects.prefetch_related(
            Prefetch('questions', queryset=Question.objects.order_by('sort_order')),
            Prefetch('questions__sub_questions', queryset=SubQuestion.objects.order_by('sort_order'))).order_by('id').all()
        context['categories'] = categories
        return context


class RespondentDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Respondent
    success_url = reverse_lazy('respondents:lists')

    def get(self, *args, **kwargs):
        return self.post(*args, **kwargs)