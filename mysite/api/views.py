from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import VendorSerializer, PurchaseOrderSerializer, VendorPerformaceSerializer
from Vendor.models import Vendor, PurchaseOrder

# Create your views here.

# View all vendors and add new ones
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_Vendors(request):

    # Return all the vendors
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)

    # Add a new Vendor
    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# View, update and delete a specific vendor (through vendor id)
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_Vendor(request, pk):

    # Find the vendor with given id, if no vendor exist return an error
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # return details of the vendor
    if request.method == 'GET':
        vendor = get_object_or_404(Vendor, id=pk)
        vendor = Vendor.objects.get(id=pk)
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    
    # Update details of the vendor
    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete a Vendor
    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
# View Performace metrics of a vendor
@api_view(["GET"])
def api_Vendor_performance(request, pk):

    # Find the vendor with given id, if no vendor exist return an error
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # Return the metrics of the vendor
    if request.method == 'GET':
        vendor = get_object_or_404(Vendor, id=pk)
        vendor = Vendor.objects.get(id=pk)
        serializer = VendorPerformaceSerializer(vendor)
        return Response(serializer.data)



# View all the purchase orders and add new ones
@api_view(['GET', 'POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_ProductOrders(request):

    # Return all purchase order details
    if request.method == 'GET':
        purchase_orders = PurchaseOrder.objects.all()
        serializer = PurchaseOrderSerializer(purchase_orders, many=True)
        return Response(serializer.data)
    
    # Add a purchase order
    elif request.method == 'POST':
        serializer = PurchaseOrderSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View, update and delete a specific purchase order
@api_view(['GET', 'PUT', 'DELETE'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_ProductOrder(request, pk):

    # Find the order with given id, if no vendor exist return an error
    try:
        purchase_order = PurchaseOrder.objects.get(pk=pk)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    # return details of the order
    if request.method == 'GET':
        purchase_order = get_object_or_404(PurchaseOrder, id=pk)
        purchase_order = PurchaseOrder.objects.get(id=pk)
        serializer = PurchaseOrderSerializer(purchase_order)
        return Response(serializer.data)
    
    # Update details of the order
    elif request.method == 'PUT':
        serializer = PurchaseOrderSerializer(purchase_order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Delete details of the order
    elif request.method == 'DELETE':
        purchase_order.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# Api where the vendors can acknowledge POs
@api_view(["POST"])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def api_Acknowledge(request, pk):

    # Find the order with given id, if no vendor exist return an error
    try:
        purchase_order = PurchaseOrder.objects.get(pk=pk)
    except PurchaseOrder.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

    # Modify the acknowledgement date of the purchase order
    if request.method == "POST":
        purchase_order.acknowledgment_date = timezone.now()
        
        purchase_order.save()
        purchase_order.update_avg_response_time()
        return Response("Purchase order has been acknowledged")