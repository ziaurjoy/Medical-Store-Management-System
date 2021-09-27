from django.db import models

# Create your models here.
from medicine.models import Medicine


class Customer(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class Bill(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete= models.CASCADE)
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.customer_id.name



class BillDetails(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.bill_id.customer_id.name



class CustomerRequest(models.Model):
    name = models.CharField(max_length=100)
    phone = models.IntegerField()
    medicine_details = models.TextField()
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    





















