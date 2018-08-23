from django.shortcuts import render

from .models import Produto, Categoria


def product_list(request):
    context = {
        'produtos': Produto.objects.all()
    }
    return render(request, 'catalog/products.html', context)


def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    context = {
        'produto': produto
    }
    return render(request, 'catalog/product.html', context)


def categoria(request, slug):
    categoria = Categoria.objects.get(slug=slug)

    context = {
        'current_categoria': categoria,
        'produtos': Produto.objects.filter(categoria=categoria),
    }
    return render(request, 'catalog/categoria.html', context)
