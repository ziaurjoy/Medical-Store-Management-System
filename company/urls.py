from django.urls import path, include


from company.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', CompanyViewSet, basename='company')
router.register(r'bank', CompanyBankViewSet, basename='bank')


urlpatterns = router.urls

