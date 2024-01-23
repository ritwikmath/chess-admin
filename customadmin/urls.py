from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name='dashboard'),
    path("customers", views.CustomersList.as_view(), name='customers'),
    path("api/customers", views.customerListApi, name='customersapi'),
]
