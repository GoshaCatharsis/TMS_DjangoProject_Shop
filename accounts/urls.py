from django.urls import path, include
from .views import Registration


urlpatterns = [
    path('account-registration/', Registration.as_view(), name='account-registration')
]
