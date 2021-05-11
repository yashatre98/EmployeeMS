from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField
    email=models.CharField(max_length=50)
    gender=models.CharField(max_length=1)
    mob=models.CharField(max_length=10)
    def __str__(self):
        return self.name