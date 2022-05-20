from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    objects = models.Manager()
 
    def getUsername(self):
        return self.username
 
    def getPassword(self):
        return self.password
 
    def __str__(self):
        return str(self.pk) + "Username: " + (self.username) + ", " + "Password: " + (self.password)