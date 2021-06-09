from django.db import models
from django.contrib.auth.models import User
from modules.questionnare.models import Council, Country
from django.conf import settings

# Create your models here.


class Profiles(models.Model):
    """A class to create profiles table"""
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    country = models.ForeignKey(
        Country, related_name="profile_country", on_delete=models.SET_NULL, null=True, blank=True)
    designation = models.CharField(max_length=150)
    institution = models.CharField(max_length=255, null=True)
    first_login = models.PositiveIntegerField(null=False, default=1)

    class Meta:
        db_table = "profiles"
        verbose_name_plural = "profiles"
        managed = True

    def __str__(self):
        return self.designation
