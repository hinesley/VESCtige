from django.urls import path
from . import views

urlpatterns = [
    path('', views.RideListCreateAPIView.as_view(), name='api-rides-list'),
]
