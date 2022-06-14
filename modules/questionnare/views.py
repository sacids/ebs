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
from django.db.models import Q
from .models import *
from .utils import render_to_pdf
from .forms import RespondentForm
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from ..notification.views import send_notification


@login_required(login_url='/login')
def surveys(request):
    if request.user.is_authenticated:
        # get all survey
        surveys = Survey.objects.all().order_by('id')

        # country
        country = Country.objects.get(pk=request.user.profiles.country_id)

        context = {
            'country': country,
            'surveys': surveys
        }

        # render view
        return render(request, "questionnare/surveys.html", context)


@login_required(login_url='/login')
def introduction(request):
    # survey
    survey_id = request.GET.get('sv_id', -1)
    survey = get_object_or_404(Survey.objects.all(), pk=survey_id)

    context = {
        "survey": survey,
    }

    # render view
    return render(request, "questionnare/introduction.html", context)


@login_required(login_url='/login')
def questions(request):
    # survey
    survey_id = request.GET.get('sv_id', -1)
    survey = get_object_or_404(Survey.objects.all(), pk=survey_id)

    #section_id
    section_id = request.GET.get('sc_id', -1)

    if section_id == -1:
        section = Section.objects.filter(survey_id=survey_id).order_by("code")[0]
    else:
        section = get_object_or_404(Section.objects.all(), pk=section_id)  

    #questions
    questions = QuestionList.objects.filter(section_id = section.id).order_by("code", "sort_order")  

     # context
    context = {
        "survey": survey,
        "section_id": section_id,
        "section": section,
        "questions": questions
    }    

    # post data
    if request.method == "POST":
        for question in questions:
            answer = request.POST.get('answer[' + str(question.id) + ']')
            remarks = request.POST.get('remarks[' + str(question.id) + ']') 

            if answer is not None:
                # save or update
                obj, created = AnsBank.objects.update_or_create(
                    question_id=question.id, country_id=request.user.profiles.country_id,
                    defaults={'created_by_id': request.user.id, 'country_id': request.user.profiles.country_id,
                            'question_id': question.id, 'answer': answer, 'remarks': remarks},)

                # check for attachment and upload
                if request.FILES is not None:
                    attachment_files = request.FILES.getlist(
                        'attachments[' + str(question.id) + ']')
                    for f in attachment_files:
                        newAttachment = Attachments()
                        newAttachment.ansbank_id = obj.id
                        newAttachment.uploads = f
                        newAttachment.save()

        # redirect
        if(request.POST.get('post_exit')):
            # first save country survey status
            try:
                country_survey = CountrySurvey.objects.get(
                    country_id=request.user.profiles.country_id, survey_id=survey.id)
                # do nothing
            except:
                # save new country survey
                country_survey = CountrySurvey()
                country_survey.country_id = request.user.profiles.country_id
                country_survey.survey_id = survey.id
                country_survey.status = "INCOMPLETE"
                country_survey.save()

            #redirect
            return redirect('/questionnare/success/?sv_id=' + str(survey.id) + '&sc_id=' + str(section.id))
        elif(request.POST.get('post_next')):
            if section.code < survey.sections.count():
                # first save country survey status
                try:
                    country_survey = CountrySurvey.objects.get(
                        country_id=request.user.profiles.country_id, survey_id=survey.id)
                    # do nothing
                except:
                    # save new country survey
                    country_survey = CountrySurvey()
                    country_survey.country_id = request.user.profiles.country_id
                    country_survey.survey_id = survey.id
                    country_survey.status = "INCOMPLETE"
                    country_survey.save()

                #iterate to next code
                section_code = section.code + 1

                #survey
                section = Section.objects.filter(survey_id=survey.id, code=section_code)

                if section is not None:
                    return redirect('/questionnare/questions/?sv_id=' + str(survey.id) + "&sc_id=" + str(section[0].id))   
                else:
                    return redirect('/questionnare/questions/?sv_id=' + str(survey.id))  

            elif section.code == survey.sections.count():  
                # validate questions
                required_questions = []
                for question in questions:
                    print(question.required)
                    if question.required == 'YES':
                        required_questions.append(question.id)


                if required_questions is not None:
                    j = 0
                    for id in required_questions: 
                        question = QuestionList.objects.get(id)        
                        
                        # query in answer bank
                        try:
                            ans_bank = AnsBank.objects.get(
                                question_id=question.id, country_id=request.user.profiles.country_id)
                        except:
                            messages.add_message(request, messages.ERROR, 'Question number ' + question.code + ' required')
                            j=j+1

                    # check if there no required question
                    if(j == 0):
                        # change country survey survey
                        country_survey = CountrySurvey.objects.get(
                            country=request.user.profiles.country_id, survey=survey.id)
                        country_survey.status = "COMPLETE"
                        country_survey.save()

                        # country
                        country = Country.objects.get(
                            pk=request.user.profiles.country_id)

                        # send message
                        subject = 'Submission Alert: Situation analysis of EBS implementation in Africa'

                        message = '<p>Dear Reviewers,</p>'
                        message += '<p>Data for <b>' + country.title + '</b>' + \
                            ' has been Submitted.</p>'
                        message += '<p>For review and approval please <a href="https://ebs-survey.africacdc.org/">click here</a></p>'

                        # send email notification
                        send_notification(subject, message, from_email=request.user.email,
                                        to_email=['renfrid.ngolongolo@sacids.org'])

                        # redirect to success
                        return redirect('/questionnare/success/?sv_id=' + str(survey.id) + '&sc_id=' + str(section.id))      

    # render view
    return render(request, "questionnare/questions.html", context)


@login_required(login_url='/login')
def success(request):
    # survey
    survey_id = request.GET.get('sv_id', -1)
    survey = get_object_or_404(Survey.objects.all(), pk=survey_id)

    #section_id
    section_id = request.GET.get('sc_id', -1)

    if section_id == -1:
        #get first section
        section = Section.objects.filter(survey_id=survey_id).order_by("code")[0]
    else:
        section = get_object_or_404(Section.objects.all(), pk=section_id) 

    # country
    try:
        country_survey = CountrySurvey.objects.get(
            country=request.user.profiles.country_id, survey=survey.id)
    except:
        country_survey = []
        pass 

     # context
    context = {
        "country_survey": country_survey,
        "survey": survey,
        "section": section
    }   

    #render view
    return render(request, "questionnare/success.html", context)



# =================================================================
# Others callback functions
#================================================================#
def get_countries(request):
    if request.method == 'GET':
        council_id = request.GET.get('council_id')
        countries = Country.objects.filter(council_id=council_id)

        # return response.
        return render(None, 'questionnare/countries.html', {'countries': countries})
