from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

# Create your models here.
QUESTION_TYPE = (
    ('NONE', "None"),
    ('RADIO', "Radio"),
    ('SELECT', "Select One"),
    ('CHECKBOX', "Select Multiple"),
    ('NUMBER', 'Number'),
    ('FILE', 'File'),
    ('TEXT', "Normal Text"),
    ('TEXTAREA', "Text Area"),
)

SUB_QUESTION_TYPES = (
    ("NO", "No"),
    ("SUB", "Sub"),
    ("INNER", "Inner"),
    ("END", "End")
)

ANSWER = (
    ("YES", "Yes"),
    ("NO", "No"),
    ("NONE", "None")
)

STATUS = (
    ("INCOMPLETE", "Incomplete"),
    ("SUBMITTED", "Submitted"),
    ("VERIFIED", "Verified")
)
# councils


class Council(models.Model):
    """A class to create council table"""
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    class Meta:
        db_table = "councils"
        verbose_name_plural = "Councils"
        managed = True

    def __str__(self):
        return self.title

# countries


class Country(models.Model):
    """A class to create country table."""
    title   = models.CharField(max_length=100)
    council = models.ForeignKey(Council, on_delete=models.SET_NULL, null=True)
    status  = models.CharField(choices=STATUS, max_length=20, null=True, default="NO")

    class Meta:
        db_table = "countries"
        verbose_name_plural = "Countries"
        managed = True

    def __str__(self):
        return self.title

# institutions


class Institution(models.Model):
    """A class to create institutions table."""
    title = models.CharField(max_length=255)
    initial = models.CharField(max_length=25, null=True)
    description = models.TextField(null=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    logo = models.ImageField(upload_to='photos', null=True)

    class Meta:
        db_table = "institutions"
        verbose_name_plural = "Institutions"
        managed = True

    def __str__(self):
        return self.title

# Respondent


class Respondent(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, null=True)
    council = models.ForeignKey(Council, related_name="council", on_delete=models.SET_NULL, null=True)
    country = models.ForeignKey(Country, related_name="country", on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=150)
    institution = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "respondents"
        verbose_name_plural = "Respondents"
        managed = True

    def __str__(self):
        return self.name


# categories
class Category(models.Model):
    code = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Categories"
        managed = True

    def __str__(self):
        return self.title

#survey
class Survey(models.Model):
    title = models.TextField(null=False)
    description = models.TextField(null=True)

    class Meta:
        db_table = 'surveys'
        verbose_name_plural = "Surveys"
        managed = True

    def __str__(self):
        return self.title


class CountrySurvey(models.Model):
    country = models.ForeignKey(Country, related_name="country_survey", on_delete=models.DO_NOTHING, blank=True, null=True)
    survey = ForeignKey(Survey, related_name="survey_status", on_delete=models.DO_NOTHING, null=True)
    status  = models.CharField(choices=STATUS, max_length=20, null=True, default="INCOMPLETE")
    created_at  = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at  = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "country_surveys"
        verbose_name_plural = "Country Survey Status"
        managed = True

    def __str__(self):
        return self.status

# section
class Section(models.Model):
    survey = ForeignKey(Survey, related_name="sections", on_delete=models.CASCADE, null=True, default=1)
    code = models.PositiveIntegerField(null=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    class Meta:
        db_table = "sections"
        verbose_name_plural = "Sections"
        managed = True

    def __str__(self):
        return self.title


# questions
class QuestionList(models.Model):
    section = models.ForeignKey(Section, related_name="questions", on_delete=models.CASCADE, null=True)
    code = models.CharField(max_length=10, null=False)
    title = models.TextField(null=False)
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='RADIO')
    required = models.CharField(choices=ANSWER, max_length=10, default="NO")
    has_sub = models.CharField(choices=SUB_QUESTION_TYPES, verbose_name="Sub Question", max_length=10, null=True, default="NO")
    sort_order = models.IntegerField(default=1)
    hints  = models.TextField(null=True, blank=True)
    has_upload = models.CharField(choices=ANSWER, max_length=10, default="NO")

    class Meta:
        db_table = "question_lists"
        verbose_name_plural = "Questions"
        managed = True

    def __str__(self):
        return self.code + ": " + self.title



class AnsBank(models.Model):
    created_by  = models.ForeignKey(User,related_name="created_by", on_delete=models.DO_NOTHING, blank=True, null=True)
    country     = models.ForeignKey(Country,related_name="ans_country", on_delete=models.DO_NOTHING, blank=True, null=True)
    question    = models.ForeignKey(QuestionList, related_name="question", on_delete=models.CASCADE)
    answer      = models.TextField(null=False)
    remarks     = models.TextField(null=True)
    created_at  = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table            = "ansbank"
        verbose_name_plural = "Answers"
        managed             = True
        unique_together     = ('country', 'question',)

    def __str__(self):
        return str(self.question.id)+' '+self.answer

def get_upload_to(instance, filename):
    return 'attachments/%s/%s' % (instance.ansbank.country.title, filename)
    

class Attachments(models.Model):
    ansbank     = models.ForeignKey(AnsBank, related_name="uploads", on_delete=models.CASCADE)
    uploads     = models.FileField(upload_to=get_upload_to)
    class Meta:
        db_table = "attachments"
        verbose_name_plural = "attachments"
        managed = True

    def __str__(self):
        return str(self.id)