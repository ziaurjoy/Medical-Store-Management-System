

from django.db.models import fields
from employee.models import Employee, EmployeeBank, EmployeeSalary

from rest_framework import serializers


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'



class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeSalary
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response
    


class EmployeeBankSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeBank
        fields = '__all__'
    
    def to_representation(self, instance):
        response = super().to_representation(instance)
        response['employee'] = EmployeeSerializer(instance.employee_id).data
        return response



