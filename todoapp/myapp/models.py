from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
