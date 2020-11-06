from django import template
from ..models import *

register = template.Library()


@register.filter
def get_by_index(l, i):
    return l[i]


@register.filter
def get_qn_object(qn_id):
    question = QuestionList.objects.get(pk=qn_id)
    return question

@register.filter
def get_sub_questions(qn_id):
    qn_banks = QuestionBank.objects.filter(question_id=qn_id)
    return qn_banks
