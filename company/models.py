from django.db import models
from django.db.models.enums import Choices

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=100)
    license_id = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    email = models.EmailField()
    description = models.TextField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class CompanyAccount(models.Model):
    transaction_type_choise = (
        ('banking', 'Banking'),
        ('hand cash', 'Hand Cash')
    )
    payment_mode_choise = (
        ('bikash', 'Bikash'),
        ('nagat', 'Nagat'),
        ('islamic', 'Islamic Bank'),
        ('hand cash', 'Hand Cash')
    )
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)
    transaction_type = models.CharField(choices=transaction_type_choise, max_length=100)
    transaction_amount = models.CharField(max_length=10)
    transaction_data = models.DateTimeField(auto_now_add=True)
    payment_mode = models.CharField(choices=payment_mode_choise, max_length=100)

    def __str__(self):
        return self.company_id.name


class CompanyBank(models.Model):
    bank_account_no = models.CharField(max_length=30)
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return self.company_id.name