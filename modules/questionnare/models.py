from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT

# Create your models here.
QUESTION_TYPE = (
    ('SELECT',"Select One"),
    ('CHECKBOX',"Select Multiple"),
    ('TEXTAREA',"Free Text"),
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

#institutions
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

#Respondent
class Respondent(models.Model):
    name = models.CharField(max_length=200)
    designation = models.CharField(max_length=150)
    institution = models.ForeignKey(Institution, on_delete=RESTRICT)

    class Meta:
        db_table = "respondents"
        verbose_name_plural = "Respondents"

    def __str__(self):
        return self.name  


#categories
class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)

    class Meta:
        db_table ="categories"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title


#questions
class Question(models.Model):
    category = models.ForeignKey(Category, related_name="questions", on_delete=CASCADE)
    title = models.TextField(null=False)
    code = models.CharField(max_length=5, null=False)
    qn_type = models.CharField(choices=QUESTION_TYPE, verbose_name="Question type", max_length=50, default='SELECT')
    
    class Meta:
        db_table = "questions"
        verbose_name_plural = "Questions"

    def __str__(self):
        return self.title    