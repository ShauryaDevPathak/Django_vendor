from django.db import models
from django.db.models import Avg, Count
from django.utils import timezone
from datetime import datetime
# Create your models here.

# Model for the vendor details
class Vendor(models.Model):
    name = models.CharField(max_length=100)
    contact_details = models.CharField(max_length=100)
    address = models.TextField()
    vendor_code = models.CharField(max_length=20, unique=True)
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField(default=0)
    average_response_time = models.FloatField(default=0)
    fulfillment_rate = models.FloatField(default=0)    
    
    def update_performance_metrics(self):
        # finding rows with status=completed and belonging to our vendor
        completed_pos = PurchaseOrder.objects.filter(vendor=self, status='completed')

        # finding rows with belonging to our vendor          
        pos = PurchaseOrder.objects.filter(vendor=self)

        # calculate total number of completed purchase orders                                            
        total_completed_pos = completed_pos.count()
        
        # calculate total number of purchase orders
        total_pos = pos.count()                                                                     

        # On-Time Delivery Rate calculation
        on_time_deliveries = completed_pos.filter(actual_delivery_date__lte=models.F('expected_delivery_date')).count()
        self.on_time_delivery_rate = (on_time_deliveries / total_completed_pos) * 100 if total_completed_pos > 0 else 0

        # Quality Rating Average calculation
        quality_ratings = completed_pos.exclude(quality_rating__isnull=True).aggregate(avg_rating=models.Avg('quality_rating'))
        self.quality_rating_avg = quality_ratings['avg_rating'] if quality_ratings['avg_rating'] else 0

        # Fulfilment Rate calculation
        self.fulfillment_rate = (total_completed_pos/total_pos) * 100 if total_completed_pos > 0 else 0

        self.save()

    def update_avg_response_time(self):
        completed_pos = PurchaseOrder.objects.filter(vendor=self, status='completed')

        # Average Response Time calculation
        response_times = completed_pos.exclude(acknowledgment_date__isnull=True).aggregate(avg_response=models.Avg(models.F('acknowledgment_date') - models.F('issue_date')))
        self.average_response_time = response_times['avg_response'].total_seconds()/60 if response_times['avg_response'] else 0
        self.save()


    def __str__(self):
        return self.name
    
    def get_Vendor(self):           # Used for model testing purposes
        return self.name + " " + self.contact_details + " " + self.address + " " + self.vendor_code


# Model for the Order details
class PurchaseOrder(models.Model):
    po_number = models.CharField(max_length=100, unique=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    actual_delivery_date = models.DateTimeField(null=True, blank=True)
    expected_delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length=50, default='pending')
    quality_rating = models.FloatField(null=True, blank=True)
    issue_date = models.DateTimeField()
    acknowledgment_date = models.DateTimeField(null=True, blank=True)
    
    def update_avg_response_time(self):
        self.vendor.update_avg_response_time()              # To updat average response time of the vendor
        self.save()
    
    def save(self, *args, **kwargs):
        if self.status == 'completed':                      
            self.actual_delivery_date = datetime.now()      # To update actual delivery time in PurchaseOrder
            self.vendor.update_performance_metrics()        # To update all the performance metrics of the vendor

        super().save(*args, **kwargs)
            
            
    def __str__(self):
        return self.po_number


# Model to keep track of the History of the performace of vendors
class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

    def save(self, *args, **kwargs):
        self.date = datetime.now()
        self.on_time_delivery_rate = self.vendor.on_time_delivery_rate
        self.quality_rating_avg = self.vendor.quality_rating_avg
        self.average_response_time = self.vendor.average_response_time
        self.fulfillment_rate = self.vendor.fulfillment_rate
        super().save(*args, **kwargs)