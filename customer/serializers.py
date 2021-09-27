

from django.db import models
from django.db.models import fields
from medicine.serializers import MedicineSerializer
from customer.models import *


from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'



class CustomerBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['customer'] = CustomerSerializer(instance.customer_id).data
        return response



class CustomerBillDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillDetails
        fields = '__all__'

    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['bill'] = CustomerBillSerializer(instance.bill_id).data
        response['medicine'] = MedicineSerializer(instance.medicine_id).data
        return response
    


class CustomerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerRequest
        fields = '__all__'