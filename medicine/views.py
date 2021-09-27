from medicine.models import Medicine, MedicineDetails
from django.db.models import fields
from django.shortcuts import render
from medicine.serializers import MedicineDetailSerializer, MedicineSerializer
from medicine.models import Medicine

from rest_framework.generics import get_object_or_404, Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
# Create your views here.


class MedicineViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            queryset = Medicine.objects.all()
            serializer = MedicineSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = MedicineSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            get_medicine = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(get_medicine)
            return Response(serializer.data, status=status.HTTP_401_UNAUTHORIZED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            get_medicine = get_object_or_404(queryset, pk=pk)
            serializer = MedicineSerializer(get_medicine, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = Medicine.objects.all()
            get_medicine = get_object_or_404(queryset, pk=pk)
            get_medicine.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)
    



class MedicineDetailViewSet(viewsets.ViewSet):

    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    def list(self, request):
        try:
            queryset = MedicineDetails.objects.all()
            serializer = MedicineDetailSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


    def create(self, request):
        try:
            serializer = MedicineDetailSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
  

    def retrieve(self, request, pk=None):
        try:
            queryset = MedicineDetails.objects.all()
            get_medicine_details = get_object_or_404(queryset, pk=pk)
            serializer = MedicineDetailSerializer(get_medicine_details)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    

    def update(self, request, pk=None):
        try:
            queryset = MedicineDetails.objects.all()
            get_medicine_details = get_object_or_404(queryset, pk=pk)
            serializer = MedicineDetailSerializer(get_medicine_details, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
 
    
    def delete(self, request, pk=None):
        try:
            queryset = MedicineDetails.objects.all()
            get_medicine_details = get_object_or_404(queryset, pk=pk)
            get_medicine_details.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except AttributeError:
            return Response(status=status.HTTP_204_NO_CONTENT)


medicine_list = MedicineViewSet.as_view({'get': 'list'})
medicine_details = MedicineViewSet.as_view({'get': 'retrieve'})
medicine_create = MedicineViewSet.as_view({'post': 'create'})
medicine_update = MedicineViewSet.as_view({'put': 'update'})
medicine_delete = MedicineViewSet.as_view({'delete': 'delete'})



medicine_details_list = MedicineDetailViewSet.as_view({'get': 'list'})
medicine_full_details = MedicineDetailViewSet.as_view({'get': 'retrieve'})
medicine_details_create = MedicineDetailViewSet.as_view({'post': 'create'})
medicine_details_update = MedicineDetailViewSet.as_view({'put': 'update'})
medicine_details_delete = MedicineDetailViewSet.as_view({'delete': 'delete'})