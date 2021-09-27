from customer.serializers import CustomerBillSerializer, CustomerRequestSerializer, CustomerSerializer, CustomerBillDetailsSerializer
from customer.models import Bill, BillDetails, Customer, CustomerRequest
from django.shortcuts import render


from rest_framework.generics import get_object_or_404, Http404
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework import viewsets
# Create your views here.


class CustomerViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
       try:
            queryset = Customer.objects.all()
            serializer = CustomerSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = CustomerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(get_customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerSerializer(get_customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Customer.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            get_customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)





class CustomerBillViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
       try:
            queryset = Bill.objects.all()
            serializer = CustomerBillSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = CustomerBillSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            get_customer_bill = get_object_or_404(queryset, pk=pk)
            serializer = CustomerBillSerializer(get_customer_bill)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            get_customer_bill = get_object_or_404(queryset, pk=pk)
            serializer = CustomerBillSerializer(get_customer_bill, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            get_customer_bill = get_object_or_404(queryset, pk=pk)
            get_customer_bill.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)




class CustomerBillDetailsViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
       try:
            queryset = BillDetails.objects.all()
            serializer = CustomerBillDetailsSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = CustomerBillDetailsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            get_customer_bill_details = get_object_or_404(queryset, pk=pk)
            serializer = CustomerBillDetailsSerializer(get_customer_bill_details)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = BillDetails.objects.all()
            get_customer_bill_details = get_object_or_404(queryset, pk=pk)
            serializer = CustomerBillDetailsSerializer(get_customer_bill_details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Bill.objects.all()
            get_customer_bill_details = get_object_or_404(queryset, pk=pk)
            get_customer_bill_details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)





class CustomerRequestViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
       try:
            queryset = CustomerRequest.objects.all()
            serializer = CustomerRequestSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
       except:
           return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = CustomerRequestSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerRequestSerializer(get_customer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            serializer = CustomerRequestSerializer(get_customer, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = CustomerRequest.objects.all()
            get_customer = get_object_or_404(queryset, pk=pk)
            get_customer.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)



customer_list = CustomerViewSet.as_view({'get': 'list'})
customer_details = CustomerViewSet.as_view({'get': 'retrieve'})
customer_create = CustomerViewSet.as_view({'post': 'create'})
customer_update = CustomerViewSet.as_view({'put': 'update'})
customer_delete = CustomerViewSet.as_view({'delete': 'delete'})



customer_bill_list = CustomerBillViewSet.as_view({'get': 'list'})
customer_bill_details = CustomerBillViewSet.as_view({'get': 'retrieve'})
customer_bill_create = CustomerBillViewSet.as_view({'post': 'create'})
customer_bill_update = CustomerBillViewSet.as_view({'put': 'update'})
customer_bill_delete = CustomerBillViewSet.as_view({'delete': 'delete'})



customer_bill_details_list = CustomerBillDetailsViewSet.as_view({'get': 'list'})
customer_bill_detail_details = CustomerBillDetailsViewSet.as_view({'get': 'retrieve'})
customer_bill_details_create = CustomerBillDetailsViewSet.as_view({'post': 'create'})
customer_bill_details_update = CustomerBillDetailsViewSet.as_view({'put': 'update'})
customer_bill_details_delete = CustomerBillDetailsViewSet.as_view({'delete': 'delete'})



customer_request_list = CustomerRequestViewSet.as_view({'get': 'list'})
customer_request_details = CustomerRequestViewSet.as_view({'get': 'retrieve'})
customer_request_create = CustomerRequestViewSet.as_view({'post': 'create'})
customer_request_update = CustomerRequestViewSet.as_view({'put': 'update'})
customer_request_delete = CustomerRequestViewSet.as_view({'delete': 'delete'})