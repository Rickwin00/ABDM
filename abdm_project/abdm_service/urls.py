from django.urls import path
from abdm_service.views import ABHARequestOTPView, HealthView



urlpatterns = [
    path("health/", HealthView.as_view(), name="health"),
    path("abha-request-otp/", ABHARequestOTPView.as_view(), name="abha-request-otp")
]