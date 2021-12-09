from django.db.models import fields
from rest_framework import serializers
from .models import *

class Key_Value_Pair_Serializer(serializers.ModelSerializer):           

    class Meta:
        model=Key_Value_pair
        fields=['Key', 'Value']