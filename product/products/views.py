from django.shortcuts import render

# Create your views here.

from rest_framework import generics
from .models import Product
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AllProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer