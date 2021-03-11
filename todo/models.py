from django.db import models

# Create your models here.

class MainTodo(models.Model):
    sno = models.AutoField(primary_key=True)
    subject = models.CharField(max_length=50)
    contant = models.CharField(max_length=500)
    time = models.DateTimeField()

    def __str__(self):
        return self.subject
    
