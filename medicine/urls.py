from django.urls import path, include


from medicine.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', MedicineViewSet, basename='medicine-list')
router.register(r'details/list', MedicineDetailViewSet, basename='medicine-details-list')


urlpatterns = router.urls