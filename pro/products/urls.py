from django.urls import path, include
from . import views
from .views import basket_add, basket_remove

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.check)
    path('catalog/', views.catalog, name='catalog'),
    path('baskets/add/<int:product_id>/', basket_add, name='basket_add'),
    path('baskets/remove/<int:basket_id>/', basket_remove, name='basket_remove'),
]