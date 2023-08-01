from django.http import HttpResponse
from django.shortcuts import render


# Функции = контроллеры = вьюхи

def index(request):
    content = {
        'title': 'Store',
    }
    return render(request, 'products/index.html', content)


def products(request):
    content = {
        'title': 'Store - каталог',
        'products': [
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Худи черного цвета с монограммами adidas Originals',
                'price': 6090,
                'descripton': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'
            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Синяя куртка The North Face',
                'price': 6090,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            },
            {
                'image': '/static/vendor/img/products/Adidas-hoodie.png',
                'name': 'Синяя куртка The North Face',
                'price': 3390,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'
            }

        ]
    }
    return render(request, 'products/products.html', content)
