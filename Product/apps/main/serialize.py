from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
 
from .models import Product
#models for serialize
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'