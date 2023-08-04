from django.http import HttpResponse
from django.shortcuts import render
from products.models import ProductCategory, Product

# Функции = контроллеры = вьюхи

def index(request):
    content = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'title': 'Store - каталог',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', content)