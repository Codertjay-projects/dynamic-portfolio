from django.db import models

# Create your models here.
from users.models import User


class Resume(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    start_date = models.CharField(max_length=10)
    end_date = models.CharField(max_length=10)
    detail = models.CharField(max_length=200)

