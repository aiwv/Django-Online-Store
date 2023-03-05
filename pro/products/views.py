from django.shortcuts import render, HttpResponseRedirect
from .models import Product, ProductCategory, Basket
import sys
sys.path.append('C:/Users/ajsha/Desktop/backend/pro/users')
from users .models import User
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator

# Create your views here.

def catalog(request, category_id = None):
    if category_id:
        category = ProductCategory.objects.get(id = category_id)
        products = Product.objects.filter(category = category)

    else:
        products = Product.objects.all()
    
    p = Paginator(products, 2)
    page = request.GET.get('page')
    products = p.get_page(page)
    max_pages = "x" * products.paginator.num_pages
    
    context = {
            'title': 'StoreApp',
            'products': products,
            'categories' : ProductCategory.objects.all(),
            'max_pages': max_pages
    }
    
    return render(request, 'products/catalog.html', context)


def index(request):
    context = {
        'title': 'storeApp',
        'username' : 'Aisha Ait',
        'is_promotion' : False
    }
    return render(request, 'products/index.html', context)

@login_required
def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, products=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, products=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()
    print(request)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


@login_required
def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


# def listing(request):
#     prods = Product.objects.all()
#     paginator = Paginator(prods, 1)
#     page = request.GET.get('page')
#     obj = paginator.get_page(page)
#     return render(request, 'products/catalog.html', {'obj': obj})
