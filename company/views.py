from copy import Error
from django.db.models.query import QuerySet
from django.shortcuts import render
from company.serializaers import CompanySirializer, CompanyBankSirializer
from company.models import Company, CompanyBank

from rest_framework import status
from rest_framework.generics import get_object_or_404, Http404
from rest_framework.response import Response
from rest_framework import serializers, viewsets
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.



class CompanyViewSet(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            queryset = Company.objects.all()
            serializer = CompanySirializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = CompanySirializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            get_company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySirializer(get_company)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            serializer = CompanySirializer(company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            company = get_object_or_404(queryset, pk=pk)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)





class CompanyBankViewSet(viewsets.ViewSet):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def create(self, request):
        try:
            serializer = CompanyBankSirializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def list(self, request):
        try:
            queryset = CompanyBank.objects.all()
            serializer = CompanyBankSirializer(queryset, many=True) 
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def retrieve(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            get_company_bank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSirializer(get_company_bank)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = CompanyBank.objects.all()
            get_company_bank = get_object_or_404(queryset, pk=pk)
            serializer = CompanyBankSirializer(get_company_bank, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

    
    def delete(self, request, pk=None):
        try:
            queryset = Company.objects.all()
            get_company_bank = get_object_or_404(queryset, pk=pk)
            get_company_bank.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_401_UNAUTHORIZED)



        



company_list = CompanyViewSet.as_view({'get': 'list'})
company_details = CompanyViewSet.as_view({'get': 'retrieve'})
company_create = CompanyViewSet.as_view({'post': 'create'})
company_update = CompanyViewSet.as_view({'put': 'update'})
company_delete = CompanyViewSet.as_view({'delete': 'delete'})



company_bank_list = CompanyBankViewSet.as_view({'get': 'list'})
company_bank_list = CompanyBankViewSet.as_view({'get': 'retrieve'})
company_bank_create = CompanyBankViewSet.as_view({'post': 'create'})
company_bank_update = CompanyBankViewSet.as_view({'put': 'update'})
    

    