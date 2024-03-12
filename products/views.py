from django.shortcuts import render

from .models import Products

# Create your views here.
def catalog(request):
    print(request)
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/catalog.html', context=context)


def products(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context=context)