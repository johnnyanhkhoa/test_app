from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Quotation)
admin.site.register(Quotation_product)
admin.site.register(Status)
admin.site.register(Contract)
admin.site.register(contract_product)