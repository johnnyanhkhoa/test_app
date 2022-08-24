from dataclasses import fields
from django import forms
from django.forms import ModelForm, TextInput
from django.forms.models import inlineformset_factory
from quotation.models import *
from .models import *
from django.contrib.admin.widgets import AdminSplitDateTime

# YEARS
years = []
for year in range(2000,2050):
    years.append(year)

customers = Customer.objects.only('id')
products = Product.objects.only('id')
statuses = Status.objects.only('id')
channels = Channel.objects.only('id')

class CreateQuotationForm(forms.ModelForm):
    customer_id = forms.ModelChoiceField(required=False, queryset=customers ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Customer name",
    }))
    channel = forms.ModelChoiceField(required=False, queryset=channels ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Channel",
    }))
    quotation_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Quotation number",
    }))
    quotation_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    quotation_remark = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Quotation remark",
    }))
    class Meta:
        model = Quotation
        fields = ['customer_id', 'channel', 'quotation_no', 'quotation_date', 'quotation_remark']
        
class QuotationFollowupForm(forms.ModelForm):
    quotation_status = forms.ModelChoiceField(required=False, queryset=statuses ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Customer name",
    }))
    status_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    class Meta:
        model = Quotation
        fields = ['quotation_status','status_date']
        

# class AddProductToQuotationForm(forms.ModelForm):
#     customer_id = forms.ModelChoiceField(queryset=customers ,widget=forms.Select(attrs={
#         "class": "form-control bg-white", "placeholder": "Customer name",
#     }))
#     quotation_no = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control", "placeholder": "Quotation number",
#     }))
#     quotation_date = forms.DateField(widget=forms.SelectDateWidget(attrs={
#          "placeholder": "Quotation date",
#     }))
#     quotation_remark = forms.CharField(widget=forms.TextInput(attrs={
#         "class": "form-control", "placeholder": "Quotation remark",
#     }))
#     class Meta:
#         model = Quotation
#         fields = ['customer_id', 'quotation_no', 'quotation_date', 'quotation_remark']


class CreateContractForm(forms.ModelForm):
    customer_id = forms.ModelChoiceField(required=False, queryset=customers ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Customer name",
    }))
    channel = forms.ModelChoiceField(required=False, queryset=channels ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Channel",
    }))
    contract_no = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Contract number",
    }))
    contract_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    valid_from_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    valid_to_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    placement_time_in_prior_to_delivery = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Placement time in prior to delivery",
    }))
    delivery_time = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
         "placeholder": "yyyy-mm-dd HH:MM:SS",
    }))
    registration_document = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Registration document",
    }))
    payment_method = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Payment method",
    }))
    payment_due = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Payment due",
    }))
    penalty_rate_for_late_payment = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Penalty rate for late payment",
    }))
    bank_charges_related_to_payment = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Bank charges related to payment",
    }))
    delivery_point = forms.CharField(required=False, widget=TextInput(attrs={
        "class": "form-control", "placeholder": "Delivery point",
    }))
    enquiry_for_goods_receipt = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Enquiry for goods receipt",
    }))
    enquiry_for_goods_return = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Enquiry for goods return",
    }))
    documents_to_be_delivered_with_each_delivery = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Enquiry for goods return",
    }))
    complaint_time_due_to_product_issue = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Complaint time due to product issue",
    }))
    compensation_time = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Compensation time",
    }))
    support_fee_on_target_achivement = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee on target achivement",
    }))
    support_fee_on_transportation = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee on transportation",
    }))
    support_fee_for_payment_due_date = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for payment due date",
    }))
    support_fee_for_new_pos = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for new pos",
    }))
    support_fee_for_display = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for display",
    }))
    support_fee_for_listing = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for listing",
    }))
    support_fee_for_advertising_and_birthday = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for advertising and birthday",
    }))
    support_fee_for_product_creation = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Support fee for product creation",
    }))
    method_of_support_fee_payment = forms.CharField(required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Method of support fee_payment",
    }))
    penalty_for_agreement_breach = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Penalty for agreement breach",
    }))
    class Meta:
        model = Contract
        fields = ['customer_id', 'channel', 'contract_no', 'contract_date','valid_from_date',
                  'valid_to_date', 'placement_time_in_prior_to_delivery', 'delivery_time', 'registration_document', 'payment_method',
                  'payment_due', 'penalty_rate_for_late_payment', 'bank_charges_related_to_payment' , 'delivery_point', 'enquiry_for_goods_receipt',
                  'enquiry_for_goods_return', 'documents_to_be_delivered_with_each_delivery', 'complaint_time_due_to_product_issue', 'compensation_time', 'support_fee_on_target_achivement',
                  'support_fee_on_transportation', 'support_fee_for_payment_due_date', 'support_fee_for_new_pos', 'support_fee_for_display', 'support_fee_for_listing',
                  'support_fee_for_advertising_and_birthday', 'support_fee_for_product_creation', 'method_of_support_fee_payment', 'penalty_for_agreement_breach']