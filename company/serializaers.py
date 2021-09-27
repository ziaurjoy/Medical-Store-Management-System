from django.db.models import fields
from django.db.models.fields.related import ForeignKey
from rest_framework import serializers

from company.models import Company, CompanyBank

class CompanySirializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'



class CompanyBankSirializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyBank
        fields = '__all__'

    # resutn company ForeignKey 
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySirializer(instance.company_id).data
        return response
