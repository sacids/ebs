from modeltranslation.translator import translator, TranslationOptions
from .models import Section, QuestionList, Survey


class SectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class QuestionListTransalationOptions(TranslationOptions):
    fields = ('title', 'hints',)    


class SurveyTransalationOptions(TranslationOptions):
    fields = ("title",)    


translator.register(Section, SectionTranslationOptions)    
translator.register(QuestionList, QuestionListTransalationOptions)   
translator.register(Survey, SurveyTransalationOptions) 