from django.db import models

# Create your models here.


class Employee(models.Model):
    name = models.CharField(max_length=50)
    joining_data = models.DateField()
    phone = models.IntegerField()
    address = models.CharField(max_length=100)
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name



class EmployeeSalary(models.Model):
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary_data = models.DateField()
    salary_amount = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee_id.name



class EmployeeBank(models.Model):
    bank_account_no = models.CharField(max_length=30)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.employee_id.name


















