from django.db.models import Count
 
from django.db import models

# Create your models here.
#type of product 
class TypeOfProduct(models.Model):
    Id=models.IntegerField(primary_key=True,verbose_name='کد')
    Name=models.CharField(max_length=20,verbose_name='نوع')
    Parent=models.ForeignKey('self',on_delete=models.CASCADE,null=True,blank=True)
    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        verbose_name='نوع محصول'
        verbose_name_plural='انواع محصول'
        db_table='T_TypeOfProduct'
#Brand of product
class BrandOfProduct(models.Model):
    Id=models.IntegerField(primary_key=True,verbose_name='کد')
    Name=models.CharField(max_length=20,verbose_name='برند')
    
    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        verbose_name='برند'
        verbose_name_plural='برندها'
        db_table='T_Brand'

#abstract model for product
class abstractModel(models.Model):
    Name=models.CharField(max_length=20,verbose_name='نام محصول')
    Img=models.ImageField(upload_to='images/',verbose_name='عکس محصول',default='noimage.png')
    Price=models.IntegerField(verbose_name='قیمت')
    Type=models.ForeignKey(TypeOfProduct,on_delete=models.CASCADE,verbose_name='نوع',null=True)
    Brand=models.ForeignKey(BrandOfProduct,on_delete=models.CASCADE,verbose_name='برند',null=True)
    Description=models.TextField(verbose_name='توضیحات')
    Slug=models.SlugField()
    Is_Active=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='تاریخ بروزرسانی')
    
    class Meta:
        abstract = True
 
 
#property of Model
class Property(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name='کد')
    Name=models.CharField(max_length=20,verbose_name='نام ویژگی')  
    
    def __str__(self) -> str:
        return self.Name 
        
    class Meta:
        verbose_name=' ویژگی'
        verbose_name_plural='ویژگی ها'
        db_table='T_Property'
        
#product Model
class Product(abstractModel):
    property=models.ManyToManyField(Property,through='PropertiesOfProduct')
    
    def __str__(self) -> str:
        return self.Name
    
    class Meta:
        ordering=['-created_at','-updated_at']
        verbose_name=' محصول'
        verbose_name_plural='محصولات'
        db_table='T_Product'


class PropertiesOfProduct(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='نام کالا')
    property=models.ForeignKey(Property,on_delete=models.CASCADE,verbose_name='نام ویژگی')
    value=models.CharField(max_length=20,verbose_name='مقدار ویژگی')    
    
    def __str__(self) -> str:
        return self.value
    
    class Meta:
     
        verbose_name= 'ویژگی محصول'
        verbose_name_plural='ویژگی های محصولات'
        db_table='T_PropertiesOfProduct'