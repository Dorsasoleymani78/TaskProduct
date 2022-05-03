from math import fabs
from django.shortcuts import render
from .serialize import ProductSerializer
# Create your views here.
from rest_framework .decorators import api_view
from .models import Product
from rest_framework.response import Response

#show product according to Id
@api_view(['Get'])
def productDetail(request,pk):
    products=Product.objects.get(id=pk)
    serializer=ProductSerializer(products,many=False)
    return Response(serializer.data)

#show all products
@api_view(['Get'])
def products(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)