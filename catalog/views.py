from django.shortcuts import render,get_object_or_404
from .models import Produto, Categoria
from django.views import generic


class ProductListView(generic.ListView):

    #model = Produto
    queryset = Produto.objects.all()
    template_name = 'catalog/products.html'
    context_object_name = 'produtos'

product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):
    template_name = 'catalog/category.html'
    context_object_name = 'produtos'

    def get_queryset(self):
        return Produto.objects.filter(categoria__slug=self.kwargs['slug'])

    def get_context_data(self):
        context= super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Categoria,slug=self.kwargs['slug'])
        return context








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
