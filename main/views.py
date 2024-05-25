from django.http import HttpResponse
from django.shortcuts import render

from goods.models import Categories, Products


def index(request):
    products = Products.objects.all()[:8]
    products_2 = Products.objects.all().order_by('-rating')[:6]
    categories = Categories.objects.all()[:4]
    context = {
        'products': products,
        'cat': categories,
        'products_2' : products_2,
    }
    return render(request, 'main/index.html', context)


def shop(request):
    products = Products.objects.all()
    categories = Categories.objects.all()
    context = {
        'products': products,
        'cat': categories,
    }
    return render(request, 'goods/shop.html', context)

def about(request):
    context = {
        'title': 'Home - О нас',
        'content': "О нас",
        'text_on_page': "Текст о том почему этот магазин такой классный, и какой хороший товар."
    }

    return render(request, 'main/about.html', context)