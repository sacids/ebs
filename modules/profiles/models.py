from django.db import models
from authtools.models import User
from modules.questionnare.models import Council, Country
from django.conf import settings

# Create your models here.
class Profiles(models.Model):
    """A class to create profiles table""" 
    user        = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    council     = models.ForeignKey(Council, related_name="profile_council", on_delete=models.SET_NULL, null=True)
    country     = models.ForeignKey(Country, related_name="profile_country", on_delete=models.SET_NULL, null=True)
    designation = models.CharField(max_length=150)
    institution = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "profiles"
        verbose_name_plural = "profiles"
        managed = True

    def __str__(self):
        return self.id