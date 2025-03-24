from django.contrib import admin
from.models.product import Product
from .models.category import Category
from.models.customer import Customer

class Product_display(admin.ModelAdmin):
    list_display=('name','price','category')
    
class Category_display(admin.ModelAdmin): #to view name peice and decription of thr product
    list_display=('name',)

# Register your models here.
admin.site.register(Product,Product_display)  #to view it in admin page have to reguster here
admin.site.register(Category,Category_display)
admin.site.register(Customer)
