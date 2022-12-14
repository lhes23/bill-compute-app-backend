from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('readings',ReadingViewSet)
router.register('tenants',TenantViewSet)
router.register('houses',HouseViewSet)
router.register('yearly-bills',YearlyBillViewSet)

urlpatterns = [
    path('tenants/active/', TenantViewSet.getActive),
    path('readings/active/', ReadingViewSet.getActiveReadings),
    path('houses/vacant/<int:id>', HouseViewSet.makeHouseVacant),
    path('', include(router.urls))
]