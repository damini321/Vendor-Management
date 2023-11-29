from django.db import models
from django.db.models import Avg, Count
from django.utils import timezone
from .models import Vendor, PurchaseOrder

def calculate_vendor_metrics(vendor):
    completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')

    # On-Time Delivery Rate
    on_time_delivery_count = completed_pos.filter(delivery_date__lte=timezone.now()).count()
    vendor.on_time_delivery_rate = (on_time_delivery_count / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    # Quality Rating Average
    vendor.quality_rating_avg = completed_pos.filter(quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0.0

    # Average Response Time
    response_times = completed_pos.filter(acknowledgment_date__isnull=False).annotate(
        response_time=models.F('acknowledgment_date') - models.F('issue_date')
    ).aggregate(Avg('response_time'))['response_time__avg']
    vendor.average_response_time = response_times.total_seconds() / 60 if response_times else 0.0

    # Fulfillment Rate
    fulfilled_pos = completed_pos.filter(status='completed', acknowledgment_date__isnull=False)
    vendor.fulfillment_rate = (fulfilled_pos.count() / completed_pos.count()) * 100 if completed_pos.count() > 0 else 0

    vendor.save()
