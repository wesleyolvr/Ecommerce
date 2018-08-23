from django.shortcuts import render
from catalog.models import Categoria


def index(request):
    context={
        'texts':['eai brotheragem','beleza?']
    }
    return render(request, 'index.html',context)


def contact(request):
    return render(request, 'contact.html')


def product(request):
    return render(request, 'product.html')

