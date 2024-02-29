from django.shortcuts import render

# Create your views here.
def catalog(request):
    return render(request, 'products/catalog.html')


def products(request):
    return render(request, 'products/product.html')