from django.db import models
from .utils import password_hash

# Create your models here.
class User(models.Model):
    user_username=models.CharField(max_length=16,primary_key=True)
    user_type=models.CharField(max_length=16)
    user_first_name=models.CharField(max_length=16)
    user_last_name=models.CharField(max_length=16)
    user_email=models.CharField(max_length=32)
    user_password=models.CharField(max_length=64)

class Client(models.Model):
    client_id=models.CharField(max_length=16,primary_key=True)
    first_name=models.CharField(max_length=16)
    last_name=models.CharField(max_length=16)
    email=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=16)

class Appliance(models.Model):
    appliance_type=models.CharField(max_length=16)
    appliance_brand=models.CharField(max_length=16)
    appliance_model=models.CharField(max_length=16)
    appliance_sn=models.CharField(max_length=8)

class Ingress(models.Model):
    ingress_date=models.DateField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    appliance=models.ForeignKey(Appliance,on_delete=models.CASCADE)
    failure_description=models.CharField(max_length=256)
    inspection_status=models.CharField(max_length=128)
    accessories=models.CharField(max_length=128,null=True)
    diagnosis=models.CharField(max_length=128,null=True)
    technician=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    state=models.IntegerField()
    quotation=models.IntegerField()

class Ingress_Update(models.Model):
    update_date=models.DateField()
    update_state=models.IntegerField()
    ingress=models.ForeignKey(Ingress,on_delete=models.CASCADE)
    update_description=models.CharField(max_length=128)

class Component(models.Model):
    component_code=models.CharField(max_length=16,primary_key=True)
    component_qty=models.IntegerField()
    component_price=models.IntegerField()
    component_description=models.CharField(max_length=128)

class Used_Parts(models.Model):
    component_code=models.ForeignKey(Component,on_delete=models.CASCADE)
    qty=models.IntegerField()
    ingress=models.ForeignKey(Ingress,on_delete=models.CASCADE)

