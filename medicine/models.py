from django.db import models

# Create your models here.
from company.models import Company


class Medicine(models.Model):
    name = models.CharField(max_length=100)
    medical_type = models.CharField(max_length=100)
    buy_price = models.CharField(max_length=10)
    sell_price = models.CharField(max_length=10)
    # Central Goods and Services Tax
    CGST = models.CharField(max_length=10)
    # State Goods and Services Tax
    SGST = models.CharField(max_length=10)
    batch_no = models.CharField(max_length=100)
    shelf_no = models.CharField(max_length=100)
    # medicine expiry date
    exp_date = models.DateField()
    # Manufacturing Date
    mfg = models.DateField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    description = models.TextField()
    in_stock = models.IntegerField()
    quantity_in_strip = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class MedicineDetails(models.Model):
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    salt_name = models.CharField(max_length=100)
    salt_quantity = models.CharField(max_length=100)
    salt_quantity_type = models.CharField(max_length=100)
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.medicine_id.name

