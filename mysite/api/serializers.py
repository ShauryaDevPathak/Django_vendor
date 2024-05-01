from rest_framework import serializers
from Vendor.models import Vendor, PurchaseOrder

# Convert python data into json
class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['name', 'contact_details', 'address', 'vendor_code']
        extra_kwargs = {
            "name":{"required": False}, 
            "contact_details":{"required": False}, 
            "address":{"required": False}, 
            "vendor_code":{"required": False}
        }

class VendorPerformaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate']

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrder
        fields = [
            'po_number', 'vendor', 
            'order_date', 'expected_delivery_date','actual_delivery_date', 
            'items', 'quantity', 'status', 
            'quality_rating', 'issue_date', 
            'acknowledgment_date'
        ]
        extra_kwargs = {
            'po_number':{"required": False}, 'vendor':{"required": False}, 
            'order_date':{"required": False}, 'expected_delivery_date':{"required": False},'actual_delivery_date':{"required": False}, 
            'items':{"required": False}, 'quantity':{"required": False}, 'status':{"required": False}, 
            'quality_rating':{"required": False}, 'issue_date':{"required": False}, 
            'acknowledgment_date':{"required": False}
        }