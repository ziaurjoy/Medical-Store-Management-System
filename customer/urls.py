from django.urls import path, include


from customer.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', CustomerViewSet, basename='customer-list')
router.register(r'bill/list', CustomerBillViewSet, basename='customer-bill-list')
router.register(r'bill/details', CustomerBillDetailsViewSet, basename='customer-bill-details')
router.register(r'request', CustomerRequestViewSet, basename='customer-request')

urlpatterns = router.urls

