from dataclasses import fields
from django import forms
from django.forms import ModelForm, TextInput
from django.forms.models import inlineformset_factory
from quotation.models import *
from .models import *
from django.contrib.admin.widgets import AdminSplitDateTime

statuses = Status.objects.only('id')

class ContractFollowupForm(forms.ModelForm):
    contract_status = forms.ModelChoiceField(required=False, queryset=statuses ,widget=forms.Select(attrs={
        "class": "form-control bg-white text-dark",
    }))
    status_date = forms.DateField(required=False, widget=forms.SelectDateWidget(attrs={
         "placeholder": "Date",
    }))
    class Meta:
        model = Contract
        fields = ['contract_status','status_date']
        

        

