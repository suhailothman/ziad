from django.db import models
from django.contrib.auth.models import User

class PharmacyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pharmacy_name = models.CharField("اسم الصيدلية", max_length=255)
    location = models.CharField("الموقع", max_length=255)
    manager_phone = models.CharField("رقم المدير", max_length=20)

class InventoryItem(models.Model):
    batch_number = models.CharField("رقم المخزون", max_length=50)
    name = models.CharField("اسم الصنف", max_length=255)
    expiry = models.DateField("تاريخ الانتهاء")
    price = models.DecimalField("السعر", max_digits=10, decimal_places=2)

class Order(models.Model):
    pharmacy = models.ForeignKey(PharmacyProfile, on_delete=models.CASCADE)
    order_details = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
