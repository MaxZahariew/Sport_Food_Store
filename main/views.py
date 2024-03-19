from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from products.models import Categories

# Create your views here.
def index(request: HttpRequest):
    print(request.GET)
    context = {
        'title': "Sport Food",
    }
    return render(
        request, 'main/index.html', context=context
    )

def about(request):
    return render(
        request, 'main/index.html'
    )