from django.urls import path, include


from employee.views import EmployeeViewSet, EmployeeSalaryViewSet, EmployeeBankViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'list', EmployeeViewSet, basename='employee-list')
router.register(r'salary/list', EmployeeSalaryViewSet, basename='employee-salary-list')
router.register(r'bank/list', EmployeeBankViewSet, basename='employee-bank-list')



urlpatterns = router.urls