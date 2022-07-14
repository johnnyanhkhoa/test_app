from pyexpat import model
from django.db import models
from sale_management.models import *
from datetime import date, datetime
from django.utils.timezone import now


today = date.today()

# Create your models here.
class Status(models.Model):
    status = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.status
    
    
class Quotation(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, null=True)
    quotation_no = models.CharField(max_length=50, null=True)
    quotation_date = models.DateField(null=True, default=today)
    quotation_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    status_date = models.DateField(null=True, default=today)
    quotation_remark = models.CharField(max_length=500, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
            return self.quotation_no


class Quotation_product(models.Model):
    quotation_id = models.ForeignKey(Quotation, on_delete=models.PROTECT, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    unit_price_vat = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return self.quotation_id
    

class Contract(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT, null=True)
    channel = models.ForeignKey(Channel, on_delete=models.PROTECT, null=True)
    contract_no = models.CharField(max_length=50, null=True)
    contract_date = models.DateField(null=True, default=today)
    valid_from_date = models.DateField(null=True, default=today)
    valid_to_date = models.DateField(null=True, default=today)
    contract_status = models.ForeignKey(Status, on_delete=models.PROTECT, null=True)
    status_date = models.DateField(null=True, default=today)
    placement_time_in_prior_to_delivery = models.IntegerField(null=True) 
    delivery_time = models.DateTimeField(null=True, default=now)
    registration_document = models.CharField(max_length=100, null=True)
    payment_method = models.CharField(max_length=100, null=True)
    payment_due = models.IntegerField(null=True)
    penalty_rate_for_late_payment = models.IntegerField(null=True)
    bank_charges_related_to_payment = models.IntegerField(null=True)
    delivery_point = models.CharField(max_length=500, null=True)
    enquiry_for_goods_receipt = models.CharField(max_length=500, null=True)
    enquiry_for_goods_return = models.CharField(max_length=500, null=True)
    documents_to_be_delivered_with_each_delivery = models.CharField(max_length=500, null=True)
    complaint_time_due_to_product_issue = models.IntegerField(null=True)
    compensation_time = models.IntegerField(null=True)
    support_fee_on_target_achivement = models.IntegerField(null=True)
    support_fee_on_transportation = models.IntegerField(null=True)
    support_fee_for_payment_due_date = models.IntegerField(null=True)
    support_fee_for_new_pos = models.IntegerField(null=True)
    support_fee_for_display = models.IntegerField(null=True)
    support_fee_for_listing = models.IntegerField(null=True)
    support_fee_for_advertising_and_birthday = models.IntegerField(null=True)
    support_fee_for_product_creation = models.IntegerField(null=True)
    method_of_support_fee_payment = models.CharField(max_length=100, null=True)
    penalty_for_agreement_breach = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __int__(self):
        return self.contract_no
    

class contract_product(models.Model):
    contract_id = models.ForeignKey(Contract, on_delete=models.PROTECT, null=True)
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT, null=True)
    unit_price_vat = models.IntegerField(null=True)
    quantity = models.IntegerField(null=True)
    total_amount = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __int__(self):
        return self.contract_id