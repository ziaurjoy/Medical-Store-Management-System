from employee.serializers import EmployeeSalarySerializer, EmployeeSerializer, EmployeeBankSerializer
from django.shortcuts import render
from employee.models import Employee, EmployeeBank, EmployeeSalary

from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
# Create your views here.


class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
       try:
            queryset = Employee.objects.all()
            serializer = EmployeeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = EmployeeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            get_employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(get_employee)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            get_employee = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(get_employee, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Employee.objects.all()
            get_employee = get_object_or_404(queryset, pk=pk)
            get_employee.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)




class EmployeeSalaryViewSet(viewsets.ViewSet):
    def list(self, request):
       try:
            queryset = EmployeeSalary.objects.all()
            serializer = EmployeeSalarySerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = EmployeeSalarySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            get_employee_salary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(get_employee_salary)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            get_employee_salary = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeSerializer(get_employee_salary, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = EmployeeSalary.objects.all()
            get_employee_salary = get_object_or_404(queryset, pk=pk)
            get_employee_salary.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)




class EmployeeBankViewSet(viewsets.ViewSet):
    def list(self, request):
       try:
            queryset = EmployeeBank.objects.all()
            serializer = EmployeeBankSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = EmployeeBankSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            get_employee_bank = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializer(get_employee_bank)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            get_employee_bank = get_object_or_404(queryset, pk=pk)
            serializer = EmployeeBankSerializer(get_employee_bank, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = EmployeeBank.objects.all()
            get_employee_bank = get_object_or_404(queryset, pk=pk)
            get_employee_bank.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)





employee_list = EmployeeViewSet.as_view({'get': 'list'})
employee_details = EmployeeViewSet.as_view({'get': 'retrieve'})
employee_create = EmployeeViewSet.as_view({'post': 'create'})
employee_update = EmployeeViewSet.as_view({'put': 'update'})
employee_delete = EmployeeViewSet.as_view({'delete': 'delete'})



employee_salary_list = EmployeeSalaryViewSet.as_view({'get': 'list'})
employee_salary_details = EmployeeSalaryViewSet.as_view({'get': 'retrieve'})
employee_salary_create = EmployeeSalaryViewSet.as_view({'post': 'create'})
employee_salary_update = EmployeeSalaryViewSet.as_view({'put': 'update'})
employee_salary_delete = EmployeeSalaryViewSet.as_view({'delete': 'delete'})


employee_bank_list = EmployeeBankViewSet.as_view({'get': 'list'})
employee_bank_details = EmployeeBankViewSet.as_view({'get': 'retrieve'})
employee_bank_create = EmployeeBankViewSet.as_view({'post': 'create'})
employee_bank_update = EmployeeBankViewSet.as_view({'put': 'update'})
employee_bank_delete = EmployeeBankViewSet.as_view({'delete': 'delete'})