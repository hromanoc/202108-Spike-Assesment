from django.urls import path
from .views import calculateDistance

app_name = 'deliveryapp'

urlpatterns = [
    path('', calculateDistance, name='calculate-view'),
]