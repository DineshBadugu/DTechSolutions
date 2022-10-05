from django.db import models


# Create your models here.

class ContactForm(models.Model):
            Name=models.CharField(max_length=100)
            Email=models.EmailField()
            Subject = models.CharField(max_length=50)
            Message = models.CharField(max_length=500)
            def __str__(self):
                return self.Name