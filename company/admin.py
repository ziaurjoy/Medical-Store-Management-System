from django.contrib import admin

# Register your models here.
from company.models import *
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'address']
admin.site.register(Company,CompanyAdmin)
admin.site.register(CompanyAccount)
admin.site.register(CompanyBank)