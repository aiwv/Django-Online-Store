# Create your views here.
from django.shortcuts import render

# Create your views here.

def catalog(request):
    context = {
        'products' : [
            # {'name': 'худи черного цвета', 'price': '1950'},
            # {'name': 'худи черного цвета', 'price': '1950'}
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': '609000', 'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
            {'name': 'Синяя куртка The North Face', 'price': '23 725', 'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390', 'description': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        ]
    }
    return render(request, 'products/catalog.html', context)

def index(request):
    context = {
        'title': 'storeApp',
        'username' : 'Aisha Ait',
        'is_promotion' : False
    }
    return render(request, 'products/index.html', context)

# def catalog(request):
#     context = {
#         'title' : 'Catalog',

#     }
#     return render(request, 'products/catalog.html', context)