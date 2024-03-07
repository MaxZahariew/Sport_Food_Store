from django.http import HttpResponse
from django.shortcuts import render

from products.models import Categories

# Create your views here.
def index(request):

    categories = Categories.objects.all()
    context = {
        'title': "Sport Food",
        'categoryes': categories
    }
    return render(
        request, 'main/index.html', context=context
    )

def about(request):
    return render(
        request, 'main/index.html'
    )