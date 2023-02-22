from django.db import models
import sys
sys.path.append('C:/Users/ajsha/Desktop/backend/pro/users')
from users .models import User

class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True)
    desc = models.TextField(null=True, blank=True)
    def __str__(self) -> str:
        return self.name

    def __repr__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=256)
    desc = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    image = models.ImageField(upload_to='prroducts_image')
    category = models.ForeignKey(to=ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name 
    def __repr__(self) -> str:
        return self.name


class Basket(models.Model) :
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    products = models.ForeignKey(to=Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) :
        return f"Корзина товаров для {self.user.username}"