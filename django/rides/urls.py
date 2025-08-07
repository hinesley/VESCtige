from django.urls import path
from . import views

urlpatterns = [
    path('', views.RideListCreateView.as_view(), name='rides-list'),
]
