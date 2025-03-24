from django.db import models
from.category import Category

class Product(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    price=models.DecimalField(max_digits=10,decimal_places=2)
    image=models.ImageField(upload_to='upload/products/')
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1) # map caegory in product to delete and easya accesible for user
    
    def __str__(self):
        return self.name
    
    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoriesid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()