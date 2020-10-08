from django import forms
from django.db.models import fields
from .models import *


class RespondentForm(forms.ModelForm):
    council = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Council.objects.all(), empty_label="-- Select--")

    country = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Country.objects.all(), empty_label="-- Select--")

    institution = forms.ModelChoiceField(
        widget=forms.Select(attrs={'class': 'form-control'}),
        queryset=Institution.objects.all(), empty_label="-- Select--")    

    class Meta:
        model = Respondent
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write full name...'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Write designation...'}),

        }
