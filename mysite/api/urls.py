from django.urls import path
from . import views

urlpatterns = [
    path("vendors", views.api_Vendors, name="api_Vendors"),
    path("vendors/<str:pk>", views.api_Vendor, name="api_Vendor"),
    path("vendors/<str:pk>/performance", views.api_Vendor_performance, name="api_Vendor_performance"),
    path("purchase_orders", views.api_ProductOrders, name="api_PurchaseOrders"),
    path("purchase_orders/<str:pk>", views.api_ProductOrder, name="api_ProductOrder"),
    path('purchase_orders/<str:pk>/acknowledge', views.api_Acknowledge, name="api_Acknowledge"),
]