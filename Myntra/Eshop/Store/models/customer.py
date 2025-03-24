from django.db import models

class Customer(models.Model):
    FirstName=models.CharField(max_length=50)
    LastName=models.CharField(max_length=25)
    Mobno=models.CharField(max_length=15)
    Emailid=models.EmailField()
    Password=models.CharField(max_length=500)
    
  
    
    def register(self):
        self.save()

    