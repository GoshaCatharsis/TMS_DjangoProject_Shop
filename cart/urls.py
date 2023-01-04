from django.urls import path
from .views import *


urlpatterns = [
    path('add/<int:id>/', CartView.as_view(), name='cart-add'),
]