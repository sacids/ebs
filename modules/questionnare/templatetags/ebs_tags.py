from django import template
from django.http import request
from ..models import *
from django.http import Http404

register = template.Library()


@register.filter
def get_by_index(l, i):
    return l[i]


@register.filter
def get_qn_title(qn_id):
    question = QuestionList.objects.get(pk=qn_id)
    return question.code + '. ' + question.title


@register.filter
def get_qn_hint(qn_id):
    question = QuestionList.objects.get(pk=qn_id)
    return question.hints


@register.filter
def get_qn_answer(qn_id, user):
    try:
        answers = AnsBank.objects.get(country_id=user.profiles.country_id, question_id=qn_id)
        return answers.answer
    except AnsBank.DoesNotExist:
        return ""


@register.filter
def get_qn_remarks(qn_id, user):
    try:
        answers = AnsBank.objects.get(country_id=user.profiles.country_id, question_id=qn_id)
        return answers.remarks
    except AnsBank.DoesNotExist:
        return ""

@register.filter
def get_qn_attachments(qn_id, user):
    try:
        answers = AnsBank.objects.get(country_id=user.profiles.country_id, question_id=qn_id)
        
        #query attachment based on answers
        attachments = ''

        return answers.remarks
    except AnsBank.DoesNotExist:
        return ""

@register.filter
def get_sub_questions(qn_id):
    qn_banks = QuestionBank.objects.filter(question_id=qn_id)
    return qn_banks
