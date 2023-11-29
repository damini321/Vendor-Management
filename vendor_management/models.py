from django.db import models

# Create your models here.
class Vendor(models.Model):
    name = models.CharField(max_length=255)
    contact_details = models.CharField(max_length=255)
    address = models.TextField()
    vendor_code = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class PurchaseOrder(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    po_number = models.CharField(max_length=50)
    vendor_reference = models.CharField(max_length=100)
    order_date = models.DateField()
    items = models.TextField()
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.po_number