from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
import sys
sys.path.append('C:/Users/ajsha/Desktop/backend/pro/users')
from users .models import User


# Create your views here.

def catalog(request):
    context = {
        'title' : 'StoreApp',
        'products' : Product.objects.all(),
        'categories' : ProductCategory.objects.all()

    }
    return render(request, 'products/catalog.html', context)

def index(request):
    context = {
        'title': 'storeApp',
        'username' : 'Aisha Ait',
        'is_promotion' : False
    }
    return render(request, 'products/index.html', context)

def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
