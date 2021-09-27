
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('medicine/', include('medicine.urls')),
    path('customer/', include('customer.urls')),
    path('employee/', include('employee.urls')),

    # token create and refresh url
    path('create/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
