from django.urls import path
from numpy import product 
from .views import productDetail,products
urlpatterns = [
   path('productDetail/<str:pk>/',productDetail),
   path('products',products)
]
