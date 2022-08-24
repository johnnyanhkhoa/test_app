from django.contrib import admin
from .models import *

admin.site.site_header = "Tedis - Sale Agreement"
# Register your models here.
admin.site.register(Quotation)
admin.site.register(Quotation_product)
admin.site.register(Status)
admin.site.register(Contract)
admin.site.register(contract_product)