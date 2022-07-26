"""pets_hospital URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .router import router
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from pets import viewsets



schema_view = get_schema_view(
   openapi.Info(
      title="Pets_API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('pets/', include(router.urls)),
    path('pets/appointmentforday/<date>/', viewsets.AppointmentsForDayViewSet.as_view({'get': 'list'})),
    path('pets/unpaid-amount-sum/', viewsets.UnpaidAmountSumViewSet.as_view({'get': 'list'})),
    path('pets/total-amount-sum/', viewsets.TotalAmountSumViewSet.as_view({'get': 'list'})),
    path('pets/get-sum-of-pet-types/', viewsets.GetSumOfPetTypesViewSet.as_view({'get': 'list'})),
    path('pets/popular-pet-type/', viewsets.GetPopularPetTypeViewSet.as_view({'get': 'list'})),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]