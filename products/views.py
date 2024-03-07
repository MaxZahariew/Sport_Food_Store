from django.shortcuts import render

from .models import Products

# Create your views here.
def catalog(request):
    products = Products.objects.all()
    context = {
        'products': products
    }
    return render(request, 'products/catalog.html', context=context)


def products(request):
    return render(request, 'products/product.html')