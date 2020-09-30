from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields.related import ForeignKey

# Create your models here.
QUESTION_TYPE = (
    ('NONE', "None"),
    ('SELECT', "Select One"),
    ('CHECKBOX', "Select Multiple"),
    ('NUMBER', 'Number'),
    ('TEXT', "Normal Text"),
    ('TEXTAREA', "Text Area"),
)

ANSWER = (
    ('YES', "Yes"),
    ('NO', "No"),
    ('UNKNOWN', "Unknown"),
)

# countries


class Country(models.Model):
    """A class to create country table."""
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10, null=True)

    class Meta:
        db_table = "contries"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.title

# institutions


class Institution(models.Model):
    """A class to create institutions table."""
    title = models.CharField(max_length=255)
    initial = models.CharField(max_length=25, null=True)
    description = models.TextField(null=True)
    country = models.ForeignKey(Country, on_delete=RESTRICT)
    logo = models.ImageField(upload_to='photos', null=True)

    class Meta:
        db_table = "institutions"
        verbose_name_plural = "Institutions"

    def __str__(self):
        return self.title

# Respondent


class Respondent(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    institution = models.ForeignKey(Institution, on_delete=RESTRICT)

    class Meta:
        db_table = "respondents"
        verbose_name_plural = "Respondents"

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

    def __str__(self):
        return self.title


# questions
class Question(models.Model):
    category = models.ForeignKey(
        Category, related_name="questions", on_delete=CASCADE)
    title = models.TextField(null=False)
    code = models.CharField(max_length=10, null=False)
    has_sub = models.CharField(
        choices=ANSWER, verbose_name="Has sub question?", max_length=10, null=True, default="NO")
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='NONE')

    class Meta:
        db_table = "questions"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.title



# sub question
class SubQuestion(models.Model):
    question = ForeignKey(
        Question, related_name="sub_questions", on_delete=CASCADE)
    title = models.TextField(null=False)
    code = models.CharField(max_length=10, null=False)
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='NONE')

    class Meta:
        db_table = "sub_questions"
        verbose_name_plural = "Sub Questions"

    def __str__(self):
        return self.title


# answer
class Answer(models.Model):
    #respondent  = models.ForeignKey(User, related_name="respondents", on_delete=models.SET_DEFAULT, default=1)
    question = models.ForeignKey(
        Question, related_name="answers", on_delete=models.CASCADE)
    answer = models.CharField(max_length=200, null=False)
    remarks = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        db_table = "answers"
        verbose_name_plural = "Answers"

    def __str__(self):
        return self.question
