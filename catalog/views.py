from django.shortcuts import render,get_object_or_404
from .models import Produto, Categoria
from django.views import generic


class ProductListView(generic.ListView):

    model = Produto
    template_name = 'catalog/products.html'
    context_object_name = 'produtos'
    paginate_by = 3

product_list = ProductListView.as_view()

class CategoriaListView(generic.ListView):
    template_name = 'catalog/categoria.html'
    context_object_name = 'produtos'
    paginate_by = 3

    def get_queryset(self):
        return Produto.objects.filter(categoria__slug=self.kwargs['slug'])

    def get_context_data(self,**kwargs):
        context= super(CategoriaListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Categoria,slug=self.kwargs['slug'])
        return context

categoria = CategoriaListView.as_view()

def produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    context = {
        'produto': produto
    }
    return render(request, 'catalog/product.html', context)

