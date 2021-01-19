from modeltranslation.translator import translator, TranslationOptions
from .models import Section, QuestionList


class SectionTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


class QuestionListTransalationOptions(TranslationOptions):
    fields = ('title', 'hints',)    


translator.register(Section, SectionTranslationOptions)    
translator.register(QuestionList, QuestionListTransalationOptions)    