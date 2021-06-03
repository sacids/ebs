from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Council)
class CouncilAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title__startwith']
    ordering = ("id",)


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    search_fields = ['title__startwith']
    ordering = ("id",)


# @admin.register(Institution)
# class InstitutionAdmin(admin.ModelAdmin):
#     list_display = ['id', 'title', 'initial', 'country']
#     list_filter = ['initial']
#     search_fields = ['title__startwith']
#     ordering = ("id",)


# @admin.register(Respondent)
# class RespondentAdmin(admin.ModelAdmin):
#     list_display = ['name', 'designation', 'institution']
#     search_fields = ['name__startwith']
#     ordering = ("name",)

# class QuestionInline(admin.StackedInline):
#     model = Question   

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ['title', 'description']
#     ordering = ("id",)  
#     inlines = [QuestionInline]

# class SubQuestionInline(admin.StackedInline):
#     model = SubQuestion  

# @admin.register(Question)
# class QuestionAdmin(admin.ModelAdmin):
#     list_display = ['code','title', 'has_sub']
#     list_filter = ['category', 'has_sub']
#     ordering = ("sort_order",)
#     inlines = [SubQuestionInline]

#Survey
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    ordering = ("id",)

#section
@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id','title']
    ordering = ("id",)  


#Question List
@admin.register(QuestionList)
class QuestionListAdmin(admin.ModelAdmin):
    list_display = ['id','code','title', 'required']
    list_filter = ['section']
    ordering = ("section","code",)


#Question Bank  
# @admin.register(QuestionBank)
# class QuestionBankAdmin(admin.ModelAdmin):
#     list_display = ['sort_order','question']  
#     list_filter  = ['section']
#     ordering = ("section", "sort_order")
