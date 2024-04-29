from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.db.models import Avg
from .models import PurchaseOrder, Vendor
from django.db import models

@receiver(post_save, sender=PurchaseOrder)
def update_metrics_on_purchase_order_save(sender, instance, created, **kwargs):
    if not created:
        vendor = instance.vendor

        # On-Time Delivery Rate
        if instance.status == 'completed' and instance.delivery_date <= instance.delivery_date:
            completed_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()
            vendor.on_time_delivery_rate = completed_pos / PurchaseOrder.objects.filter(vendor=vendor, status='completed').count()

        # Quality Rating Average
        if instance.quality_rating:
            quality_rating_avg = PurchaseOrder.objects.filter(vendor=vendor, quality_rating__isnull=False).aggregate(Avg('quality_rating'))['quality_rating__avg']
            vendor.quality_rating_avg = quality_rating_avg

        # Fulfillment Rate
        fulfilled_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
        total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
        vendor.fulfillment_rate = fulfilled_pos.count() / total_pos if total_pos != 0 else 0

        vendor.save()

@receiver(pre_delete, sender=PurchaseOrder)
def update_metrics_on_purchase_order_delete(sender, instance, **kwargs):
    vendor = instance.vendor

    # Fulfillment Rate
    fulfilled_pos = PurchaseOrder.objects.filter(vendor=vendor, status='completed')
    total_pos = PurchaseOrder.objects.filter(vendor=vendor).count()
    vendor.fulfillment_rate = fulfilled_pos.count() / total_pos if total_pos != 0 else 0

    vendor.save()

