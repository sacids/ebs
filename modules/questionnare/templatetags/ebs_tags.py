from django.template.loader import get_template
from django import template
from django.http import request
from ..models import *
from django.http import Http404
from django.utils.safestring import mark_safe

# template
register = template.Library()


@register.filter
def get_by_index(l, i):
    return l[i]

@register.filter(name='has_group') 
def has_group(user, group_name):
    return user.groups.filter(name=group_name).exists()

@register.filter
def get_country_survey_status(survey_id, country_id):
    try:
        country_survey = CountrySurvey.objects.get(country = country_id, survey = survey_id)
        return country_survey.status
    except:
        return "NOT STARTED"


@register.filter
def get_qn_title(qn_id):
    question = QuestionList.objects.get(pk=qn_id)
    return mark_safe('<b>' + question.code + '</b>. ' + question.title)


@register.filter
def get_qn_hint(qn_id):
    question = QuestionList.objects.get(pk=qn_id)
    return question.hints


@register.filter
def get_qn_answer(qn_id, user):
    try:
        answers = AnsBank.objects.get(
            country_id=user.profiles.country_id, question_id=qn_id)

        if answers.answer is not None or "":    
            return answers.answer.replace('\n', ' ').replace('\r', '')
    except AnsBank.DoesNotExist:
        pass


@register.filter
def get_qn_remarks(qn_id, user):
    try:
        answers = AnsBank.objects.get(
            country_id=user.profiles.country_id, question_id=qn_id)
        if answers.remarks is not None or "":  
            return answers.remarks.replace('\n', ' ').replace('\r', '')
    except AnsBank.DoesNotExist:
        pass


@register.filter
def get_sub_questions(qn_id):
    qn_banks = QuestionBank.objects.filter(question_id=qn_id)
    return qn_banks


def show_attachments(qn_id, user):
    try:
        answers = AnsBank.objects.get(
            country_id=user.profiles.country_id, question_id=qn_id)

        # query attachment based on answers
        attachments = Attachments.objects.filter(ansbank_id=answers.id)
        if attachments:
            return {'attachments': attachments}
        else:
            return {'attachments': []}
    except AnsBank.DoesNotExist:
        return {'attachments': []}        


attachment_template = get_template('questionnare/attachments.html')
register.inclusion_tag(attachment_template)(show_attachments)
