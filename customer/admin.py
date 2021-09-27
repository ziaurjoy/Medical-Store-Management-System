from django.contrib import admin

# Register your models here.
from customer.models import *

admin.site.register(Customer)
admin.site.register(Bill)
admin.site.register(BillDetails)
admin.site.register(CustomerRequest)
