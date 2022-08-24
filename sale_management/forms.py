from unicodedata import category
from django import forms
from django.forms import ModelForm, TextInput
from .models import *

# YEARS
years = []
for year in range(2000,2050):
    years.append(year)
# Queryset
customer_types = Customer_type.objects.only('id')
channels = Channel.objects.only('id')
provinces = Province.objects.only('id')
sale_areas = Sale_area.objects.only('id')
categories = Product_category.objects.only('id')
brands = Product_brand.objects.only('id')
# Form
class CreateProductForm(forms.ModelForm):
    product_category = forms.ModelChoiceField(required=False, queryset=categories ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Product category",
    }))
    product_brand = forms.ModelChoiceField(required=False, queryset=brands ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Product category",
    }))
    product_code = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Product code",
    }))
    product_name = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Product name",
    }))
    product_name_on_registration_document = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Product name on registration document",
    }))
    product_unit = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Product unit",
    }))
    packing_size = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Packing size",
    }))
    vat = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "VAT(%)",
    }))
    retail_selling_price_wo_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Retail selling price(-VAT)",
    }))
    retail_selling_price_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Retail selling price(+VAT)",
    }))
    selling_price_distributor_wo_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price distributor(-VAT)",
    }))
    selling_price_distributor_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price distributor(+VAT)",
    }))
    selling_price_etc_wo_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price ETC(-VAT)",
    }))
    selling_price_etc_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price ETC(+VAT)",
    }))
    selling_price_otc_wo_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price OTC(-VAT)",
    }))
    selling_price_otc_vat = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Selling price OTC(+VAT)",
    }))
    registraion_approval_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    registraion_expiry_date = forms.DateField(required=False, widget=forms.SelectDateWidget(years=years))
    registraion_reference = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Registraion reference",
    }))
    manufacture = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Manufacture",
    }))
    manufacturing_country = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Manufacturing country",
    }))
    intended_use = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Intended use",
    }))
    product_type = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Product type",
    }))
    ingredient_list = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Ingredient list",
    }))
    expiry_date = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Months",
    }))
    product_remark = forms.IntegerField(required=False, widget=forms.NumberInput(attrs={
        "class": "form-control", "placeholder": "Months",
    }))
    class Meta:
        model = Product
        fields = ['product_category', 'product_brand', 'product_code', 'product_name', 'product_name_on_registration_document',
                  'product_unit', 'packing_size', 'vat', 'retail_selling_price_wo_vat', 'retail_selling_price_vat',
                  'selling_price_distributor_wo_vat', 'selling_price_distributor_vat', 'selling_price_etc_wo_vat', 'selling_price_etc_vat', 'selling_price_otc_wo_vat',
                  'selling_price_otc_vat', 'registraion_approval_date', 'registraion_expiry_date', 'registraion_reference', 'manufacture',
                  'manufacturing_country', 'intended_use', 'product_type', 'ingredient_list', 'expiry_date',
                  'product_remark']


class CreateCustomerForm(forms.ModelForm):
    customer_name = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Customer name",
    }))
    customer_code = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Customer code",
    }))
    tax_code = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Tax code",
    }))
    customer_address = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Customer address",
    }))
    contact_no = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Contact number",
    }))
    customer_type = forms.ModelChoiceField(required=False, queryset=customer_types ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Contact number",
    }))
    channel = forms.ModelChoiceField(required=False, queryset=channels ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Channel",
    }))
    province = forms.ModelChoiceField(required=False, queryset=provinces ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Province",
    }))
    sale_area = forms.ModelChoiceField(required=False, queryset=sale_areas ,widget=forms.Select(attrs={
        "class": "form-control bg-white", "placeholder": "Sale area",
    }))
    account_no_1 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Account number 1",
    }))
    legal_name = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Legal name",
    }))
    legal_address = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Legal address",
    }))
    represented_by = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Represented by",
    }))
    phone = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Phone number",
    }))
    contact_person = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Contact person",
    }))
    fax = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Fax",
    }))
    LoA = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "LoA",
    }))
    account_no_2 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Account number 2",
    }))
    account_no_3 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Account number 3",
    }))
    bank_name_1 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Bank name 1",
    }))
    bank_name_2 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Bank name 2",
    }))
    bank_name_3 = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Bank name 3",
    }))
    remark = forms.CharField(strip=False, required=False, widget=forms.TextInput(attrs={
        "class": "form-control", "placeholder": "Remark",
    }))
    class Meta:
        model = Customer
        fields = ['customer_code', 'customer_name', 'tax_code', 'customer_address', 'contact_no',
                  'channel', 'customer_type', 'sale_area', 'province', 'account_no_1',
                  'legal_name', 'legal_address', 'represented_by', 'phone', 'contact_person',
                  'fax', 'LoA', 'account_no_2', 'account_no_3', 'bank_name_1', 
                  'bank_name_2', 'bank_name_3', 'remark']
        

