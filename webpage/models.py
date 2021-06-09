from django.db import models


# Create your models here.
class Employee(models.Model):
    name= models.CharField(max_length=100,null=True)
    employee_id=models.CharField(max_length=20,null=True)
    desgination=models.CharField(max_length=50,null=True)
    date_of_joinig=models.CharField(max_length=30,null=True)
    owner = models.ForeignKey('auth.User', related_name='mukesh', on_delete=models.CASCADE,null=True)


    class Meta:
        db_table='employee'
