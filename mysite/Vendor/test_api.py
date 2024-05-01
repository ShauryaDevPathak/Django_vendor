import json
import datetime, pytz
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone

from Vendor.models import Vendor, PurchaseOrder
from api.serializers import VendorSerializer, VendorPerformaceSerializer, PurchaseOrderSerializer

client = Client()

class GetAllVendorsTest(TestCase):
    """Test module for api_Vendors API"""
    # setting up the database
    def setUp(self):
        Vendor.objects.create(
            name="Vendor one", 
            contact_details="123456789", 
            address = "123 Test Street", 
            vendor_code="vendor123"
        )
        Vendor.objects.create(
            name="Vendor Two", 
            contact_details="987654321", 
            address = "456 Main Street", 
            vendor_code="vendor234"
        )
    
    def test_get_all_Vendors(self):
        # get API response
        response = client.get(reverse("api_Vendors"))
        #get data from db
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetSingleVendorTest(TestCase):
    """Test module for api_Vendor API"""
    # setting up the database
    def setUp(self):
        self.v1 = Vendor.objects.create(
            name="Vendor one",
            contact_details="123456789", 
            address = "123 Test Street", 
            vendor_code="vendor123"
        )
        self.v2 = Vendor.objects.create(
            name="Vendor Two", 
            contact_details="987654321", 
            address = "456 Main Street", 
            vendor_code="vendor234"
        )
    
    def test_get_valid_single_Vendor(self):
        # get API response
        response = client.get(reverse("api_Vendor", kwargs={'pk': self.v1.pk}))
        #get data from db
        vendor = Vendor.objects.get(pk=self.v1.pk)
        serializer = VendorSerializer(vendor)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAllPurchaseOrdersTest(TestCase):
    """Test module for api_PurchaseOrders API"""
    # setting up the database
    def setUp(self):
        self.v1 = Vendor.objects.create(
            name="Vendor one",
            contact_details="123456789", 
            address = "123 Test Street", 
            vendor_code="vendor123"
        )
        self.v2 = Vendor.objects.create(
            name="Vendor Two", 
            contact_details="987654321", 
            address = "456 Main Street", 
            vendor_code="vendor234"
        )

        self.p1 = PurchaseOrder.objects.create(
            po_number = "Pro 1",
            vendor = self.v1,
            order_date = "2024-04-30T10:00:00Z",
            delivery_date = "2024-05-01T11:00:00Z",
            items = json.loads('{"Chocolate": "crunchy"}'),
            quantity = 1,
            status = "",
            quality_rating = 4.4,
            issue_date = "2024-04-30T10:00:00Z",
        )
    
    def test_get_all_Vendors(self):
        # get API response
        response = client.get(reverse("api_PurchaseOrders"))
        #get data from db
        vendors = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(vendors, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)