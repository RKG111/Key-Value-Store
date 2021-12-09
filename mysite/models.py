from django.db import models
from django.db.models.expressions import Value

class Key_Value_pair(models.Model):
    Key=models.CharField( max_length=100)
    Value=models.CharField(max_length=100)
