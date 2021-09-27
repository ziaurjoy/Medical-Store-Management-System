
from company.serializaers import CompanySirializer
from re import M
from django.db.models import fields
from rest_framework import serializers
from medicine.models import Medicine, MedicineDetails

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = CompanySirializer(instance.company_id).data
        return response


class MedicineDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicineDetails
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['company'] = MedicineSerializer(instance.medicine_id).data
        return response