from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Admin(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)
    image = models.ImageField(upload_to='static', null=True, blank=True)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    age = models.IntegerField
    phoneNumber = models.IntegerField
    date = models.DateField
    address = models.CharField

    class Meta:
        db_table = "Department"

class field(models.Model):
    username=models.CharField(max_length=200)
    emil=models.EmailField()
    password=models.CharField(max_length=200)

    class Meta:
        db_table = "field"

    def __init__(self, *args, **kwargs):
        super().__init__(args, kwargs)
        self.name = None

    def __str__(self):
        return self.name


