from django.db import models
import suppliers
from django.db import models
from django.utils import timezone
from datetime import datetime
now = datetime.now()
# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=300)
    address = models.CharField(max_length=300)
    phonenumber =  models.CharField(max_length=300)
    emailaddress = models.CharField(max_length=300)
    date = models.DateTimeField(default=now, editable=False)

    def getName(self):
        return self.name

    def getAddress(self):
        return self.address

    def getNumber(self):
        return self.phonenumber

    def getEmail(self):
        return self.emailaddress
        
    def __str__(self):
        return str(self.pk) + ": " + self.name + str(self.phonenumber) + ". " + self.address + ". " + self.emailaddress + "created at " + self.date