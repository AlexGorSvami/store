from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from products.models import ProductCategory, Product, Basket
from users.models import User


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


def basket_add(request, product_id):
    product = Product.objects.get(id=product_id)
    baskets = Basket.objects.filter(user=request.user, product=product)

    if not baskets.exists():
        Basket.objects.create(user=request.user, product=product, quantity=1)
    else:
        basket = baskets.first()
        basket.quantity += 1
        basket.save()

    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def basket_remove(request, basket_id):
    basket = Basket.objects.get(id=basket_id)
    basket.delete()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
