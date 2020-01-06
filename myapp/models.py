from django.db import models
from django import forms

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    data_establish = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'company'

        
class CompanyForm(forms.Form):
    name = forms.CharField(max_length=50, required = True)
    class Meta:
        fields = ['name']