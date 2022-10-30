from django.db import models
from .utils import password_hash

# Create your models here.
class User(models.Model):
    user_type=models.CharField(max_length=16)
    user_username=models.CharField(max_length=16)
    user_first_name=models.CharField(max_length=16)
    user_last_name=models.CharField(max_length=16)
    user_password=models.CharField(max_length=64)

class Client(models.Model):
    client_id=models.CharField(max_length=16)
    first_name=models.CharField(max_length=16)
    last_name=models.CharField(max_length=16)
    email=models.CharField(max_length=32)
    phone_number=models.CharField(max_length=16)

class Appliance(models.Model):
    appliance_type=models.CharField(max_length=16)
    appliance_brand=models.CharField(max_length=16)
    appliance_model=models.CharField(max_length=16)
    appliance_sn=models.CharField(max_length=8)

class Accessory(models.Model):
    accessory_type=models.CharField(max_length=16)
    appliance=models.ForeignKey(Appliance,on_delete=models.CASCADE)

class Ingress(models.Model):
    ingress_date=models.DateField()
    client=models.ForeignKey(Client,on_delete=models.CASCADE)
    appliance=models.ForeignKey(Appliance,on_delete=models.CASCADE)
    technician=models.ForeignKey(User,on_delete=models.CASCADE)
    state=models.IntegerField()
    quotation=models.IntegerField()

class Ingress_Update(models.Model):
    update_date=models.DateField()
    update_state=models.IntegerField()
    ingress=models.ForeignKey(Ingress,on_delete=models.CASCADE)
    

