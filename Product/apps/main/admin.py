from django.contrib import admin
from .models import *
from django.utils.html import format_html
 
# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('Name','Img','Price','Type','Brand','Is_Active','created_at','updated_at',  'click_me')
    list_filter=('Is_Active','Brand','Type')
    prepopulated_fields={'Slug':('Name',)}
    change_list_template='admin/products/products_change_list.html'
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/product/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
   
    click_me.short_description=' ویرایش '
  
    def get_queryset(self,request):   
       return super().get_queryset(request).annotate(num_brand=Count('Brand')).filter(num_brand=10)
 
#----------------------------------------------------------------------------------      
@admin.register(TypeOfProduct)
class TypeOfProductAdmin(admin.ModelAdmin):
    list_display=('Name','Parent','click_me')
    list_filter=('Parent',)
    search_fields=['Name','Parent']
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/typeofproduct/{obj.Id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
   
    click_me.short_description=' ویرایش '
#--------------------------------------------------------------------------------------
@admin.register(BrandOfProduct)
class BrandOfProductAdmin(admin.ModelAdmin):
    list_display=('Id','Name','click_me' )
    search_fields=['Name']
    
    def click_me(self,obj):
       return format_html(f'<a href="/admin/main/brandofproduct/{obj.Id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
   
    click_me.short_description=' ویرایش '
    
#-------------------------------------------------------------------------------------- 
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display=('id','Name','click_me')
    list_filter=('Name',)
    search_fields=['Name']
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/property/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
   
    click_me.short_description=' ویرایش '
#---------------------------------------------------------------------------------------
@admin.register(PropertiesOfProduct)
class PropertiesOfProduct(admin.ModelAdmin):
    list_display=('product','property','value','click_me')
    list_filter=('product','property')
    search_fields=['product','property']
    
    def click_me(self,obj):
        return format_html(f'<a href="/admin/main/propertiesofproduct/{obj.id}/change/" class="default" style="color:rgb(26, 119, 159)">View</a>')
   
    click_me.short_description=' ویرایش '