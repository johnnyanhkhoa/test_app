from django.db import models
from django.utils.timezone import now
from datetime import date, datetime

today = date.today()
# Create your models here.
class Product_category(models.Model):
    product_category_name = models.CharField(max_length=200)    # nếu return kh được thì để thêm blank=False
    product_category_remark = models.TextField()
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
        
    def __str__(self):
        return self.product_category_name   # nếu return kh được thì để thêm blank=False
    

class Product_brand(models.Model):
    product_brand_name = models.CharField(max_length=200)
    product_brand_remark = models.TextField(blank=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.product_brand_name
    

class Product(models.Model):
    product_category = models.ForeignKey(Product_category, on_delete=models.PROTECT, null=True)
    product_brand = models.ForeignKey(Product_brand, on_delete=models.PROTECT, null=True)
    product_code = models.CharField(max_length=20, null=True)
    product_name = models.CharField(max_length=200, null=True)
    product_name_on_registration_document = models.CharField(max_length=200, null=True)
    product_unit = models.CharField(max_length=20, null=True)
    packing_size = models.CharField(max_length=100, null=True)
    vat = models.CharField(max_length=10, null=True)
    retail_selling_price_wo_vat = models.IntegerField(null=True)
    retail_selling_price_vat = models.IntegerField(null=True)
    selling_price_distributor_wo_vat = models.IntegerField(null=True)
    selling_price_distributor_vat = models.IntegerField(null=True)
    selling_price_etc_wo_vat = models.IntegerField(null=True)
    selling_price_etc_vat = models.IntegerField(null=True)
    selling_price_otc_wo_vat = models.IntegerField(null=True)
    selling_price_otc_vat = models.IntegerField(null=True)
    registraion_approval_date = models.CharField(max_length=50, null=True)
    registraion_expiry_date = models.CharField(max_length=50, null=True)
    registraion_reference = models.CharField(max_length=50, null=True)
    manufacture = models.CharField(max_length=200, null=True)
    manufacturing_country = models.CharField(max_length=50, null=True)
    intended_use = models.CharField(max_length=500, null=True)
    product_type = models.CharField(max_length=500, null=True)
    ingredient_list = models.CharField(max_length=500, null=True)
    expiry_date = models.IntegerField(null=True)
    product_remark = models.TextField(null=True)
    created_by = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.product_name


class Sale_area(models.Model):
    sale_area_code = models.CharField(max_length=200)   # nếu return kh được thì để thêm blank=False
    sale_area_name = models.CharField(max_length=200)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.sale_area_code


class Province(models.Model):
    sale_area = models.ForeignKey(Sale_area, on_delete=models.PROTECT)
    province_code = models.CharField(max_length=200)    # nếu return kh được thì để thêm blank=False
    province_name = models.CharField(max_length=200)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.province_code


class Customer_type(models.Model):
    customer_type_abbrev = models.CharField(max_length=10)
    customer_type_name = models.CharField(max_length=100)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.customer_type_abbrev
    
    
class Channel(models.Model):
    channel_name = models.CharField(max_length=10)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.channel_name    
    

class Customer(models.Model):
    customer_code = models.CharField(max_length=50, null=True)
    customer_name = models.CharField(max_length=200, null=True)
    tax_code = models.CharField(max_length=100, null=True)
    customer_address = models.CharField(max_length=500, null=True)   
    contact_no = models.CharField(max_length=50, null=True)
    channel =  models.ForeignKey(Channel, on_delete=models.PROTECT, null=True)
    customer_type = models.ForeignKey(Customer_type, on_delete=models.PROTECT, null=True)
    phone = models.CharField(max_length=50, null=True) 
    contact_person = models.CharField(max_length=100, null=True)
    fax = models.CharField(max_length=50, null=True) 
    LoA = models.CharField(max_length=200, null=True)
    sale_area =  models.ForeignKey(Sale_area, on_delete=models.PROTECT, null=True)
    province =  models.ForeignKey(Province, on_delete=models.PROTECT, null=True)
    legal_name = models.CharField(max_length=200, null=True)
    legal_address = models.CharField(max_length=500, null=True)   
    represented_by = models.CharField(max_length=300, null=True)
    account_no_1 = models.CharField(max_length=100, null=True)
    account_no_2 = models.CharField(max_length=100, null=True)
    account_no_3 = models.CharField(max_length=100, null=True)
    bank_name_1 = models.CharField(max_length=100, null=True)
    bank_name_2 = models.CharField(max_length=100, null=True)
    bank_name_3 = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=500, null=True)
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    

    def __str__(self):
        return self.customer_name
    

class Log_product_price(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.PROTECT)
    channel = models.CharField(max_length=50)  # làm thêm các choice để chọn channel như ENUM
    old_price = models.IntegerField()
    new_price = models.IntegerField()
    price_log_remark = models.TextField()
    created_by = models.IntegerField(null=True)
    created_at = models.DateTimeField(null=True, default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    deleted_by = models.IntegerField(null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.new_price


    
