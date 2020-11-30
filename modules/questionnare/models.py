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
    ("NEW", "New"),
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
    status  = models.CharField(choices=STATUS, verbose_name="Has sub question?", max_length=10, null=True, default="NO")

    class Meta:
        db_table = "contries"
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


# questions
class Question(models.Model):
    category = models.ForeignKey(Category, related_name="questions", on_delete=models.CASCADE)
    title = models.TextField(null=False)
    code = models.CharField(max_length=10, null=False)
    placeholder = models.TextField(null=True)
    has_sub = models.CharField(choices=ANSWER, verbose_name="Has sub question?", max_length=10, null=True, default="NO")
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='NONE')
    sort_order = models.IntegerField(default=1)

    class Meta:
        db_table = "questions"
        verbose_name_plural = "Questions"
        managed = True

    def __str__(self):
        return self.title


# sub question
class SubQuestion(models.Model):
    question = ForeignKey(Question, related_name="sub_questions", on_delete=models.CASCADE)
    title = models.TextField(null=False)
    code = models.CharField(max_length=10, null=False)
    placeholder = models.TextField(null=True)
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='NONE')
    sort_order = models.IntegerField(default=1)

    class Meta:
        db_table = "sub_questions"
        verbose_name_plural = "Sub Questions"
        managed = True

    def __str__(self):
        return self.title

# answer


class Answer(models.Model):
    respondent = models.ForeignKey(Respondent, related_name="respondents", on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    sub_question = models.ForeignKey(SubQuestion, on_delete=models.SET_NULL, null=True)
    answer = models.CharField(max_length=200, null=False)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "answers"
        verbose_name_plural = "Answers"
        managed = True

    def __str__(self):
        return self.question


# section
class Section(models.Model):
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



# questions banks
class QuestionBank(models.Model):
    sort_order = models.IntegerField(default=1)
    section = models.ForeignKey(Section, related_name="question_banks", on_delete=models.CASCADE)
    question = models.OneToOneField(QuestionList, related_name="sub_question_banks", on_delete=CASCADE)
    sub_questions = models.ManyToManyField(
        QuestionList, blank=True)

    class Meta:
        db_table = "question_banks"
        verbose_name_plural = "Question Banks"
        managed = True

    def __str__(self):
        return self.section.title + str(self.question.id)


class AnsBank(models.Model):
    created_by  = models.ForeignKey(User,related_name="created_by", on_delete=models.DO_NOTHING, blank=True, null=True)
    country     = models.ForeignKey(Country,related_name="ans_country", on_delete=models.DO_NOTHING, blank=True, null=True)
    question    = models.ForeignKey(QuestionList, on_delete=models.CASCADE)
    answer      = models.CharField(max_length=200, null=False)
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
    return 'attachments/%d/%s' % (instance.ansbank.country.title, filename)

    
class Attachments(models.Model):
    ansbank     = models.ForeignKey(AnsBank, related_name="uploads", on_delete=models.CASCADE)
    uploads     = models.FileField(upload_to=get_upload_to)
    class Meta:
        db_table = "attachments"
        verbose_name_plural = "attachments"
        managed = True

    def __str__(self):
        return self.id