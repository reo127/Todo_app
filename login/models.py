from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,)
    email = models.CharField(max_length=30)
    contact = models.CharField(max_length=400)
    timestamp = models.DateTimeField(blank=True)

    def __str__(self):
        return self.name
