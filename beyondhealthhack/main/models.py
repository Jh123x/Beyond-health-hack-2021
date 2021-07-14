from django.db import models

# Create your models here.
class ContactUsForm(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=20)
    category = models.CharField(max_length=1)
    message = models.TextField(max_length=2000)


    def __str__(self):
        return f"{self.name}: {self.email}"