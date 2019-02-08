from django.db import models

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, default='')
    phone_no = models.CharField(max_length=15)
    address = models.TextField(default='')
    email = models.EmailField(default='') 


