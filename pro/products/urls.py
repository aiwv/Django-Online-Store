from django.urls import path, include

from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    # path('', views.check)
    path('catalog/', views.catalog, name='catalog')
]